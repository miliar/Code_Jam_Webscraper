#ifndef __SOME_UTILS_HPP__
#define __SOME_UTILS_HPP__

#include <iostream>
#include <fstream>
#include <vector>
#include <list>
#include <map>
#include <pthread.h>
#include <assert.h>
#include <climits>
#include <cmath>
#include <iomanip>
#include <cstdio>
#include <stdio.h>
#include <string.h>
#include <algorithm>
#include <queue>

#include <memory>
#include <thread>
#include <mutex>
#include <condition_variable>
#include <future>
#include <functional>
#include <stdexcept>
#include <sstream>

#include <opencv2/opencv.hpp>
#include <opencv2/core/core.hpp>

using namespace std;
using namespace cv;

// Utility
const string timeStamp()
{
	time_t rawtime;
	time(&rawtime);
	const tm* timeinfo = localtime (&rawtime);

	char dd[20];
	strftime(dd, sizeof(dd), "%Y%m%d_%H%M%S", timeinfo);

	return string(dd);
}

// using namespace boost;

struct gPoint
{
	gPoint(){}
	gPoint(const Point _p) : c(_p.x), r(_p.y) {}
	int c = 0;
	int r = 0;
	bool operator == (const gPoint& p) const{return r == p.r && c == p.c;}
	inline friend istream& operator>> (istream& is, gPoint& p) {is >> p.r; is >> p.c;return is;}
	inline friend ostream& operator<< (ostream& os, const gPoint& p) {os << p.r << " " << p.c; return os;}
	Point toPoint() const{
		return Point(c, r);
	}
	inline static double dist(const gPoint& pt1, const gPoint& pt2)
	{
		return sqrt((pt1.r-pt2.r)*(pt1.r-pt2.r)+(pt1.c-pt2.c)*(pt1.c-pt2.c));
	}
};

struct gLine
{
	gLine(){}
	gLine(const gPoint& _p1, const gPoint _p2) : p1(_p1), p2(_p2){}
	gLine(const Rect& _r) : p1(_r.tl()), p2(_r.br() - Point(1,1)){}
	gPoint p1;
	gPoint p2;
	Rect toRect() const{
		return Rect(p1.toPoint(), p2.toPoint() + Point(1,1));
	}
	bool operator == (const gLine& li) const{return p1 == li.p1 && p2 == li.p2;}
	inline friend istream& operator>> (istream& is, gLine& li) {is >> li.p1; is >> li.p2;return is;}
	inline friend ostream& operator<< (ostream& os, const gLine& li) {os << li.p1.r << " " << li.p1.c << " " << li.p2.r << " " << li.p2.c; return os;}
};

struct gSquare
{
	gSquare(){}
	gSquare(const Rect& _r){
		assert(_r.width == _r.height);
		s = (_r.width - 1) / 2;
		c = _r.x + s; 
		r = _r.y + s;
	}
	int r = 0;
	int c = 0;
	int s = 0;
	Rect toRect() const{
		return Rect(c - s, r - s, s * 2 + 1, s * 2 + 1);
	}
	bool operator == (const gSquare& sq) const{return r == sq.r && c == sq.c && s == sq.s;}
	inline friend istream& operator>> (istream& is, gSquare& sq) {is >> sq.r; is >> sq.c; is >> sq.s;return is;}
	inline friend ostream& operator<< (ostream& os, const gSquare& sq) {os << sq << " " << sq << " " << sq.s; return os;}
};

/// Class to create a pool of threads: do not change
class ThreadPool {
	public:
		// the constructor just launches some amount of workers
		inline ThreadPool(size_t threads):stop(false)
		{
			for(size_t i = 0;i<threads;++i)
				workers.emplace_back(
					[this]
					{
						for(;;)
						{
							std::function<void()> task;
							{
								std::unique_lock<std::mutex> lock(this->queue_mutex);
								this->condition.wait(lock, [this]{ return this->stop || !this->tasks.empty(); });
								if(this->stop && this->tasks.empty())
									return;
								task = std::move(this->tasks.front());
								this->tasks.pop();
							}
							task();
						}
					}
				);
		}
		template<class F, class... Args> auto enqueue(F&& f, Args&&... args) -> std::future<typename std::result_of<F(Args...)>::type>
		{
			using return_type = typename std::result_of<F(Args...)>::type;

			auto task = std::make_shared< std::packaged_task<return_type()> >(
					std::bind(std::forward<F>(f), std::forward<Args>(args)...)
					);

			std::future<return_type> res = task->get_future();
			{
				std::unique_lock<std::mutex> lock(queue_mutex);

				// don't allow enqueueing after stopping the pool
				if(stop)
					throw std::runtime_error("enqueue on stopped ThreadPool");

				tasks.emplace([task](){ (*task)(); });
			}
			condition.notify_one();
			return res;
		}
		// the destructor joins all threads
		inline ~ThreadPool()
		{
			{
				std::unique_lock<std::mutex> lock(queue_mutex);
				stop = true;
			}
			condition.notify_all();
			for(std::thread &worker: workers)
				worker.join();
		}
	private:
		// need to keep track of threads so we can join them
		std::vector< std::thread > workers;
		// the task queue
		std::queue< std::function<void()> > tasks;

		// synchronization
		std::mutex queue_mutex;
		std::condition_variable condition;
		bool stop;
};


#endif

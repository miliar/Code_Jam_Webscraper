#include <fstream>
#include <iomanip>
#include <string>
#include <vector>
#include <cassert>
#include <iostream>
#include <limits>
#include <map>
#include <algorithm>

#include <thread>
#include <mutex>
#include <condition_variable>
#include <queue>
#include <functional>
#include <limits>

using namespace std;

struct noncopyable {
  noncopyable(const noncopyable&) = delete;
  noncopyable& operator=(const noncopyable&) = delete;
  noncopyable() {}
};

typedef std::lock_guard<std::mutex> lguard;
typedef std::unique_lock<std::mutex> ulock;

constexpr size_t def_locked_queue_max_size = 20;
constexpr size_t def_num_threads = 2;

template<class T> class LockedQueue : noncopyable {
  mutable std::mutex m_mutex;
  std::condition_variable m_cond;
  std::queue<T> m_queue;
  const size_t m_max_size;
  size_t m_returned;
  bool m_stop;
  size_t m_waiting;
 public:

  enum { C_STOP = std::numeric_limits<size_t>::max() };

  typedef T value_type;

   LockedQueue(size_t max_size = def_locked_queue_max_size) : m_max_size(max_size), 
    m_returned(0), m_stop(false), m_waiting(0) {}

  ~LockedQueue() {
    assert(0 == m_waiting);
  }
  void push(const T& v) {
    lguard l(m_mutex);
    m_queue.push(v);
    m_cond.notify_one();
  }
  void push(T&& v) {
    lguard l(m_mutex);
    m_queue.push(std::move(v));
    m_cond.notify_one();
  }
  size_t pop(T& v) {
    ulock lock(m_mutex);
    while (m_queue.empty()) {
      if (m_stop) {
	return C_STOP;
      }
      ++m_waiting;
      m_cond.wait(lock);
      --m_waiting;
    }
    v = std::move(m_queue.front());
    m_queue.pop();
    return m_returned++;
  }
  size_t size() const {
    lguard(m_mutex);
    return m_queue.size();
  }
  size_t empty() const {
    lguard l(m_mutex);
    return m_queue.empty();
  }
  void stop() {
    {
      lguard l(m_mutex);
      m_stop = true;
    }
    m_cond.notify_all();
  }
};

class ThreadPool : noncopyable {
  std::vector<std::thread> m_threads;
  bool m_stoped;
public:
  template<class F> ThreadPool(size_t n, const F& f = F()) : m_stoped(false) {
    while (n-- > 0) {
      m_threads.push_back(std::thread(f));
    }
  }
  ~ThreadPool() {
    wait();
  }
  void wait() {
    if (!m_stoped) {
      for (auto& t : m_threads) {
	t.join();
      }
      m_stoped = true;
    }
  }
};

template<class T, class R> class Runner2 {
  LockedQueue<T> m_queue;
  std::vector<R> m_out;
  ThreadPool m_pool;
  template<class F> void processq(F func) {
    while (1) {
      T value;
      auto i = m_queue.pop(value);
      if (i == LockedQueue<T>::C_STOP) {
	return;
      }
      m_out[i] = func(std::move(value));
      //cout << i << ' ';
      //cout.flush();
    }
  }
 public:
  template<class F> Runner2(size_t n, const F& func) : m_pool(def_num_threads, std::bind(&Runner2::processq<F>, this, func)) {
    m_out.resize(n);
  }
  ~Runner2() {
    wait();
  }
  
  void push(T&& t) {
    m_queue.push(std::move(t));
  }
  void push(const T& t) {
    m_queue.push(t);
  }
  void wait() {
    m_queue.stop();
    m_pool.wait();
  }
  const std::vector<R>& result() {
    wait();
    return m_out;
  }
};

/////

struct Files : noncopyable {
  std::fstream in;
  std::fstream out;

  static std::string name_to_out(const std::string& s) {
    if (s.substr(s.size()-3) == ".in") {
      return s.substr(0, s.size()-3)+".out";
    } else {
      return s+".out";
    }
  }

  Files(const std::string& name) : in(name.c_str(), std::ios_base::in),
    out(name_to_out(name).c_str(), std::ios_base::out) {
  }

  size_t get_numline() {
    size_t N;
    in >> N;
    std::string es;
    std::getline(in, es);
    if (!es.empty()) {
      assert(false);
    }
    return N;
  }

  template<class T> std::vector<T> get_vec(size_t n) {
    std::vector<T> v;
    v.reserve(n);
    while (n-- > 0) {
      T tmp;
      in >> tmp;
      v.push_back(std::move(tmp));
    }
    return v;
  }

  template<class T> T get() {
    T tmp;
    in >> tmp;
    return tmp;
  }
};

constexpr size_t inf = std::numeric_limits<int>::max(); //!!! size_t = MAX_INT

vector<size_t> sqrt_table;

size_t sqrt(size_t n) {
  return sqrt_table[n];
}

void fill_sqrt(size_t max) {
  sqrt_table.resize(max+1);
  sqrt_table[0] = 0;
  size_t k = 1;
  size_t i = 1;
  while (1) {
    size_t m = k*k;
    while (i < m) {
      if (i > max) {
	return;
      }
      sqrt_table[i] = k-1;
      //cout << (k-1) << ' ';
      ++i;
    }
    ++k;
  }
}

size_t solve1(vector<size_t> v, size_t pos);

size_t solve(vector<size_t> x) {
  vector<size_t> v(1001);
  size_t pos = 0;
  for(size_t c : x) {
    ++v[c];
    if (c > pos) { //finding max 
      pos = c;
    }
  }
  return solve1(move(v), pos);
}

size_t solve1(vector<size_t> v, size_t max_pos) {
  //size_t max_wait = 1;
  //size_t moves = 0;
  map<size_t, size_t> min;
  min[0] = 0;
  for (size_t pos = 1; pos <= max_pos; ++pos) {
    if (v[pos] > 0) {
      map<size_t, size_t> new_min;
      new_min[0] = pos;
      for (auto& p : min) {
	//size_t min = p.first+pos;
	size_t moves = p.first;
	size_t max_wait = p.second;
	for (size_t parts = sqrt(pos); parts >= 1; --parts) {
	  size_t min_res = pos/parts;
	  size_t plus_one = pos%parts;
	  size_t wait = min_res+(plus_one>0);

	  size_t new_moves = moves + (parts-1)*v[pos];
	  if (new_min.count(new_moves) == 0 || new_min[new_moves] > max(wait, max_wait)) {
	    new_min[new_moves] = std::max(wait, max_wait);
	  } else {
	    break;
	  }
	}
      }
      /*
      for (auto& p : new_min) {
	cout << p.first << "m:" << p.second << "sec  ";
      }
      cout << endl;
      */
      min.swap(new_min);
    }
  }
  size_t res = inf;
  for (auto& p : min) {
    if (res > p.first+p.second) {
      res = p.first+p.second;
    }
  }
  return res;
}

size_t solveS(const string& s) {
  vector<size_t> x(s.size());
  for (size_t i = 0 ; i < s.size(); ++i) {
    x[i] = s[i]-'0';
  }
  return solve(x);
}

void test() {
  assert(2 == solveS("1212"));
  assert(3 == solveS("4"));
  assert(5 == solveS("23454"));
  assert(6 == solveS("559"));
  assert(8 == solveS("6875"));
  assert(5 == solveS("66"));
  assert(8 == solveS("666699"));
  assert(6 == solveS("96"));
  assert(7 == solveS("9666"));
  assert(8 == solveS("9597"));
  assert(6 == solveS("475"));
  assert(7 == solveS("8475"));
  assert(5 == solveS("148"));
  assert(8 == solveS("299933"));
  assert(8 == solveS("999"));
  cout << "Tests OK" << endl;
}

int main(int argc, char** argv) {
  fill_sqrt(1000); 

  if (argc < 2) {
    std::cerr << "Use ./a.out <file>" << std::endl;
    test();
    return 1;
  }

  Files f(argv[1]);
  size_t T;
  f.in >> T;

  Runner2<vector<size_t>, size_t> r(T, solve);
  for (size_t t = 1; t <= T; ++t) {
    size_t d;
    f.in >> d;
    vector<size_t> x = f.get_vec<size_t>(d);
    r.push(move(x));
    //auto min = solve(x);
    /*
    cout << t << ": ";
    for (auto c : x) {
      cout << c;
    }
    cout << endl;
    */
    //f.out << "Case #" << t << ": " << min << endl;
  }

  vector<size_t> res = r.result();
  for (size_t t = 1; t <= T; ++t) {
    f.out << "Case #" << t << ": " <<  res[t-1] << endl;
  }
}

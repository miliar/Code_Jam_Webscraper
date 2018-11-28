#include <iostream>
#include <cstdint>
#include <vector>
#include <condition_variable>
#include <atomic>
#include <mutex>
#include <queue>
#include <boost/thread/thread.hpp>

using namespace std;

struct info {
	char str[10001];
	uint64_t reallen;
	uint64_t partsnum;
	char loopres = 0;
	uint64_t index;
};

vector<bool> results;
atomic_uint done;
queue<info*> tasks;
mutex mtx;
condition_variable cond;

char resi[8] = { 1, 7, 4, 2, 5, 3, 0, 6 };
char resj[8] = { 2, 3, 7, 6, 1, 0, 4, 5 };
char resk[8] = { 3, 5, 1, 7, 0, 6, 2, 4 };

/*
0: 1
1: i
2: j
3: k
7: -1
6: -i
5: -j
4: -k
*/

char __inline nextc(char cur, char next) {
	switch (next) {
	case 'i':
		return resi[cur];
	case 'j':
		return resj[cur];
	case 'k':
		return resk[cur];
	}
}

bool parsefork(uint64_t starti, uint64_t startp, info *inf) {
	if (startp == inf->partsnum)
		return false;
	char cur = 0;
	for (uint64_t i = starti; i < inf->reallen; i++) {
		cur = nextc(cur, inf->str[i]);
	}
	/*for (uint64_t p = startp + 1; p < partsnum; p++) {
		for (uint64_t i = 0; i < reallen; i++) {
			cur = nextc(cur, str[i]);
		}
	}*/
	//return cur == 3;
	if (startp + 1 < inf->partsnum) {
		//	cerr << "hi " << (int)loopres << " bye" << endl;
		if (inf->loopres == (char)0xFF) {
			inf->loopres = 0;
			for (uint64_t i = 0; i < inf->reallen; i++) {
				inf->loopres = nextc(inf->loopres, inf->str[i]);
			}
			//cerr << "loopres " << (int)loopres << endl;
		}
		switch (inf->loopres) {
		case 0:
			return cur == 3;
		case 7:
			if ((inf->partsnum - (startp + 1)) % 2 == 0)
				return cur == 3;
			else
				return (7 - cur) == 3;
		default:
			if (inf->loopres > 3) {
				char loopres2 = 7 - inf->loopres;
				loopres2 = 'i' + loopres2 - 1;
				for (uint64_t p = startp + 1; p < inf->partsnum; p++) {
					cur = 7 - nextc(cur, loopres2);
				}
			} else {
				char loopres2 = 'i' + inf->loopres - 1;
				for (uint64_t p = startp + 1; p < inf->partsnum; p++) {
					cur = nextc(cur, loopres2);
				}
			}
			return cur == 3;
		}
	} else {
		return cur == 3;
	}
}

bool parseforj(uint64_t starti, uint64_t startp, info *inf) {
	if (startp == inf->partsnum)
		return false;
	char cur = 0;
	for (uint64_t i = starti; i < inf->reallen; i++) {
		cur = nextc(cur, inf->str[i]);
		if (cur == 2 && parsefork(i + 1, startp, inf))
			return true;
	}
	for (uint64_t p = startp + 1; p < inf->partsnum; p++) {
		for (uint64_t i = 0; i < inf->reallen; i++) {
			cur = nextc(cur, inf->str[i]);
			if (cur == 2 && parsefork(i + 1, p, inf))
				return true;
		}
	}	
	return false;
}

bool parsefori(info *inf) {
	char cur = 0;
	for (uint64_t p = 0; p < inf->partsnum; p++) {
		for (uint64_t i = 0; i < inf->reallen; i++) {
			cur = nextc(cur, inf->str[i]);
			if (cur == 1 && parseforj(i + 1, p, inf))
				return true;
		}
	}
	return false;
}

void worker() {
	while (true) {
		info *inf;
		{
			unique_lock<mutex> lock(mtx);
			while (tasks.empty())
				cond.wait(lock);
			inf = tasks.front();
			tasks.pop();
		}
		results[inf->index] = parsefori(inf);
		delete inf;
		done++;
	}
}

int main(int argc, char *argv[]) {
	uint64_t casenum;
	char c;
	done.store(0);
	for (int i = 0; i < 8; i++)
		boost::thread a(worker);
	cin >> casenum;
	for (uint64_t ccase = 0; ccase < casenum; ccase++) {
		info *inf = new info();
		cin >> inf->reallen >> inf->partsnum;
		cin >> c;
		while (c != 'i' && c != 'j' && c != 'k')
			cin >> c;
		inf->str[0] = c;
		for (uint64_t i = 1; i < inf->reallen; i++) {
			cin >> c;
			inf->str[i] = c;
		}
		inf->loopres = 0xFF;
		inf->index = ccase;
		results.push_back(false);
		{
			unique_lock<mutex> lock(mtx);
			tasks.push(inf);
			cond.notify_one();
		}
	}
	while (done != casenum)
		boost::this_thread::sleep(boost::posix_time::milliseconds(100));
	for (uint64_t ccase = 0; ccase < casenum; ccase++) {
		cout << "Case #" << ccase + 1 << ": " << (results[ccase] ? "YES" : "NO") << endl;
	}
	exit(0);
}
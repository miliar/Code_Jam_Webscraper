#define _CRT_SECURE_NO_DEPRECATE
#include <iostream>
#include <sstream>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <memory.h>
#include <cctype>
#include <string>
#include <vector>
#include <list>
#include <queue>
#include <deque>
#include <stack>
#include <map>
#include <set>
#include <algorithm>
#include <thread>
using namespace std;

typedef long double Double;
typedef vector<int> VInt;
typedef vector< vector<int> > VVInt;
typedef long long Int;
typedef pair<int, int> PII;

#define FOR(i, n, m) for(i = n; i < m; ++i)
#define RFOR(i, n, m) for(i = (n) - 1; i >= (m); --i)
#define CLEAR(x, y) memset(x, y, sizeof(x))
#define COPY(x, y) memcpy(x, y, sizeof(x))
#define PB push_back
#define MP make_pair
#define SIZE(v) ((int)((v).size()))
#define ALL(v) (v).begin(), (v).end()

// compilation:
// g++ -std=c++11 -pthread -O2 file.cpp
// clang++ -std=c++11 -stdlib=libc++ file.cpp
//============================================================

bool PRINT_TESTS_PROGRESS = true;
const int THREADS = 8;

const int MAX_TESTS = 100;

struct TestCase {
  // input/output data goes here
  int N;
  vector<vector<string> > S;
  int res;

  void read() {
    char buf[20000];
    gets(buf);
    sscanf(buf, "%d", &N);
    for (int i = 0 ; i < N; ++i) {
      gets(buf);
      istringstream ss(buf);
      string s;
      vector<string> w;
      while (ss >> s)
	w.PB(s);
      S.PB(w);
    }
  }

  void solve() {
    // solution goes here

    map<string, int> ids;
    vector<vector<int>> SI;
    int id = 0;
    for (int i = 0; i < N; ++i) {
      SI.PB(vector<int>());
      for (int j = 0; j < S[i].size(); ++j) {
	if (ids.find(S[i][j]) == ids.end()) {
	  ids[S[i][j]] = id;
	  SI[i].PB(id);
	  ++id;
	} else {
	  SI[i].PB(ids[S[i][j]]);
	}
      }
    }

    vector<int> Lang(id, 0);

    res = 1000000;
    int smask = (1<<N);
    for (int mask = 1; mask < smask; mask += 4) {
      set<int> s[2];
      int cr = 0;
      for (int i = 0; i < id; i++)
	Lang[i] = -1;
      for (int i = 0; i < N; ++i) {
	int l = 0;
	if (mask & (1<<i)) {
	  l = 1;
	}
	vector<int> & SIi = SI[i];
	for (int j = 0; j < SI[i].size(); ++j) {
	  int p = SIi[j];
	  if (Lang[p] == -1) {
	    Lang[p] = l;
	  } else if (Lang[p] != 2) {
	    if (Lang[p] != l) {
	      Lang[p] = 2;
	      ++cr;
	    }
	  }
	}
      }
      res = min(res, cr);
    }

  }

  void print(int testId) {
    printf("Case #%d: %d\n", testId+1, res);

  }
};

//============================================================


queue<int> _testQueue;
mutex _testQueueMutex;
int _testsDone;
int _allTests;

TestCase Tests[MAX_TESTS];

void _solveTest(int testId) {
  Tests[testId].solve();
}

void _solveTestsFromQueue() {
  while (true) {
    int nextTest = -1;
    {
      lock_guard<mutex> lock(_testQueueMutex);
      if (_testQueue.empty()) break;
      nextTest = _testQueue.front();
      _testQueue.pop();
    }
    _solveTest(nextTest);
    if (PRINT_TESTS_PROGRESS) {
      lock_guard<mutex> lock(_testQueueMutex);
      ++_testsDone;
      fprintf(stderr, "Done %d/%d (test %d)\n", _testsDone, _allTests, nextTest + 1);
    }
  }
}

void _readTests() {
  int T;
  scanf("%d", &T);
  char buf[10];
  gets(buf);
  for (int t = 0; t < T; ++t) {
    Tests[t].read();
    _testQueue.push(t);
  }
  _allTests = T;
}

void _solveTests() {
  thread threads[THREADS];
  for (int i = 0; i < THREADS; ++i) {
    threads[i] = thread(_solveTestsFromQueue);
  }
  for (int i = 0; i < THREADS; ++i) {
    threads[i].join();
  }
}

void _printResults() {
  for (int i = 0; i < _allTests; ++i) {
    Tests[i].print(i);
  }
}

int main() {
  _readTests();
  _solveTests();
  _printResults();
  return 0;
};

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

const int MAX_TESTS = 101;

int Dir[4][2] = {{-1, 0}, {0, 1}, {1, 0}, {0, -1}};

struct Point {
  int x, y;
};

struct TestCase {
  // input/output data goes here
  char B[110][110];
  int R, C;

  int res;

  void read() {
    scanf("%d%d", &R, &C);
    for (int i = 0 ; i < R; ++i)
      scanf("%s", B[i]);
  }

  Point next(const Point& p, int d) {
    Point np = p;
    int dx = Dir[d][0];
    int dy = Dir[d][1];
    np.x += dx;
    np.y += dy;
    while (np.x >= 0 && np.x < R && np.y >= 0 && np.y < C) {
      if (B[np.x][np.y] != '.')
	break;
      np.x += dx;
      np.y += dy;
    }
    if (np.x >= 0 && np.x < R && np.y >= 0 && np.y < C) {
      return np;
    }
    np.x = np.y = -1;
    return np;
  }

  void solve() {
    // solution goes here
    res = 0;
    vector<Point> P;
    for (int i = 0 ; i < R; ++i)
      for (int j = 0; j < C; ++j)
	if (B[i][j] != '.') {
	  if (B[i][j] == '^') B[i][j] = 0;
	  if (B[i][j] == '>') B[i][j] = 1;
	  if (B[i][j] == 'v') B[i][j] = 2;
	  if (B[i][j] == '<') B[i][j] = 3;
	  Point p;
	  p.x = i;
	  p.y = j;
	  P.PB(p);
	}
    bool bad = false;
    for (int i = 0; i < P.size() && !bad; ++i) {
      Point p = next(P[i], B[P[i].x][P[i].y]);
      if (p.x == -1) {
	int d;
	for (d = 0; d < 4; ++d) {
	  p = next(P[i], d);
	  if (p.x != -1)
	    break;
	}
	if (d < 4)
	  res++;
	else
	  bad = true;
      }
    }
    if (bad)
      res = -1;
  }

  void print(int testId) {
    printf("Case #%d: ", testId+1);
    if (res == -1)
      printf("IMPOSSIBLE\n");
    else
      printf("%d\n", res);
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

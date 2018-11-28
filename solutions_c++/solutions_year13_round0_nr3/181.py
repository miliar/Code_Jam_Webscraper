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

#define MAX 120

struct Long {
  vector<char> A;
  
  Long() {
    A.resize(MAX, 0);
  }

  Long(const Long& L) {
    A = L.A;
  }
  
  bool isPal() {
    int i = MAX-1;
    while (i >= 0 && A[i] == 0)
      --i;
    if (i < 0)
      return false;
    ++i;
    for (int j = i/2; j >= 0; --j)
      if (A[j] != A[i-1-j])
	return false;
    return true;
  }

  void squareIt() {
    vector<char> B;
    B.resize(MAX, 0);

    int rem = 0;
    for (int i = 0; i < MAX; ++i)
      for (int j = 0; i+j < MAX; ++j) {
	B[i+j] += A[i] * A[j] + rem;
	if (B[i+j] >= 10) {
	  rem = B[i+j] / 10;
	  B[i+j] %= 10;
	} else {
	  rem = 0;
	}
      }
    A = B;
  }

  bool operator < (const Long& L) const {
    for (int i = MAX-1; i >= 0; --i)
      if (A[i] != L.A[i])
	return A[i] < L.A[i];
    return false;
  }

  int numDigs() {
    int i = MAX-1;
    while (i > 0 && A[i] == 0)
      --i;
    return i+1;
  }

  vector<Long> genInserts() {
    int KD = 2;

    vector<Long> res;
    int digs = numDigs();
    for (int k = 0; k+k <= digs; ++k) {
      Long a;
      for (int i = 0; i < k; ++i) {
	a.A[i] = A[i];
	a.A[digs+1 - i] = A[digs-1-i];
      }
      for (int i = k; i < digs-k; ++i)
	a.A[i+1] = A[i];
      
      for (int nd = 0; nd < KD; ++nd) {
	Long b(a);
	b.A[k] = nd;
	b.A[digs+1-k] = nd;

	Long c(b);
	b.squareIt();
	if (b.isPal()) {
	  res.PB(c);
	}
      }
    }

    if ((digs & 1) == 0) {
      Long a;
      int k = digs / 2;
      for (int i = 0; i < k; ++i) {
	a.A[i] = A[i];
	a.A[digs-i] = A[digs-1-i];
      }

      for (int nd = 0; nd < KD; ++nd) {
	Long b(a);
	b.A[k] = nd;

	Long c(b);
	b.squareIt();
	if (b.isPal()) {
	  res.PB(c);
	}
      }
    }

    return res;
  }

  void init(Int x) {
    A = vector<char>(MAX, 0);
    for (int i = 0; i < MAX && x; ++i) {
      A[i] = x % 10;
      x /= 10;
    }
  }

  void init(char * buf) {
    A = vector<char>(MAX, 0);
    for (int i = strlen(buf)-1, j = 0; i >= 0; --i, ++j)
      A[j] = buf[i] - '0';
  }


  void print() const {
    int i = MAX-1;
    while (i >= 0 && A[i] == 0)
      --i;
    for (i; i >= 0; --i)
      printf("%d", A[i]);
  }
};



char buf[100];

bool isPal(Int x) {
  sprintf(buf, "%lld", x);
  int L = strlen(buf);
  for (int i = L-1; i >= 0; --i)
    if (buf[i] != buf[L-1-i])
      return false;
  return true;
}

int main()
{
  vector<Int> res;
  for (Int x = 1; x <= 10000000; ++x)
    if (isPal(x) && isPal(x*x)) {
      res.PB(x);
    }

  queue<Long> Q;
  set<Long> all;
  for (int i = 0; i < res.size(); ++i) {
    Long a;
    a.init(res[i]);
    Q.push(a);
    all.insert(a);
  }
  
  int mdigs = 52;

  while (!Q.empty()) {
    Long a = Q.front();
    Q.pop();
    vector<Long> na = a.genInserts();
    for (int i = 0; i < na.size(); ++i)
      if (na[i].numDigs() <= mdigs && all.find(na[i]) == all.end()) {
	all.insert(na[i]);
	Q.push(na[i]);
      }
  }

  vector<Long> VR;
  
  for (set<Long>::iterator it = all.begin(); it != all.end(); ++it) {
    Long a(*it);
    a.squareIt();
    VR.PB(a);
    //    a.print();
    //    printf("\n");
  }

  fprintf(stderr, "Finished precalc\n");


  int T, t;
  scanf("%d", &T);
  char bufa[200];
  char bufb[200];
  for (t = 0; t < T; ++t) {
    scanf("%s%s", bufa, bufb);

    Long aa, bb;
    aa.init(bufa);
    bb.init(bufb);

    int r = 0;

    for (int i = 0; i < VR.size(); ++i) {
      if ((! (VR[i] < aa)) && (! (bb < VR[i])))
	++r;
    }

    printf("Case #%d: %d\n", t+1, r);
    fprintf(stderr, "Case #%d: %d\n", t+1, r);
  }
  


  return 0;
};

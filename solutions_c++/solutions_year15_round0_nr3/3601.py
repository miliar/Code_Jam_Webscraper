#pragma comment (linker, "/STACK:1073741824")
#define _USE_MATH_DEFINES
#include <math.h>
#include <time.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <assert.h>
#include <fstream>
#include <iostream>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <deque>
#include <vector>
#include <string>
#include <bitset>
#include <complex>

using namespace std;

#define SZ(x) (int((x).size()))
#define FOR(i, a, b) for(int (i) = (a); (i) <= (b); ++(i))
#define ROF(i, a, b) for(int (i) = (a); (i) >= (b); --(i))
#define REP(i, n) for (int (i) = 0; (i) < (n); ++(i))
#define REPD(i, n) for (int (i) = (n); (i)--; )
#define FE(i, a) for (int (i) = 0; (i) < (int((a).size())); ++(i))
#define MEM(a, val) memset((a), val, sizeof(a))
#define INF 1000000000
#define LLINF 1000000000000000000LL
#define PB push_back
#define PPB pop_back
#define ALL(c) (c).begin(), (c).end()
#define SQR(a) ((a)*(a))
#define MP(a,b) make_pair((a), (b))
#define XX first
#define YY second
#define GET_RUNTIME_ERROR *(int*)(NULL) = 1

typedef vector<int> vint;
typedef vector<long long> vLL;
typedef double dbl;
typedef long double ldbl;
typedef vector<pair<int, int> > vpii;
typedef long long LL;
typedef pair<int, int> pii;

int mult_t[4][4] = {
{1,  2,  3,  4},
{2, -1,  4, -3},
{3, -4, -1,  2},
{4,  3, -2, -1},
};

int sign(int a) {
  if (a == 0) return 0;
  return a > 0 ? 1 : -1;
}

int mult(int a, int b) {
  int sgn = sign(a * b);
  a = abs(a) - 1;
  b = abs(b) - 1;
  int res = mult_t[a][b] * sgn;
  return res;
}

int get(char c) {
  if (c == '1') return 1;
  if (c == 'i') return 2;
  if (c == 'j') return 3;
  if (c == 'k') return 4;
  assert(false);
}

bool solve(int x, string s0) {
  string s;
  REP(i, x) {
    s += s0;
  }

  int least = INF;
  int most = -INF;
  int l = 1;
  int r = 1;
  int all = 1;
  REP(i, s.size()) {
    int c = get(s[i]);
    all = mult(all, c);
  }
  if (all != -1) return false;

  REP(i, s.size()) {
    int c = get(s[i]);
    l = mult(l, c);
    if (l == 2) {
      least = i;
      break;
    }
  }
  REPD(i, s.size()) {
    int c = get(s[i]);
    r = mult(c, r);
    if (r == 4) {
      most = i;
      break;
    }
  }

  return least < most;
}

char s[10100];

int main() {
#ifdef    CENADAR_DEBUG
  freopen("/home/maksym/Downloads/C-small-attempt0.in", "r", stdin);
  freopen("output.txt", "w", stdout);
//  freopen("errput.txt", "w", stderr);
#else  // CENADAR_DEBUG
//  freopen("input.txt", "r", stdin);
//  freopen("output.txt", "w", stdout);
#endif // CENADAR_DEBUG

  int T;
  cin >> T;
  REP(i, T) {
    int l, x;
    scanf("%d%d%s", &l, &x, s);

    bool ans = solve(x, s);
    printf("Case #%d: ", i + 1);
    printf(ans ? "YES\n" : "NO\n");
  }

  return 0;
}

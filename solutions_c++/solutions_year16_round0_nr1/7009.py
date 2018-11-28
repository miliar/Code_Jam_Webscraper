#define _CRT_SECURE_NO_DEPRECATE
#pragma comment(linker, "/STACK:128777216")

#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>

#include <algorithm>
#include <vector>
#include <map>
#include <set>
#include <bitset>
#include <queue>
#include <deque>
#include <stack>

#include <math.h>
#include <cmath>
#include <string>
#include <cstring>
#include <string.h>

#include <memory.h>
#include <cassert>
#include <time.h>

using namespace std;

#define forn(i,n) for (int i = 0; i < (int)(n); i++)
#define fornd(i, n) for (int i = (int)(n) - 1; i >= 0; i--)
#define forab(i,a,b) for (int i = (int)(a); i <= (int)(b); i++)
#define forabd(i, b, a) for (int i = (int)(b); i >= (int)(a); i--)
#define forit(i, a) for (__typeof((a).begin()) i = (a).begin(); i != (a).end(); i++)

#define _(a, val) memset (a, val, sizeof (a))
#define sz(a) (int)((a).size())
#define pb push_back
#define mp make_pair
#define all(v) (v).begin(), (v).end()

typedef long long lint;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int, int> pii;
typedef vector<int> vii;

const lint LINF = 1000000000000000000LL;
const int INF = 1000000000;
const long double eps = 1e-9;
const long double PI = 3.1415926535897932384626433832795l;

#ifdef MY_DEBUG
#define dbgx( x ) { cerr << #x << " = " << x << endl; }
#define dbg( ... ) { fprintf(stderr, __VA_ARGS__); fflush(stderr); }
#else
#define dbgx( x ) {  }
#define dbg( ... ) {  }
#endif

void prepare(string s) {
#ifdef MY_DEBUG
  freopen("/home/dima/ClionProjects/gcj_r1/input.txt", "r", stdin);
  freopen("/home/dima/ClionProjects/gcj_r1/output.txt", "w", stdout);
#endif
}

lint n;
int used[10];

void read() {
  scanf("%lld", &n);
}

bool check() {
  forn(i, 10)
    if (!used[i])
      return false;
  return true;
}

void apply(lint n) {
  if (n == 0) {
    used[n] = 1;
    return;
  }
  while (n > 0) {
    used[n % 10] = 1;
    n /= 10;
  }
}

void solve() {
  if (n == 0) {
    printf("INSOMNIA\n");
    return;
  }
  _(used, 0);
  int k = 0;
  do {
    apply(n * ++k);
  } while (!check());
  printf("%lld\n", n*k);
}

int main() {
  prepare("");

  int T;
  scanf("%d", &T);
  forn(i, T) {
    printf("Case #%d: ", i + 1);
    read();
    solve();
  }
  dbg("Clock = %.3f\n", clock() / (double) CLOCKS_PER_SEC);
  return 0;
}

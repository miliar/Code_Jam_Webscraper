#include <cstdlib>
#include <cstring>
#include <cstdio>
#include <cassert>
#include <cmath>
#include <vector>
#include <algorithm>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <bitset>
#include <string>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>

using namespace std;

typedef vector<string> vs;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef long long LL;
typedef vector<LL> vl;
typedef vector<double> vd;

#define FOR(i,n) for (i = 0; i < (n); i++)
#define FORI(i,a,b) for (i = (a); i <= (b); i++)
#define FORD(i,a,b) for (i = (a); i >= (b); i--)
#define FOREACH(i, x) for (typeof((x).begin()) i = (x).begin(); i != (x).end(); i++)
#define ZERO(a) memset(a, 0, sizeof(a))
#define MINUS(a) memset(a, -1, sizeof(a))
#define SZ(a) (a.size())
#define MP(a, b) make_pair(a, b)
#define SHL(a,b) ((a) << (b))
#define SHR(a,b) ((a) >> (b))
#define FI first
#define SE second
#define PB push_back

template<class T> int bitcount(T a) { int x = 0; while (a) { x += (a & 1); a >>= 1; } return x; }
template<class T> inline T gcd(T a, T b) { return b ? gcd(b, a % b) : a; }
template<class T> inline T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> inline T sqr(T a) { return a * a; } // NOTE: T must be enough to save sqr!
inline int parity(LL a) { return __builtin_parityl(a); }
inline int parity(int a) { return __builtin_parity(a); }
template<class T> T s2type(string s) { T res; istringstream in(s); in >> res; return res; }
template<class T> string toString(T n) { ostringstream out; out << n; return out.str(); }

const double PI = acos(-1.0);
const double EPS = 1e-11;

int n, m, ans1;
char s[1024][128];
int len[1024];
int d[8];
LL ans2;

void buildtrie()
{
  int i, j, k;
  int l = n, first, prev;

  FOR(i, n) {
    first = 1;
    FOR(j, m) {
      if (d[j] == i) {
        if (first) {
          l += len[j];
          first = 0;
          prev = j;
        }
        else {
          FOR(k, min(len[prev], len[j])) if (s[prev][k] != s[j][k]) break;
          l += len[j] - k;
          prev = j;
        }
      }
    }
  }

  if (l == ans1) ans2++;
  else if (l > ans1) { ans1 = l; ans2 = 1; }
}

void recurse(int idx) {
  if (idx == m) {
    int c[4];
    int i;
    ZERO(c);
    FOR(i, m) c[d[i]] = 1;
    FOR(i, n) if (!c[i]) return;
    buildtrie();
  }
  else {
    int i;
    FOR(i, n) {
      d[idx] = i;
      recurse(idx + 1);
    }
  }
}

void doit()
{
  ans1 = -1;
  ans2 = 0LL;
  recurse(0);
}

char x[128];

int main()
{
  int i, j, k;
  int t, tc;

  scanf("%d", &tc);
  FOR(t, tc) {
    ZERO(s);
    scanf("%d %d", &m, &n);
    FOR(i, m) scanf("%s", s[i]);
    FOR(i, m)
      FORI(j, i + 1, m - 1)
        if (strcmp(s[i], s[j]) > 0) {
          strcpy(x, s[i]);
          strcpy(s[i], s[j]);
          strcpy(s[j], x);
        }
    FOR(i, m) len[i] = strlen(s[i]);
//    FOR(i, m) printf("%s\n", s[i]);
    doit();
    printf("Case #%d: %d %lld\n", t + 1, ans1, ans2);
  }
  return 0;
}


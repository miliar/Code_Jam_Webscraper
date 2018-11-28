#include <iostream>
#include <set>
#include <vector>
#include <string>
#include <algorithm>
#include <cstdio>
#include <cstring>
#include <cmath>
#include <cstdlib>
#include <stack>
#include <queue>
#include <map>

using namespace std;

char fi;

const int INF = 2000000000;
const long long int LINF = (1L<<63) - 1L;

#define FOR(v, i) for (int i = 0; i < int(v.size()); ++i)
#define For(a, b, i) for (int i = a; i < b; ++i)
#define TR(m, it) for (set<int>::iterator it = m.begin(); it != m.end(); ++it)
#define menja scanf ("%c", &fi)
#define debug(var) cerr << #var << " : " << var << '\n';

typedef long long int lol;
typedef unsigned long long int lel;
typedef vector<int> VI;
typedef pair<int, int> ii;
typedef vector<VI> VVI;
typedef vector<ii> VII;
typedef vector<VII> VVII;
typedef vector<string> VS;
typedef vector<double> VD;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef long double ld;
typedef map<int, int> mii;
typedef vector<mii> VMII;
typedef pair<int, ii> iii;
typedef set<int> si;
typedef vector<si> VSI;
typedef vector<VSI> VVSI;

int main() {
  ios_base::sync_with_stdio(false);
  cout.setf(ios::fixed);
  cout.precision(10);
  int t;
  scanf ("%d\n", &t);
  for (int cas = 1; cas <= t; ++cas) {
    int n;
    scanf ("%d ", &n); ++n;
    VI shy (n);
    FOR(shy, i) scanf ("%1d", &shy[i]);
    menja;
    int ac = 0, ans = 0;
    FOR(shy, i) {
      if (ac >= i) ac += shy[i];
      else {
	ans += (i - ac);
	ac = i + shy[i];
      }
    }
    printf ("Case #%d: %d\n", cas, ans);
  }
}
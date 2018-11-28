#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cfloat>
#include <climits>
#include <cctype>
#include <cmath>
#include <cassert>
#include <ctime>
 
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <sstream>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <queue>
#include <stack>
#include <map>
#include <set>
#include <bitset>
#include <complex>
#include <limits>
#include <functional>
#include <numeric>

#define frr(a,b,c) for(int (a) = (b); (a) < (c); ++(a))
#define fr(a,b) frr(a,0,b)
#define rp fr
#define ms(a,b) memset((a), (b), sizeof(a))
#define cl ms
#define sc(a) scanf("%d", &a)
#define sc2(a,b) scanf("%d%d", &a, &b)
#define scs(s) scanf("%s", s)
#define pri(x) printf("%d\n", x)
#define db(x) cerr << #x << " == " << x << endl
#define _ << ", " <<

const int INF = 0x3f3f3f3f;
typedef long long ll;

using namespace std;

int n, cap, a[10009];

int main() {
  int t, cn = 1;
  sc(t);
  while (t--) {
    printf("Case #%d: ", cn++);
    sc2(n, cap);
    fr(x, n) sc(a[x]);
    sort(a, a+n);
    int b = 0, e = n-1, ans = 0;
    while (b < e) {
      if (a[b] + a[e] <= cap) {
        b++; e--; 
      } else e--;
      ans++;
    }
    if (b == e) ans++;
    pri(ans);
  }
  return 0;
}

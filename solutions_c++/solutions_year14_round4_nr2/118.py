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

int n, b, e, a[100009], ord[100009];

int cmp(int b, int c) {
  return a[b] < a[c];
}

void swapp(int i, int j) {
//  db(i _ j);
  swap(ord[a[i]], ord[a[j]]);
//  db(a[i] _ a[j]);
  swap(a[i], a[j]);
}

int main() {
  int t, cn = 1;
  sc(t);
  while (t--) {
    sc(n);
    fr(x, n) {
      sc(a[x]);
      ord[x] = x;
    }
    sort(ord, ord+n, cmp);
    fr(x, n) a[ord[x]] = x;
    int ans = 0;
    e = n;
    fr(x, n) {
//      fr(y, e) printf("%d ", a[y]); puts("");
//      fr(y, e) printf("%d ", ord[y]); puts("");
      int p = ord[x];
//      db(p);
      if (p <= (e-1)/2) {
//        puts("A");
        ans += p;
      } else {
//        puts("B");
        ans += e-p-1;
      }
      for(int y = p; y < e-1; y++) swapp(y, y+1);
      e--;
    }
    printf("Case #%d: ", cn++);
    pri(ans);
  }
  return 0;
}

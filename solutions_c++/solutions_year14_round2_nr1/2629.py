#include <cstdio>
#include <cmath>
#include <cstring>
#include <ctime>
#include <cstdlib>
#include <iostream>
#include <iomanip>
#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <algorithm>

using namespace std;

typedef pair<int,int> ii;
typedef long long LL;
typedef vector <int> vi;

#define INF 2000000000
#define PI 3.14159265

#define REP(i,n) for(int i=0, _n=n; i<_n; ++i)
#define FOR(i,a,n) for(int i=a,_n=n; i<=_n; ++i)
#define FOREACH(it,arr) for (__typeof((arr).begin()) it=(arr).begin(); it!=(arr).end(); it++)

#define ALL(v) (v).begin(), (v).end()

#define DEBUG(x) cout << '>' << #x << ':' << x << '\n';

int main()
{
   freopen("a.in", "r", stdin);
   freopen("a.out", "w", stdout);
	int t; scanf("%d", &t);
	int tcase = 0;

	while (t--) {
      char a[105][105];
      string s[105];
      int n; scanf("%d", &n);
      REP (i, n) scanf("%s", a[i]);
      REP (i, n) s[i] = a[i];

      if ( s[0].size() > s[1].size() ) swap(s[0], s[1]);

      int i = 0, j = 0;
      int ret = 0;
      bool can = true;
      for(;;) {
         if ( i > s[0].size() && j > s[1].size() ) break;
         char x = s[0][i];
         char y = s[1][j];
         char prevX = i > 0 ? s[0][i-1] : '?';
         char prevY = j > 0 ? s[1][j-1] : '?';

         if ( x == y ) {
            ++i, ++j;
            continue;
         }
         if ( y == prevY || prevX == y ) {
            ++j;
            ++ret;
            continue;
         }
         if ( x == prevX || prevY == x ) {
            ++i;
            ++ret;
            continue;
         }
         can = false;
         break;
      }

      printf("Case #%d: ", ++tcase);
      if ( can ) printf("%d\n", ret);
      else puts("Fegla Won");
	}
   return 0;
}

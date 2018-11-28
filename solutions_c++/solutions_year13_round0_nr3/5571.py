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

bool isPalindrome(int x) {
   char pal[5];
   sprintf(pal, "%d", x);

   for ( int i = 0, j = strlen(pal)-1; i < j; ++i, --j ) {
      if ( pal[i] != pal[j] ) return false;
   }

   return true;
}

int main() {
   freopen("c-small.in", "r", stdin);
   freopen("c-small.out", "w", stdout);
   //precompute all squares
   int arr[1001]; memset(arr, false, sizeof arr);

   FOR (i, 1, 100) {
      int s = i*i;
      if ( s > 1000 ) break;
      if ( isPalindrome(i) && isPalindrome(s) )  arr[s] = true;
   }

   int t; scanf("%d", &t);

   REP (T, t) {
      int a, b; scanf("%d %d", &a, &b);

      int cnt = 0;
      FOR (i, 1, 1000) {
         if ( arr[i] && i >= a && i <= b ) ++cnt;
      }

      printf("Case #%d: %d\n", T+1, cnt);
   }
   return 0;
}

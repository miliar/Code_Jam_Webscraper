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

double solve(double c, double f, double x, double current)
{
   double next = x / current;
   double tryBuy = (c / current) + (x / (current+f));
      
   if ( tryBuy < next ) 
      return (c / current) + solve(c, f, x, current+f);
   
   else 
      return next;   
}

int main()
{
   freopen("b.in", "r", stdin);
   freopen("b.out", "w", stdout);
   int tcase; scanf("%d", &tcase);
   
   REP (y, tcase) {
       double c, f, x;
       scanf("%lf %lf %lf", &c, &f, &x);
       
       double current = 2.0;
       double res = 0.0;
       while (true) {
             double next = x / current;
             double tryBuy = (c / current) + (x / (current+f));
             
             if ( tryBuy < next ) {
                res += (c / current);
                current += f;                
             }
             else {
                res += next;
                break;     
             }
       }
       
       printf("Case #%d: %.7lf\n", y+1, res);   
   }

   return 0;
}

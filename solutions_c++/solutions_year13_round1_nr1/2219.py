#include <algorithm>
#include <numeric>
#include <string>
#include <cstring>
#include <set>
#include <map>
#include <vector>
#include <queue>
#include <iostream>
#include <iterator>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <sstream>
#include <cassert>
#include <math.h>
#define debug(x) cerr<<#x<<" = "<<(x)<<endl;

using namespace std;
#define ALL(c) (c).begin(), (c).end()
#define SORT(c) sort(ALL(c))
#define VAR(a,b) __typeof(b) a=(b)
#define REVERSE(c) reverse(ALL(c))
#define FOREACH(it,c) for(VAR(it,(c).begin());it!=(c).end();++it)
#define MINN(X,Y) ((X) > (Y) ? (Y) : (X))
#define MAXX(X,Y) ((X) < (Y) ? (Y) : (X))
typedef pair<int, int> PII;
typedef vector<PII> VPII;
typedef vector<int> VI;
typedef vector<VI> VVI;
typedef long long LL;

#define dbv(x)   {for(int i=0;i<x.size();i++)  cerr<<x[i]; cerr<<endl;}

int a[1000], b[1000];
long double PI;
void solve()
{
  

  unsigned long long r, T;
  cin >> r>>T;
  long double sum = T;  ///PI;
  int cnt =0;
  long double s = 0;
  //cout <<"rr "<<r<<endl;
  //cout << " t "<< T << endl;
  //cout<< " PI" << PI << endl;
  //cout<<"sum "<<sum<<endl;
  double nn = (2.0 *r -1.0);
  nn = nn*nn;
  nn+= 8.0 * sum;
  nn = sqrt(nn);
  nn += (1.0-2.0 * r);
  nn /=4.0;
  int rslt = (int)(floor(nn));
  unsigned long long c= 2 * rslt * r;
  c += ( 2*rslt * rslt -rslt);
  if ( c > T )
    rslt--;
  printf("%d\n",rslt);
}

int main()
{
  PI=atan(1)*4;
  int T;
    scanf("%d", &T);
    for(int t=1; t<=T; t++)
    {
        printf("Case #%d: ", t);
        solve();
    }
  return 0;
}

#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <ctime>
#include <cctype>
#include <cfloat>
#include <climits>
#include <iostream>
#include <iomanip>
#include <fstream>
#include <algorithm>
#include <string>
#include <vector>
#include <list>
#include <stack>
#include <queue>
#include <deque>
#include <map>
#include <set>
#include <utility>
#include <sys/time.h>

#define INF 1000000007
#define EPS (1e-8)
#define pb(a) push_back(a)
#define pf(a) push_front(a)
#define mp make_pair
#define FOR(i,k) for(i=0;i<k;i++)
#define RFOR(i,k) for(i=k-1;i>=0;i--)
const long double PI = 3.1415926535897932384626433832795;
typedef long long LL;


using namespace std;


LL getReverseNum( LL n )
{
  LL revnum = 0;
  LL t = n;
  
  while( t > 0 )
    {
      LL dig = t%10;
      t = t/10;
      revnum = revnum*10 + dig;
    }
  return revnum;
}

main()
{
  vector<LL> fairsquare;
  for( LL n = 1 ; n < 10000000 ; n++ )
    {
      if( n == getReverseNum(n) )
	{
	  LL sq = n*n;
	  if( sq == getReverseNum(sq) )
	    {
	      fairsquare.pb( sq );
	    }
	}
    }
  
  int tests;
  cin >> tests;
  
  LL A,B;
  for( int tc = 1 ; tc <= tests ;tc++ )
    {
      scanf("%lld%lld",&A,&B);
      
      LL ans = 0;
      for( int i = 0 ; i < fairsquare.size() ; i++ )
	{
	  if( fairsquare[i] >= A && fairsquare[i] <= B )
	    {
	      ans++;
	    }
	}
      
      printf("Case #%d: %lld\n",tc,ans);
    }
}




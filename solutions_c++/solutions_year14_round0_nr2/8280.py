#include<vector>
#include<stack>
#include<set>
#include<list>
#include<map>
#include<queue>
#include<deque>
#include<string>
#include<iostream>
#include<algorithm>
#include<cstring>
#include<cassert>
#include<cstdlib>
#include<cstdio>
#include<cmath>
#include<iomanip>

using namespace std;

#define s(n) scanf("%d",&n)
#define sl(n) scanf("%lld",&n)
#define sf(n) scanf("%lf",&n)
#define ss(n) scanf("%s",n)
#define INF (int)1e9
#define LINF (long long)1e18
#define MAX(a,b) ((a)>(b)?(a):(b))
#define MIN(a,b) ((a)<(b)?(a):(b))
#define ABS(x) ((x)<0?(-(x)):(x))
#define FOR(i,a,b) for(int i=a;i<b;i++)
#define REP(i,n) FOR(i,0,n)
#define foreach(v,c) for( typeof((c).begin()) v = (c).begin();  v != (c).end(); ++v)

int main()
{
  int tc;s(tc);
  int tests = tc;
  setprecision(10);
  while(tc--) {
    double C; cin>>C;
    double F; cin>>F;
    double X; cin>>X;
 
    double total = X/2;
    for(int it=1;;it++)
    {
      double total_chk = 0;
      for(int cs=0;cs<it;cs++)
      {
        total_chk += C/(2+cs*F);
      }
      total_chk += X/(2+it*F);
      if(total_chk < total)
      {
        total = total_chk;
      }
      else
        break;
    } 
    
    cout<<"Case #"<<(tests-tc)<<": "<<setprecision(10)<<total<<endl;
  }
  return 0;
}


#include <bits/stdc++.h>
using namespace std;
#define TR(i,v)       for(__typeof((v).begin())i=(v).begin();i!=(v).end();++i)
#define DEBUG(x)      cout<<#x<<" = "<<x<<endl
#define SIZE(p)       (int)(p).size()
#define MP(a,b)       make_pair((a),(b))
#define ALL(p)        (p).begin(),(p).end()
#define rep(i,n)      for(int i=0;i<(int)(n);++i)
#define REP(i,a,n)    for(int i=(a);i<(int)(n); ++i)
#define FOR(i,a,b)    for(int i=(int)(a);i<=(int)(b);++i)
#define FORD(i,b,a)   for(int i=(int)(b);i>=(int)(a);--i)
#define CLR(x,y)      memset((x),(y),sizeof((x)))
typedef long long LL;
typedef pair<int,int> pii;

int main(){	
	int T;scanf("%d",&T);
	FOR(cs,1,T){
		printf("Case #%d: ",cs);
		int n,res=2000,mx=0;
		scanf("%d",&n);
		static int P[1005];
		rep(i,n)scanf("%d",P+i),mx=max(mx,P[i]);		
		FOR(lo,1,mx){			
			int r=0;
			rep(i,n)r+=(P[i]-1)/lo;
			res=min(res,r+lo);			
		}
		printf("%d\n",res);
	}
    return 0;
}
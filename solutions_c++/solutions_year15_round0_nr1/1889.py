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
#ifndef ONLINE_JUDGE
    freopen("Ain.in","r",stdin);    
#endif    
    int T;scanf("%d",&T);
    FOR(cs,1,T){
    	int n;scanf("%d",&n);
    	static char s[1005];scanf("%s",s);
    	int sum=0,r=0;
    	FOR(i,0,n){
    		int d=s[i]-'0';
    		r=max(r,i-sum);
    		sum+=d;
    	}
    	printf("Case #%d: %d\n",cs,r);
    }
    return 0;
}
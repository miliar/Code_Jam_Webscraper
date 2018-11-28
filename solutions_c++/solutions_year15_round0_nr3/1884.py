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
const int M[5][5]={
	{0,0,0,0,0},
	{0,1,2,3,4},
	{0,2,-1,4,-3},
	{0,3,-4,-1,2},
	{0,4,3,-2,-1}
};
inline int sgn(int a){return a>0?1:-1;}
inline int mul(int a,int b){
	return sgn(a)*sgn(b)*M[abs(a)][abs(b)];
}
int main(){
	int T;scanf("%d",&T);
	FOR(cs,1,T){
		printf("Case #%d: ",cs);
		static int p[10005],pr[10005];
		static char S[10005];
		int L,X;scanf("%d%d%s",&L,&X,S);
		int n=L*X;
		rep(i,n)p[i]=S[i%L]-'i'+2;
		bool ok=0;pr[n]=1;
		FORD(i,n-1,0)pr[i]=mul(p[i],pr[i+1]);
		int p1=1,p2,p3;
		rep(i,n){
			p1=mul(p1,p[i]);
			p2=1;			
			REP(j,i+1,n){
				p2=mul(p2,p[j]);
				if(j+1>=n)continue;
				p3=pr[j+1];				
				if(p1==2 && p2==3 && p3==4)ok=1;
			}
		}
		puts(ok?"YES":"NO");
	}
    return 0;
}
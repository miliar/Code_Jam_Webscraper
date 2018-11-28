#include<cstdio>
#include<algorithm>
#include<cstring>
#include<cmath>
using namespace std;
#define FOR(i,l,r) for(int i=l; i<=r; i++)
#define COR(i,r,l) for(int i=r; i>=l; i--)
#define FILL(a,b) memset(a,b,sizeof(a))
#define FLT double
#define INF 1000000000
#define N 120001
int T;
FLT c,f,x,ans,lastans,per;
int sgn(FLT a){
	if( a < -1e-10 ) return -1;
	return fabs(a) > 1e-10;
}
int main(){
	freopen("a.in","r",stdin);
	freopen("a.out","w",stdout);
	scanf("%d",&T);
	FOR(t,1,T){
		scanf("%lf%lf%lf",&c,&f,&x);
		lastans = 1e10;
		FOR(i,0,100000){
			ans = 0; per = 2.0;
			FOR(j,1,i){
				ans += c/per;
				per += f;
			}
			ans += x/per;
			if( sgn( ans - lastans ) > 0 ) break;
			lastans = ans;
		}
		printf("Case #%d: %.7lf\n",t,lastans);
	}
	
	return 0;
}


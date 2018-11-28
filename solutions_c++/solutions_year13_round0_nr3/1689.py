#include<cstdio>
#include<algorithm>
#include<cstring>
#include<vector>
#include<queue>
#include<map>
#include<set>
using namespace std;
#define INF (1<<29)
#define min(x,y) (((x)<(y))?(x):(y))
#define max(x,y) (((x)>(y))?(x):(y))
#define FOR(i,x,y) for(int i=(x);i<(y);++i)
#define FOE(i,x,y) for(int i=(x);i<=(y);++i)
#define CLR(i) memset(i,0,sizeof(i))

#define MAXN (10000000ll)
#define ll long long

ll a[1000000];
int T,n;

bool f(ll x){
	char s[20];
	sprintf(s,"%lld",x);

	int n = strlen(s);
	for (int i=0,j=n-1;i<n;++i,--j) if (s[i]!=s[j]) return 0;
	return 1;
}

int main(){
	n=0;
	for (ll i=0ll;i<MAXN;++i){
		if (f(i) && f(i*i)) a[n++] = i*i;
	}

	//printf("%d: %lld\n",n,a[n-1]);
	//FOR(i,0,10) printf("%d: %lld\n",i,a[i]);

	scanf("%d",&T);
	FOE(t,1,T){
		ll x,y; scanf("%lld%lld",&x,&y);
		int sx = lower_bound(a,a+n,x) - a;
		int sy = lower_bound(a,a+n,y) - a;

		if (sx==n) --sx;
		if (sy==n) --sy;
		if (a[sy] > y) --sy;

		//printf("%d %d\n",sx,sy);

		printf("Case #%d: %d\n",t,sy-sx+1);
	}
	return 0;
}

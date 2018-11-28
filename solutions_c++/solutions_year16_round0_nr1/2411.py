#include<iostream>
#include<cstdio>
#include<algorithm>
#include<cmath>
using namespace std;
#define LL long long
bool ok[10],bb;
LL ans;
void init()
{
	memset(ok,0,sizeof(ok));
}
bool solve(LL x)
{
	ans=x;
	while(x){
		ok[x%10]=1;
		x/=10;
	}
	for(int i=0;i<10;i++){
		if(!ok[i]) return 0;
	}
	return 1;
}
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("A-large.out","w",stdout);
	int T;
	LL n,nn;
	scanf("%d",&T);
	for(int cas=1;cas<=T;cas++){
		init();
		scanf("%lld",&n);
		nn=n;
		ans=n;
		printf("Case #%d: ",cas);
		if(n==0) puts("INSOMNIA");
		else{
			while(!solve(nn)){
				nn+=n;
			}
			printf("%lld\n",ans);
		}
	}
	return 0;
}

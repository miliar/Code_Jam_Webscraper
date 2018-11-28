#include<bits/stdc++.h>
using namespace std;
const int maxn=1e6+100;
typedef long long LL;
LL ans[maxn];
int con;
bool vis[15];
LL cal(LL v)
{
	con=10;
	for(int i=0;i<10;++i)vis[i]=0;
	int res=0;
	do
	{
		++res;
		for(LL n=v*res;n;n/=10)
			if(!vis[n%10])vis[n%10]=1,--con;
	}while(con);
	return res*v;
}
int main()
{
	ans[0]=-1;
	int n=1;
	for(;n<maxn;++n)
	{
		ans[n]=cal(n);
		//if(ans[n]>1e6)printf("%d %I64d\n",n,ans[n]);
	}
	LL v;
	int T;
	scanf("%d",&T);
	for(int cas=1;cas<=T;++cas)
	{
		scanf("%I64d",&v);
		if(v==0)printf("Case #%d: INSOMNIA\n",cas);
		else printf("Case #%d: %I64d\n",cas,ans[v]);
	}
	return 0;
}

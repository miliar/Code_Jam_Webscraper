#include<cstdio>
#include<cmath>
#include<cstdlib>
#include<iostream>
#include<cstring>
#include<algorithm>
using namespace std;
bool ok[100];
long long ans,n;
int main()
{
	//freopen("A.in","r",stdin);
	//freopen("A.out","w",stdout);
	int t;
	scanf("%d",&t);
	for(int cas=1;cas<=t;cas++)
	{
		memset(ok,0,sizeof(ok));
		scanf("%d",&n);
		if(!n){printf("Case #%d: INSOMNIA\n",cas);continue;}
		ans=0;
		for(;;)
		{
			ans+=n;
			long long x=ans;
			while(x)
			{
				ok[x%10]=true;
				x/=10;
			}
			bool flag=false;
			for(int i=0;i<=9;i++)
			{
				if(!ok[i]){flag=true;break;}
			}
			if(!flag)break;
		}
		printf("Case #%d: %lld\n",cas,ans);
	}
	return 0;
}

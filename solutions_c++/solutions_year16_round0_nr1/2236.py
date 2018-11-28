#include<cstdio>
#include<cstring>
#include<iostream>
#include<queue>
#include<vector>
#include<map>
#include<set>
#include<algorithm>
#include<string>
using namespace std;
typedef long long ll;
const int N = 1000005;
bool u[10];
int ret[N];
int main()
{
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	for(int i=1;i<N;i++)
	{
		memset(u,0,sizeof(u));
		int t=0,j;
		for(j=1;;j++)
		{
			ll x=(ll)i*j;
			while(x)
			{
				if(!u[x%10])t++,u[x%10]=true;
				x/=10;
			}
			if(t==10)break;
		}
		ret[i]=j;
	}
	int T,ca=1;
	scanf("%d",&T);
	while(T--)
	{
		int x;
		scanf("%d",&x);
		printf("Case #%d: ",ca++);
		if(!x)puts("INSOMNIA");
		else printf("%lld\n",(ll)x*ret[x]);
	}
	return 0;
}


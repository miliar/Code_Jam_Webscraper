#define N (1<<4)
#include <bits/stdc++.h>
using namespace std;

bool vis[N];
int T,n,cas,cnt;

int main()
{
	freopen("in","r",stdin);
	freopen("out","w",stdout);
	for(cin>>T;T--;)
	{
		cin>>n;
		if(n==0)
			printf("Case #%d: INSOMNIA\n",++cas);
		else
		{
			memset(vis,0,sizeof(vis)),cnt=0;
			for(int i=n;;i+=n)
			{
				for(int k=i;k;k/=10)
					if(!vis[k%10]) cnt++,vis[k%10]=1;
				if(cnt==10)
				{
					printf("Case #%d: %d\n",++cas,i);
					break;
				}
			}
		}
	}
	return 0;
}

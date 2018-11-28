#include<iostream>
#include<cstdio>
#include<cmath>
#include<cstring>

using namespace std;
int vis[20];

int main()
{
	int t,n;
	freopen("A-large.in","r",stdin);
	freopen("out.txt","w",stdout);
	scanf("%d",&t);
	int ca=0;
	while(t--)
	{
		ca++;
		scanf("%d",&n);
		printf("Case #%d: ",ca);
		if(n==0)
		{
			cout<<"INSOMNIA"<<endl;
			continue;
		}
		memset(vis,0,sizeof(vis));
		int count=0;
		long long ans;
		for(int i=1;;i++)
		{
			ans=i*n;
			long long tmp=ans;
			while(tmp)
			{
				int a=tmp%10;
				tmp=tmp/10;
				if(!vis[a])
				{
					vis[a]=1;
					count++;
				}
			}
			if(count==10)
				break;
		}
		if(count==10)
			cout<<ans<<endl;
	}
 	return 0;
}



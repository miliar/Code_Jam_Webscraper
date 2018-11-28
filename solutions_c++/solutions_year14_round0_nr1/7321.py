#include <iostream>
#include <cstdio>
#include <cstring>
using namespace std;
int a[4],b[4];
int n,m;
int main()
{
	freopen("A-small-attempt2.in.txt","r",stdin);
	freopen("out.txt","w",stdout);
	int T,kase=1;
	scanf("%d",&T);
	while(T--)
	{
		scanf("%d",&n);
		int t;
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++) 
			{
				scanf("%d",&t);
				if(i+1==n) a[j]=t;
			}
		}
		scanf("%d",&m);
		for(int i=0;i<4;i++)
		{
			for(int j=0;j<4;j++)
			{
				scanf("%d",&t);
				if(i+1==m) b[j]=t;
			}
		}
		int ans=0;
		for(int i=0;i<4;i++)
			for(int j=0;j<4;j++)
				if(a[i]==b[j]) 
				{
					ans++;t=a[i];
				}
		printf("Case #%d: ",kase++);
		if(ans==0) puts("Volunteer cheated!");
		else if(ans>1) puts("Bad magician!");
		else printf("%d\n",t);
	}
	return 0;
}

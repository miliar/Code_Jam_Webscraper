#include <cstdio>
#include <cstring>
#include <algorithm>
#include <iostream>
using namespace std;
int n,m;
int now,ans;
int main()
{
//	freopen("A.in","r",stdin);
//	freopen("A.out","w",stdout);
	
	scanf("%d",&n);
	for(int i=1;i<=n;++i)
	{
		now=ans=0;
		scanf("%d",&m);
		for(int j=0;j<=m;++j)
		{
			char t=getchar();
			while(t<'0'||t>'9')t=getchar();
			int x=t-'0';
			if(now<j)
			{
				ans+=j-now;
				now=j;
			}
			now+=x;
		}	
		printf("Case #%d: %d\n",i,ans);
	}
	return 0;
}

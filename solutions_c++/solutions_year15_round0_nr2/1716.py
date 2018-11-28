#include<cstdio>
#include<algorithm>
#include<cstring>
#include<string>
using namespace std;
int a[1001];
int main()
{
	freopen("B-large.in.txt","r",stdin);
	freopen("ans.txt","w",stdout);
	int i,j,x,t,tt=0,n,ans,mx;
	scanf("%d",&t);
	while(t--)
	{
		scanf("%d",&n);
		mx=0;
		for(i=0;i<n;i++)
		{
			scanf("%d",a+i);
			mx=max(mx,a[i]);
		}
		ans=mx;
		for(j=1;j<=mx;j++)
		{
			x=0;
			for(i=0;i<n;i++)
				x+=a[i]/j+(a[i]%j!=0)-1;
			if(x+j<ans)
				ans=x+j;
		}
		printf("Case #%d: %d\n",++tt,ans);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
/*
99
1
3
4
1 2 1 2
1
4

Case #1: 3
Case #2: 2
Case #3: 3
*/

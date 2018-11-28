#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	double ar[1005],br[1005];
	int t,tc,x,n,c,flag;
	for(scanf("%d",&tc),t=1;t<=tc;t++)
	{
		int hash[1005]={},hash1[1005]={};
		scanf("%d",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",ar+i);
		for(int i=0;i<n;i++)
			scanf("%lf",br+i);
		sort(ar,ar+n);
		sort(br,br+n);
		c=0;
		for(int i=n-1;i>=0;i--)
		{
			flag=0;
			for(int j=0;j<n;j++)
				if(!hash[j] && ar[j]>br[i])
				{
					hash[j]=1;
					flag=1;
					break;
				}
			if(flag)
				c++;
			else
			{
				for(int j=0;j<n;j++)
				{
					if(!hash[j])
					{
						hash[j]=1;
						break;
					}
				}
			}
		}
		x=0;
		for(int i=n-1;i>=0;i--)
		{
			flag=0;
			for(int j=0;j<n;j++)
			{
				if(!hash1[j] && br[j]>ar[i])
				{
					flag=1;
					hash1[j]=1;
					break;
				}
			}
			if(!flag)
			{
				x++;
				for(int j=0;j<n;j++)
				{
					if(!hash1[j])
					{
						hash1[j]=1;
						break;
					}
				}
			}
		}
		printf("Case #%d: %d %d\n",t,c,x);
	}
	return 0;
}
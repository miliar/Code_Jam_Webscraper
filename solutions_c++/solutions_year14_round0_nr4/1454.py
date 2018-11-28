#include<cstdio>
#include<cstdlib>
#include<algorithm>
using namespace std;

int main()
{
	int t,T,i,n,j;
	double N[1010],K[1010];
	scanf("%d",&T);
	for (t=1;t<=T;t++)
	{
		scanf("%d",&n);
		for (i=0;i<n;i++)
		{
			scanf("%lf",&N[i]);
		}
		sort(N,N+n);
		for (i=0;i<n;i++)
		{
			scanf("%lf",&K[i]);
		}
		sort(K,K+n);
		j=n-1;i=n-1;
		int ans1=0;
		while (i>=0 && j>=0)
		{
			//printf("%lf %lf\n",N[i],K[j]);
			if (N[i]>K[j])
			{
				i--;
				j--;
				ans1++;
			}
			else
				j--;
				
		}
		
		i=0;j=0;
		int count=0,ans2=0;
		while (i<n && j<n)
		{
			if (N[i]<K[j])
			{
				i++;
				j++;
				count++;
			}
			else
			{
				j++;
			}
		}
		ans2 = n-count;
		printf("Case #%d: %d %d\n",t,ans1,ans2);
	}
	return 0;
}
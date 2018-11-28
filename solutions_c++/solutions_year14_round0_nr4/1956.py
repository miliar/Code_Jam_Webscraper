#include <stdio.h>
#include <vector>
#include <algorithm>
using namespace std;
int main()
{
	int t,k;
	scanf("%d",&t);
	k=t;
	while(t--)
	{
		int n,i,j,k2;
		scanf("%d",&n);
		vector<double> a(n),b(n);
		for(int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a.begin(),a.end());sort(b.begin(),b.end());
		j=0;k2=0;
		for(i=0;i<n;i++)
			if(a[i]>b[j])
			{k2++;j++;}
		printf("Case #%d: %d ",k-t,k2);
		k2=0;j=0;
		for(i=0;i<n;i++)
		{
			while(j<n&&a[i]>b[j])
			{
				j++;
				k2++;
			}
			if(j==n) break;
			else j++;
		}
		printf("%d\n",k2);
	}
	return 0;
}

#include <stdio.h>
#include <algorithm>

using namespace std;

int main()
{
	freopen("d.in","r",stdin);
	freopen("d.out","w",stdout);
	int t;
	scanf("%d",&t);
	int id = 0;
	while(t--)
	{
		int n;
		double a[1005],b[1005];
		scanf("%d",&n);
		for(int i = 0;i < n;i++)
			scanf("%lf",&a[i]);
		for(int i = 0;i < n;i++)
			scanf("%lf",&b[i]);
		int r1 = 0,r2 = 0;
		sort(a,a+n);
		sort(b,b+n);
		int j = n - 1;
		for(int i = n - 1;i >= 0;i--)
		{
			if(a[j] > b[i])
			{
				r1++;
				j--;
			}
		}
		j = n - 1;
		for(int i = n - 1;i >= 0;i--)
		{
			if(b[j] > a[i])
			{
				r2++;
				j--;
			}
		}
		r2 = n - r2;
		printf("Case #%d: %d %d\n",++id,r1,r2);
	}
	return 0;
}

		

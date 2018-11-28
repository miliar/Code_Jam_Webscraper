#include <iostream>
#include <cstdio>
#include <algorithm>
using namespace std;
int T;
int n;
double a[1005],b[1005];
int main()
{
	//freopen("1.in","r",stdin);
	//freopen("1.out","w",stdout);
	scanf("%d",&T);
	int t=0;
	while(T--)
	{
		t++;
		scanf("%df",&n);
		for(int i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(int i=0;i<n;i++)
			scanf("%lf",&b[i]);
		
		sort(a,a+n);
		sort(b,b+n);
		int ans1 = 0;
		int id1=0,id2=0;
		while(id1<n && id2<n)
		{
			if(a[id1]<=b[id2])
				id1++;
			else 
			{
				ans1++;
				id1++;
				id2++;
			}
		}
		int ans2 = 0;
		id1=id2=n-1;
		while(id1>=0 && id2>=0)
		{
			if(a[id1]>=b[id2])
				id1--;
			else 
			{
				ans2++;
				id1--;
				id2--;
			}
		}

		printf("Case #%d: ",t);
		printf("%d %d\n",ans1,n-ans2);

	}
	return 0;
}

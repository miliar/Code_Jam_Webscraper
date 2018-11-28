#include <cstdio>
#include <cstdlib>
#include <algorithm>
using namespace std;
bool cmp(double a,double b)
{
	return a>b;
}
int main()
{
	freopen("out.txt","w",stdout);
	freopen("D-large.in","r",stdin);
	int t;
	scanf("%d",&t);	
	for(int T=0;T<t;T++)
	{
		int n,ans1=0,ans2=0,k;
		scanf("%d",&n);
		double a[1009],b[1009];
		for(int i=0;i<n;i++)scanf("%lf",&a[i]);
		for(int i=0;i<n;i++)scanf("%lf",&b[i]);
		sort(a,a+n,cmp);
		sort(b,b+n,cmp);
		k=0;
		ans1=0;
		for(int i=0;i<n;i++)
		{
			
			while(b[k]>a[i])
			{
				
				k++;
				if(k==n)break;
			}
			if(k==n)break;
			k++;
			ans1++;
			if(k==n)break;
		}
		k=0;
		ans2=0;
		for(int i=0;i<n;i++)
		{
			while(a[k]>b[i])
			{
				
				k++;
				if(k==n)break;
			}
			if(k==n)break;
			k++;
			ans2++;
			if(k==n)break;
		}
		printf("Case #%d: %d %d",T+1,ans1,n-ans2);
		
		printf("\n");
	}
	return 0;
}

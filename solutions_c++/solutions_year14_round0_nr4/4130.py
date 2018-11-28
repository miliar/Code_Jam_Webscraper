#include<stdio.h>
#include<algorithm>
using namespace std;

int main(){
	int t,i,j,k,n,l,count,backup,ans1,ans2,pts,pts1;
	double a[1000],b[1000];
	scanf("%d",&t);
	for(k=1;k<=t;k++)
	{
		scanf("%d",&n);
		for(i=0;i<n;i++)
			scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
			scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		
		pts=0;
		for(l=0;l<=n;l++)
		{
			backup=0;
			count=0;
			for(i=n-1;i>=l ;i--)
			{
				j=i-l;
				if(b[j]>a[i])
				{
					backup++;
				}
				if(backup>0)
				{
					count++;
					backup--;
				}
			}
			pts = max(pts,n-l-count);		
		}
		ans1=pts;

		backup=0;
		count=0;
		j=n-1;
		for(i=n-1;i>=0 && j>=0;i--)
		{
			if(b[j]>a[i])
			{
				backup++;
				j--;
			}
			if(backup>0)
			{
				count++;
				backup--;
			}
		}		
		ans2=n-count;
		printf("Case #%d: %d %d\n",k,ans1,ans2);
	}
}

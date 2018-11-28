#include<cstdio>
#include<algorithm>
using namespace std;
int main(){
	int t,n,p,i,j,m,k;
	scanf("%d",&t);
	for(p=1;p<=t;p++) {
		scanf("%d",&n);
		double a[n],b[n];
		for(i=0;i<n;i++)
		scanf("%lf",&a[i]);
		for(i=0;i<n;i++)
		scanf("%lf",&b[i]);
		sort(a,a+n);
		sort(b,b+n);
		i=0;j=0;
		m=0,k=0;
		for(;i<n && j<n;)
		{
			if(a[i]<b[j])
			{
				i++;
				j++;
				m++;
			}
			else
			{
				j++;
			}
		}
		i=0;j=0;
		for(;i<n && j<n;)
		{
			if(a[i]>b[j])
			{
				i++;
				j++;
				k++;
			}
			else
			{
				i++;
			}
		}
		printf("Case #%d: %d %d \n",p,k,n-m);
	}
return 0;
}

#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{
	int i,j,k,m,n,t,v,l;
	double a[100],b[100],c[100],d[100];
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		v=0;
		m=0;
		scanf("%d",&n);
		for(j=0;j<n;j++)
		scanf("%lf",&a[j]);
		for(j=0;j<n;j++)
		scanf("%lf",&b[j]);
		for(j=0;j<n;j++)
		{
			c[j]=a[j];
			d[j]=b[j];
		}
		sort(a,a+n);
		sort(b,b+n);
		for(j=0;j<n;j++)
		{
			for(k=0;k<n;k++)
			{
				if(c[j]<=b[k]&&b[k]!=-1.00)
				{
					b[k]=-1.00;
					break;
				}
			}
		}
		for(j=0;j<n;j++)
		{
			if(b[j]!=-1.00)
			 v++;
		}
		sort(d,d+n);k=0;
		for(j=n-1;j>=0;j--)
		{
		b[k]=d[j];
		k++;
	    }
	    k=0;
	    for(j=n-1;j>=0;j--)
	    {
	    	c[k]=a[j];
			k++;
	    }
	    k=0;
	    for(j=0;j<n;)
	    {
	    l=0;
	    while(b[l]==-1)
		{
		l++;	
		}
		if(b[l]>c[j])
		{
			b[l]=-1.00;
			n--;
		}
		else if(b[l]<=c[j])
		{
			m++;
			b[l]=-1.00;
			j++;
		}	
	    }
	    printf("Case #%d: %d %d\n",i+1,m,v);
	}
	return 0;
}

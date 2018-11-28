#include<stdio.h>
#include<algorithm>
#include<iostream>

using namespace std;
main()
{
	
	int i,j,k,t;
	float temp;
	scanf("%d",&t);
	for(i=0;i<t;i++)
	{
		int n,y=0,w=0,m;
		scanf("%d",&n);
		float a[1002]={}, b[1002]={},c[1002]={};
		for(j=1;j<=n;j++)
		scanf("%f",&a[j]);
		for(j=1;j<=n;j++)
		scanf("%f",&b[j]);
		
		sort(a+1,a+n+1);
		sort(b+1,b+n+1);

		for(j=1;j<=n;j++)
		c[j]=b[j];
		
		for(j=1;j<=n;j++)
		{
			for(k=n;k>=1;k--)
			{
			if(b[k]==0)
			continue;
			if(a[j]>b[k])
			{
				b[k]=0;
				k=0;
				w++;
				continue;
			}
			}
		}
		
		for(j=n;j>=1;j--)
		{
			for(k=n;k>=j;k--)
			{
				if(c[k]==0)
				continue;
				if(c[k]>a[j])
				{
				c[k]=0;
				y++;
				k=0;
				continue;
				}
				if(c[k]<a[j])
				{
				for(m=0;c[m]!=0;m++)
				c[m]=0;
				}
		}
	}
		printf("Case #%d: %d %d\n",i+1,w,n-y);
	
}
}

#include<iostream>
#include<stdio.h>
#include<algorithm>

using namespace std;


int main()
{
	double c1[1001],c2[1001];
	long long int t,p,n,dw,w;
	scanf("%d",&t);
	
	for(int i=1;i<=t;i++)
	{
	
		dw=0;
		w=0;	
		
		scanf("%d",&n);
		
		for(int j=0;j<n;j++)
			scanf("%lf",&c1[j]);

		for(int j=0;j<n;j++)
			scanf("%lf",&c2[j]);
			
		sort(c1,c1+n,greater<double>());
		sort(c2,c2+n,greater<double>());
		
		int j;
		int k=0;
		for(j=0;j<n;j++)
			if(c1[j]<c2[k])	
			{	
				k++;
				w++;
			}
		
		k=0;
		for(j=0;j<n;j++)
			if(c1[k]>c2[j])	
			{	
				k++;
				dw++;
			}
	
		printf("Case #%d: %d %d\n",i,dw,n-w);
			
	}
	
	
}	

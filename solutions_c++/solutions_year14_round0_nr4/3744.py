#include<iostream>
#include<stdio.h>
#include<math.h>
#include<algorithm>
#include<functional>
using namespace std;
int main()
{
	int t,tt,i,w,dw,j;
	int n;
	double arr1[1000],arr2[1000];
	
	freopen("D-large.in","r",stdin);
	freopen("siku4.txt","w",stdout);
	scanf("%d",&t);
	for(tt=0;tt<t;tt++)
	{
		w=0;
		scanf("%d",&n);
		dw=(int)n-1;
		for(i=0;i<n;i++)
		scanf("%lf",&arr1[i]);
		for(i=0;i<n;i++)
		scanf("%lf",&arr2[i]);
		sort(arr1,arr1+n);
		sort(arr2,arr2+n);
		for(j=n-1;j>=0;j--)
		{
			if(arr1[dw]>arr2[j])
			dw--;
		}
		for(j=0;j<n;j++)
		{
			if(arr1[w]<arr2[j])
			w++;
		}
		
		printf("Case #%d: %d %d\n",tt+1,(int)n-dw-1,(int)n-w);
	}
	return 0;
}

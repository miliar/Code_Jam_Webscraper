#include<stdio.h>
#include<iostream>
#include<cmath>
#include<vector>
#include<map>
#include<algorithm>

using namespace std;

double X[1005],Y[1005];

int main()
{
int i,j,t,n,k,c,d,f;
scanf("%d",&t);

for(k=1;k<=t;k++)
{
	scanf("%d",&n);
	for(i=0;i<n;i++)
	{
		scanf("%lf",&X[i]);
	}
	for(i=0;i<n;i++)
	{
		scanf("%lf",&Y[i]);
	}

	sort(X,X+n);
	sort(Y,Y+n);
	//for(i=0;i<n;i++)printf("%.3f ",arr[i]);printf("\n");
	//for(i=0;i<n;i++)printf("%.3f ",Y[i]);printf("\n");
	c=d=0;
	j=0;	

	for(i=0;i<n;i++)
	{
		while(j<n&&X[j]<Y[i])j++;
		if(j<n)c++;
		else break;
		j++;
	}
	j=0;
	for(i=0;i<n;i++)
	{
		while(j<n&&X[i]>Y[j])j++;
		if(j<n)d++;
		else break;	
		j++;
	}
	printf("Case #%d: %d %d\n",k,c,n-d);
}
return 0;
}



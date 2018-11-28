#include<stdio.h>
#include<iostream>
#include<algorithm>
using namespace std;
int main()
{
	int t,p;
	scanf("%d",&t);
	for(p=1;p<=t;p++)
	{
		int n;
		scanf("%d",&n);
		double arra[n+1],arrb[n+1];
		int i,j;
		for(i=0;i<n;i++)
		{
			scanf("%lf",&arra[i]);
		}
	    for(i=0;i<n;i++)
	    {
	    	scanf("%lf",&arrb[i]);
	    }
	    if(n==1)
	    {
	    	if(arra[0]>arrb[0])
	    	printf("Case #%d: 1 1\n",p);
	    	else 
	    	printf("Case #%d: 0 0\n",p);
	    }
	    else
	    {
	    	int dum1=0,dum2,ctr=0;
	    	sort(arra,arra+n);
	    	sort(arrb,arrb+n);
	    	double arrc[n+1];
	    	for(i=0;i<n;i++)
	    	{
	    		arrc[i]=arrb[i];
	    	}
	    	int k=0;
	    	for(i=0;i<n;i++)
	    	{
	    		int dum=0;
	    		for(j=k;j<n;j++)
	    		{
	    			if(arra[i]<arrb[j])
	    			{
	    				ctr++;
	    				dum=1;
	    				k=j+1;
	    			}
	    			if(dum)
	    			break;
	    		}
	    	}
	    	dum2=n-ctr;
	    	for(i=0,j=0;i<n;i++)
	    	{
	    		if(arra[i]>arrb[j])
	    		{
	    			j++;
	    			dum1++;
	    		}
	    	}
	    	printf("Case #%d: %d %d\n",p,dum1,dum2);
	    }
	  }
	  return 0;
}

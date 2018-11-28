#include<iostream>
#include<cstdio>
#include<algorithm>
using namespace std;
int main()
{
	int t,k=1;
	scanf("%d",&t);
	while(t--)
	{
		int n,i;
		scanf("%d",&n);
		double naomi[n+1],ken[n+1],naomi1[n+1],ken1[n+1];
		for(i=0;i<n;i++)
		scanf("%lf",&naomi[i]);
		sort(naomi,naomi+n);
 		for(i=0;i<n;i++)
		{
		scanf("%lf",&ken[i]);
		  //if(ken[i]<naomi[i])
		  //count++;
	    }
		sort(ken,ken+n);
		for(i=0;i<n;i++)
		{
		naomi1[i]=naomi[i];
		ken1[i]=ken[i];
		}
		int count1=0,count=0,j=0,t=n-1,l=n-1,m=0;
		for(i=n-1;i>=0;i--)
		{
			if(naomi[i]>ken[l] && naomi[i]!=0)
			{
				
				if(ken[m]!=0)
				{
				ken[m]=0;
				m++;
				naomi[i]=0;
			    count1++;
			    }
			}
			else if(naomi[i]<ken[l] && naomi[i]!=0)
			{
				if(ken[l]!=0)
				{
					ken[l]=0;
					l--;
					naomi[i]=0;
				}
			}
		}
		for(i=0;i<n;i++)
		{
			if(naomi1[i]>ken1[j] && naomi1[i]!=0)
			{
				if(ken1[j]!=0)
				{
				
				naomi1[i]=0;
				ken1[j]=0;
				j++;
				count++;
			    }
				
			}
			else if(naomi1[i]<ken1[j]&& naomi1[i]!=0)
			{
				  if(ken1[t]!=0)
				  {
				  	naomi1[i]=0;
				  	ken1[t]=0;
					  t--;
				  }
			}
		}
		
		printf("Case #%d: %d %d\n",k,count,count1);
		k++;
	}
return 0;	
}

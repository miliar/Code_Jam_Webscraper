#include <iostream>
#include <stdio.h>
#include <string.h>
#include <algorithm>
using namespace std;

int main()
{
    freopen("D-large.in","r",stdin);
     freopen("out.txt","w",stdout);

    int test,n,i,j,test_count=0;
    float naomi[1005],naomi2[1005];
    float ken[1005],ken2[1005];
    cin>>test;
    while(test--)
    {
    	for(i=0;i<1005;i++)
    	{
    		naomi[i]=0.0;
    		ken[i]=0.0;
    	}
    	test_count++;
    	cin>>n;
    	for(i=0;i<n;i++)
    	{
    		cin>>naomi[i];
    	    naomi2[i]=naomi[i];
    	}
    	for(i=0;i<n;i++)
    	{
    		cin>>ken[i];
            ken2[i]=ken[i];
    	}
    	sort(naomi,naomi+n);
    	sort(ken,ken+n);
    	sort(naomi2,naomi2+n);
    	sort(ken2,ken2+n);
        int index=0;
        int count=0;
    	for(i=0;i<n;i++)
    	{
    	     for(j=0;j<n;j++)
    	     {
    	     	  if(ken2[i]<naomi2[j])
    	     	  {
    	     	  	  naomi2[j]=0.0;
    	     	  	  count++;
    	     	  	  break;
    	     	  }

    	     }
    	}
    	int ans=count;
    	int war_count=0;

    	for(i=0;i<n;i++)
    	{
    		for(j=0;j<n;j++)
    		  if(ken[j]>naomi[i])
              {
              	war_count++;
              	ken[j]=0.0;
              	break;
              }
    	}
    	printf("Case #%d: %d %d\n",test_count,ans,n-war_count);
    }

    return 0;
}


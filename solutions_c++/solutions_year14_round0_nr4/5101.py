#include <iostream>
#include<algorithm>
#include <stdio.h>

using namespace std;


float arr[1000],brr[1000];

int main() 
{
	int test,n,i,a,b,l,p,q;
	
	scanf("%d",&test);
	
	for(l=1;l<=test;l++)
	{
		a=b=p=q=0;
		
		scanf("%d",&n);
	
		for(i=0;i<n;i++)
		scanf("%f",&arr[i]);
		
		for(i=0;i<n;i++)
		scanf("%f",&brr[i]);
		
		sort(arr,arr+n);
		sort(brr,brr+n);
		
		
		
		
		while(1)
		{
			if(brr[q]<arr[p])
			{
				a++;	
                p++;
                q++;
			}
			else
            p++;
			if(p==n||q==n)	
            break;
		}
		
		p=q=0;
		
		
		while(1)
		{
			if(brr[q]>arr[p])
			{
				b++;	
                p++;
                q++;
            }
			else	
            q++;
			
			if(p==n||q==n)	
            break;
		}
		
		
		printf("Case #%d: %d %d\n",l,a,n-b);
	}
		
	return 0;
}
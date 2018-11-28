#include <iostream>
#include<stdio.h>
using namespace std;

int main()
{
    long t,n,i,r,j,k;
   
	scanf("%ld",&t);
	j=0;
	while(t--)
	{     j++;
	    scanf("%ld",&n);
	    if(n==0)
	    {
	         printf("Case #%ld: INSOMNIA\n",j);
	        continue;
	    }
	     int a[11]={0},count=0;i=1;
	    while(count<10)
	    {
	       
	        r=(i++)*n;
	        while(r>0)
	        {
	           
	             k=r%10;
	            if(a[k]==0)
	            { 
	                count++;
	                a[k]=1;
	            }
	            r/=10;
	        }
	        
	    }
	    
	    r=(--i)*n;
	         printf("Case #%ld: %ld\n",j,r);
	  
	}

    return 0;
}


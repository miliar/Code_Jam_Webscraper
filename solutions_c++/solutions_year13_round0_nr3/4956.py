#include <iostream>
#include <cstdio>
#include <math.h>
using namespace std;
int main ()
{ 
     freopen ("C-small-attempt5.in", "r", stdin);
     freopen ("outCsmall.txt", "w", stdout); 
     int testCase,caseprint=1;
	 scanf ("%d", &testCase);
     while ( testCase-- )
	 {
         int a,b,d;
         float c;
		 scanf ("%d %d", &a, &b);
         int i,j=0,k,arr[40],cases=0;
         c=sqrt(a);
         if(c*c!=a)c++;
		 d=sqrt(b);
	     for(i=c;i<=d;i++)
	     { 
		    int rev=0,n;
	        n=i;
 	       	while(n>0)
	        {
		          int digit;
		          rev=rev*10;
	              digit=n%10;
		          n=n/10;
		          rev=rev+digit;
        	}
	        if(i==rev)
	        {
	         arr[j]=i;
			 j++;	
	        }
	     }
	     for(i=0;i<j;i++)
	     {  
		    int rev=0,n;
	        n=arr[i]*arr[i];
 	       	while(n>0)
	        {
		          int digit;
		          rev=rev*10;
	              digit=n%10;
		          n=n/10;
		          rev=rev+digit;
        	}
	        if(arr[i]*arr[i]==rev)
	        { 
	          cases++;	
	        }
	     }
	     printf("Case #%d: %d\n",caseprint,cases);
	     caseprint++;
    }
    return 0;
}

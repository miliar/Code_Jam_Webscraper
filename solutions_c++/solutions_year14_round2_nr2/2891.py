#include <iostream>
#include<stdio.h>
#include<cstdio>
using namespace std;
int main (void)
{
    int l=1, T;
    freopen ("B-small-attempt1.in","r",stdin);
    freopen("B2-output.txt","w",stdout);
    scanf("%d", &T);
    while(l<=T)
   {
    int count=0,A,B,K,i,j;
    scanf("%d", &A);
    scanf("%d", &B);
    scanf("%d", &K);
    for(i=0;i<A;i++)
    {
    	for(j=0;j<B;j++)
    	{
    	
			if(K>(i&j))
    		 count++;
    	}
    }
    printf("Case #%d: %d",l,count);
   printf("\n");
    l++;
    }
   
return(0);
}

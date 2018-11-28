#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<string.h>
#include<cmath>
#define MAXN 1005
using namespace std;
int a[MAXN];  
int main()
{
    int T,cases,n,i,j,x,t,ans;
	freopen("B-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	scanf("%d",&T);
	for(cases=1;cases<=T;cases++)
	{
	      scanf("%d",&n);
		  for(i=1;i<=n;i++) scanf("%d", &a[i]);  
          i=1,j=n,x,t,ans=0;
	      for (i=1,j=n;i<j;)
          {
               for(t=i,x=i;t<=j;t++)
		           if(a[t]<a[x]) x=t; 
		       if(x+x<i+j)
		       {
                    ans+=x-i;
                    for (;x>i;x--) 
	  		           swap(a[x-1],a[x]);  
	                i++;
	           }else
	           {
                    ans+=j-x;
                    for (;x<j;x++) 
			           swap(a[x],a[x+1]);  
	                j--;
               }
          }		  
	      printf("Case #%d: %d\n",cases,ans); 
	}
	return 0;
}

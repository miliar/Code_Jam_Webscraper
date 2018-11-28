#include<iostream>
#include<stdio.h>
#include<algorithm>
#include<stdlib.h>
using namespace std;

int main()
{  int t,n,i,j,k,ch=0,war=0,dwar=0;
   double na[14],ke[14];
   scanf("%d",&t);
   while(t--)
     { ++ch;
	   scanf("%d",&n);
	   war=dwar=0;
       
	   for(i=0;i<n;i++)scanf("%lf",&na[i]);
       for(i=0;i<n;i++)scanf("%lf",&ke[i]);
       
	   sort(na,na+n);
	   sort(ke,ke+n);
	   
	   i=j=0;
	   
	   while(j<n)
	     { if(ke[j]>na[i])++i;
	       else ++war;
		   ++j;	
	     }
	     
	   i=0; 
	   if(n==1){ if(na[0]>ke[0])++dwar; }
	   else
	    { int ct=0;
		  for(i=0,j=0;i<n;i++)
	          { if(na[i]>=ke[j])
	               {  ++dwar;
	               	  ++j;
	               }
	          } 
		}
	   cout<<"Case #"<<ch<<": "<<dwar<<" "<<war<<endl;	
     }  
    return 0; 
}

#include<iostream>
#include<stdio.h>
#include<algorithm>
using namespace std;
int main()
{  
    freopen ("D-large.in","r",stdin);
	freopen ("output.in","w",stdout);
   int t,n,i,j,k,w,d_w;
   double a1[1001],a2[1001];
   cin>>t;
   int chk=1;
   while(chk<=t)
   { 
	   cin>>n;
	   w=0;d_w=0;
 
	   for(i=0;i<n;i++)
	   //scanf("%lf",&a1[i]);
       cin>>a1[i];
	   for(i=0;i<n;i++)
        cin>>a2[i];
		//scanf("%lf",&a2[i]);
 
	   sort(a1,a1+n);
	   sort(a2,a2+n);
 
	   i=0;
	   j=0;
 
	while(j<n)
     {
       if(a1[i]<a2[j])
       i++;
       else
       {
          w++;
         }
	  j++;	
       }
 
	   
	    
        int x=0;
        int y=0;
		while(x<n)
          { 
          if(a1[x]>=a2[y])
          { 
		  y++; 
          d_w++;
          }
          x++;
          } 
		  
	   cout<<"Case #"<<chk<<": "<<d_w<<" "<<w<<endl;	
     chk++;
	 }  
    return 0; 
}

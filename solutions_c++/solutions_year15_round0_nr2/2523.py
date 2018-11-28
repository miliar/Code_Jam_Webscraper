#include <iostream>
#include <stdio.h>
using namespace std;

long long T,t1,k,ans,now,i,n,a[2000],sum,j,x;
string s;

main()
{
	
	 freopen ("input.txt","r",stdin);
	 freopen ("output.txt","w",stdout);
	 
	 cin>>T;
	   t1=T;
	   
	     while (T--)
	      {
               cin>>n; ans=20000000;
                
                for (i=1;i<=n;i++)
                 	 cin>>a[i];
                 
				 
				 for (i=1;i<=1000;i++)
				  {
				  	now=i;
				  	
					  for (j=1;j<=n;j++)
				  	     {
				  	     	x=a[j];
				  	     	 while (x>i) x-=i,now++;
							} 
				  	 ans=min(ans,now);
				  }
 

			   cout<<"Case #"<<t1-T<<": "<<ans<<endl;
		  }
	  
	
}

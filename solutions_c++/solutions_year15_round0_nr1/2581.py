#include <iostream>
#include <stdio.h>
using namespace std;

long long T,t1,k,ans,now,i;
string s;

main()
{
	
	 freopen ("input.txt","r",stdin);
	 freopen ("output.txt","w",stdout);
	 
	 cin>>T;
	   t1=T;
	   
	     while (T--)
	      {
	      	 cin>>k; ans=0;now=0;
	      	 cin>>s;
	      	  for (i=0;i<=k;i++)
	      	   {
	      	    ans=max(ans,i-now);
				  now+=s[i]-'0';	
			   }
			   cout<<"Case #"<<t1-T<<": "<<ans<<endl;
		  }
	  
	
}

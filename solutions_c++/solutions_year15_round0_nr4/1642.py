#include <iostream>
#include <math.h>
#include <algorithm>
#include <stdio.h>
using namespace std;


int T,t1,X,R,C;
string ans;
main()
{
	
	 freopen ("input.txt","r",stdin);
	 freopen ("output.txt","w",stdout);
	 
	 cin>>T;
	   t1=T;
	    while (T--)
          {
          	 ans="GABRIEL";
			  cin>>X>>R>>C;
             if (R>C) swap(R,C);
           if (X>=7 || (R*C)%X!=0) ans="RICHARD";
           if (X>=3 && R<=X/2) ans="RICHARD";
          	
 			   cout<<"Case #"<<t1-T<<": "<<ans<<endl;
 		  }
	  
	
}

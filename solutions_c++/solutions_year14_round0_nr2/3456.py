#include<stdio.h>
#include<iostream>
#include<stdlib.h>
#include<vector>
#include<set>
#include<math.h>
#include<map>
#include<algorithm>
#include<queue>
#include<cstring>
#include<stack>
using namespace std;
 
int main()
{
int t,co=1;
 freopen("inp.txt","r",stdin);
freopen("out2.txt","w",stdout);
  cin>>t;
  double ti=0.0;
   while(t--)
   {
   	 double C,F,X,ra=2.0;
   	 cin>>C>>F>>X;
   
   	
       double x=X/ra;
        double tot=0;
       while(1)
       {
       	 tot+=C/ra;
       	 ra=ra+F;
       	 double gg=X/ra;
       	 if(x<tot+gg)
       	 break;
       	 x=min(x,tot+gg);
       	 
       }
       	printf("Case #%d: %0.7lf\n",co,x);
   	 		co++;
   }  
  return 0;
}

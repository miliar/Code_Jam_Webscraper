#include <iostream>
#include <stdio.h>
using namespace std;


int t,t1,i;
double timme,tim,c,f,x;

main()
{

  freopen ("cookie.in","r",stdin);
  freopen ("cookie.out","w",stdout);
  

  cin>>t;
   t1=t;
    
     while (t--)
     {
       
        cin>>c>>f>>x;
        
         tim=x/2;
         
         
         for (i=1;;i++)
          {
             timme=tim;
             
             timme-=x/( 2 + f*(i-1) );            
             timme+=x/( 2 + f*i );
             timme+=c/( 2 + f*(i-1) );
             
             if (timme>tim) break;
             tim=timme;          
          }
          
          printf ("Case #%d: %.7f\n",t1-t,tim);
          
     }
  
}

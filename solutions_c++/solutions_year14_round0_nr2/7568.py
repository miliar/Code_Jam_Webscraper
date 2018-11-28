#include<iostream>
#include<stdio.h>
using namespace std;

double c,x,f,cp,ans;

int check(double cc)
{
   if((c/cc)+(f/(cc+x))<(f/cc))
   {
      return 2;
   }
   else
   {
      return 1;
   }
}

int main ()
{  
   freopen ("B-large.in", "r", stdin);
   freopen ("B-large.out", "w", stdout);
   int t;
   cin>>t;
   
   for(int k=1;k<=t;k++)
   {
       cin>>c>>x>>f;
       cp=2;
       ans=0;
       if(f>c)
       {
          while(check(cp)==2)
          {
             //cout<<ans<<endl;
             ans=ans+(c/cp);
             cp=cp+x;
             
          }
          //cout<<ans<<endl;
          ans=ans+f/cp;
       }
       else
       {
          ans=ans+(f/cp);
       }
       printf("Case #");
       printf("%d",k);
       printf(": ");
       printf("%.7f\n",ans);
   }   
   //system("pause");
   return 0;
}

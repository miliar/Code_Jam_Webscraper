#include<cstdio>
#include<iostream>
using namespace std;

int main()
   {
       double c,f,x;
       int t;
       cin>>t;
       for(int k=1;k<=t;k++)
       {
       cin>>c>>f>>x;
       double t1=0.0,t2=0.0,t3=0.0;
       double r=2.0;
       while(1)
       {
           t1=t3+x/r;
           t2=t3+(c/r)+(x/(r+f));
           if(t1-t2>0.0000001)
           {
               t3+=c/r;
               r=r+f;

           }
           else
                break;
       }
       printf("Case #%d: %.7f\n",k,t1);
   }
   return 0;
   }

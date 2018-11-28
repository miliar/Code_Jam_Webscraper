#include<iostream>
#include<stdio.h>
using namespace std;
int main()
{  

   int T;
   double C,F,X,time,rate,res; int i,j,k;
      cin>>T;
   for(i=0;i<T;i++)
   {

     cin>>C;
     cin>>F;
     cin>>X;
     res=32767;
     for(j=0;j<X+2;j++)
     {   time=0; rate=2;
     for(k=0;k<j;k++)
     {
       time=time+(C/(rate+(k*F)));
     }
     time+=(X/(rate+(j*F)));
     if(time<res)
     res=time;
     //cout<<"time: "<<time<<" rate: "<<rate<<" res: "<<res<<"\n";
     }
     printf("Case #%d: %1.7f\n",(i+1),res);
     //cout<<"Case #"<<i+1<<": "<<res<<"\n";
   }
return 0;
}

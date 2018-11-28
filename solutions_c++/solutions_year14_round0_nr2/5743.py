#include <iostream>
#include <stdio.h>
using namespace std;

int main()
{
      freopen("B-small-attempt0.in","r",stdin);
    freopen("output.out","w",stdout);
    int n,cs=1;
   double x,f,c,cnt=0,tez=0,max=0;
   double step=2;
   cin>>n;
 while(n--)
 {
     cin>>c>>f>>x;
   max+=x/2;
   tez+=c/step;
   step+=f;
   cout<<"Case #"<<cs++<<": ";
   while(true)
   {
       //cout<<max<<" "<<tez<<"\n";
       if((tez+(x/step))<max)
        max=tez+x/step,tez+=c/step;
       else
        {
            printf("%lf\n",max);
            break;
        }
   step+=f;
   }
   tez=0,step=2,max=0;
}
    return 0;
}

#include<iostream>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("out.txt","w",stdout);
    int t;
    cin>>t;
    int cas=1;
    while(t--)
    {
       double C,X,F;
       cin>>C>>F>>X;
       double time=0;
       double per=2;
       double tot=0;
       while(true)
       {
         double need1=X/per;
         double need2=C/per+X/(per+F);
         if(need1>need2)
         {
             time+=C/per;
             per+=F;
         }
         else
         {
             time+=X/per;
             break;
         }
       }
       printf("Case #%d: ",cas++);
       printf("%.7lf\n",time);
    }
    return 0;
}
                 
           

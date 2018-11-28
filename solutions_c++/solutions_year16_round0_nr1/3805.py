#include <iostream>
using namespace std;

int main()
{
   
   
   
   
   int t;
   int i;
   int temp;
   int temp1;
   int flag;
   cin>>t;
   for(i=1;i<=t;i++)
   
   {int j;
       int  n;
       int ans;
       cin>>n;
       if(n==0)
       {
           cout<<"Case #"<<i<<": INSOMNIA\n";
       }
       else
       {int oc=0;
           int count[12]={0};int mul=1;
           while(1)
           {
           temp=n*mul;
           ans=n*mul;
           while(temp>0)
           {
           temp1=temp%10;
           temp=temp/10;
           flag=0;
           count[temp1]++;
           for(j=0;j<10;j++)
           {
               if(count[j]==0)
               flag++;
           }
           if(flag==0)
           {
           cout<<"Case #"<<i<<": "<<ans<<"\n";
           oc=7;break;
           }
           }
           if(oc==7)
           break;
           mul++;
           }
       }

   }
   

   
   
    return 0;
}

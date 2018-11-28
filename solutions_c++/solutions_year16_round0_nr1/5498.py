#include<iostream>

using namespace std;

int main()
{
   freopen ("A-large.in", "r", stdin);
   freopen ("A-large.out", "w" , stdout);
   int n,t,tt,i,j,a[1<<4],c,cc,fl;
   cin>>t;
   for(tt=1;tt<=t;tt++)
   {
      cin>>n;
      //n=tt;
      if(n==0)
      {
         cout<<"Case #"<<tt<<": "<<"INSOMNIA\n";
      }
      c=0;
      for(i=0;i<=9;i++)
      {
         a[i]=0;
      }
      
      for(i=1;i<=500000;i++)
      {
         c+=n;
         cc=c;
         while(cc>0)
         {
            a[cc%10]=1;
            cc/=10;
         }
         fl=1;
         for(j=0;j<=9;j++)
         {
            //cout<<j<<" "<<a[j]<<endl;
            if(a[j]==0)
            {
               fl=0;
               break;
            }
         }
         //system("pause");
         if(fl==1)
         {
            cout<<"Case #"<<tt<<": "<<c<<endl;
            break;
         }
      }
      /*if(fl==0)
      {
         cout<<tt<<endl;
      }*/
   }
   //system("pause");
   return 0;
}

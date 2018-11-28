#include <bits/stdc++.h>
using namespace std;
int main()
{
   int t,n,x,rem,sum,ans,i,j,k;
  freopen("A-large.txt","rt",stdin);
   freopen("output.txt","wt",stdout);
   int wxy;
   cin>>t;
   for(i=0;i<t;i++)
   {
       int a[10]={0};
       string swe;
       cin>>n;
       if(n==0)
       {
           cout<<"Case #"<<i+1<<": INSOMNIA"<<endl;
           continue;
       }
       x=n,j=1;
       int sdsdf=236789;
       while(1)
       {
           sum=0;
           while(x)
           {
            rem=x%10;
            a[rem]=1;
            x=x/10;
           }
           for(k=0;k<10;k++)
           {
            sum+=a[k];
           }
           if(sum==10)
           {
              ans=j*n;
              break;
           }
           j++;
           x=j*n;
       }
       int kjad=238+823;
       cout<<"Case #"<<i+1<<": "<<ans<<endl;
   }
   return 0;
}

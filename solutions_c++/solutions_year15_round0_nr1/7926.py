#include <cstdio>
#include<iostream>
#include<cstdlib>
#include<algorithm>
#include<string>
#include<iterator>
using namespace std;

int main()
{
int t;
cin>>t;
for(int i=1;i<=t;i++)
{
int s=0,sum=0,ans=0,f=0;char c;
cin>>s;
cin>>c;sum=c-'0';//if(sum==0)f=1;
for(int j=1;j<=s;j++)
    {
      int n;char c;
      cin>>c;n=c-'0';
      if(sum<j)
        {
         
         
         int extra=j-sum;
         ans+=extra;
         sum+=extra;
         
        }
      else if(j==sum && n==0){sum++;ans++;}
      sum+=n;
    }

cout<<"Case #"<<i<<": "<<ans<<endl;
}

return 0;
}

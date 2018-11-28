#include<iostream>
#include<stdio.h>
#include<map>
#define lol long long
using namespace std;
int main()
{
  lol int i,j,k,n,sum,v,res,rem,t,tcase=0;
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  cin>>t;
  while(t--){
  tcase++;
  cin>>n;
  v=0,k=1;
  map<lol int,lol int>mp;
  if(n==0)
  {
     printf("Case #%lld: INSOMNIA\n",tcase);
     continue;
  }
  while(!(v==10))
  {
     sum=k*n;
     res=sum;
     while(sum!=0)
     {
       rem=sum%10;
       if(mp[rem]==0)
       {
          v++;
          mp[rem]=1;
       }
       sum=sum/10;
     }
     k++;
  }
  cout<<"Case #"<<tcase<<": "<<res<<endl;
  }
 return 0;
}

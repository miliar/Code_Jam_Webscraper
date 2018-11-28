#include<iostream>
#include<algorithm>
#include<vector>
#include<map>
#include<cstdio>
#include<cstring>
using namespace std;
vector<char> v;
long long i,n,a[100005],t,k,sum,occur,maxi;
string s,x;
long long findmax()
{
  maxi=-1;
  for(i=0;i<n;i++)
    if(a[i]>maxi)
      maxi=a[i];
  if(maxi==0)
    return -1;
  else
    return maxi;
}
int main()
{
  
  cin>>t;
  for(long long j=1;j<=t;j++)
  {
     cout<<"Case #"<<j<<": ";
     cin>>n;
     for(i=0;i<n;i++)
       cin>>a[i];
     while((k=findmax())!=-1)
     {
         v.clear();
         for(i=0;i<n;i++)
         {
             if(a[i]==k)
               v.push_back(i+'A'),a[i]--;
         }
         if(v.size()%2==1)
         {
             cout<<v[0]<<" ";
             for(i=1;i<v.size();i+=2)
               cout<<v[i]<<v[i+1]<<" ";
         }
         else
         {
             for(i=0;i<v.size();i+=2)
               cout<<v[i]<<v[i+1]<<" ";
         }
     }
     cout<<endl;
     
     
  }
  
} 
#include <bits/stdc++.h>
#define ll long long int
using namespace std;

int main() {
  // your code goes here
  ll temp[5000];
  ll i,t,t1,n,c,a,j;
  t1=0;
  cin>>t;
  while(t--)
  {
      t1++;
      //max=-1;
      cout<<"Case #"<<t1<<":";
      cin>>n;
      ll arr[5000];
      for(i=1;i<=5000;i++)
      arr[i]=0;
     for(i=1;i<=2*n-1;i++)
     {
         for(j=1;j<=n;j++)
         {
              cin>>a;
              arr[a]++;
         }
         
     }
     c=0;
    // cout<<arr[5]<<arr[6];
     for(i=1;i<=5000;i++)
     {
         if(arr[i]%2!=0)
         temp[c++]=i;
     }
     sort(temp,temp+c);
     for(i=0;i<c;i++)
     cout<<" "<<temp[i];
     cout<<"\n";
  }
  return 0;
}

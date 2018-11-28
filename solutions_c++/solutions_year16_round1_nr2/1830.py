#include<bits/stdc++.h>
using namespace std;
#define SIZE 26000
#define ll long long 
int main()
{
  ll A[SIZE],t;
  cin>>t;
  for (int tc=1; tc<=t; tc++)
  { 
    ll t,m,temp,n;
    vector<ll> ans;
    cin>>n;
    m=-1;
    for (int i=0; i<2*n-1; i++)
    {
      for (int k=0;k<n;k++)
         { 
          cin>>temp;
          A[temp]++;
          if(temp>m)
            {
              m = temp;
            }
          }
    }
     
    for (int i = 0;i<m+1; i++)
    {
      if(A[i]%2==1)
        ans.push_back(i);
        A[i]=0;
    }
    sort(ans.begin(),ans.end());
    cout<<"Case #"<<tc<<": ";
    for (int i=0;i<ans.size(); i++)
      {
        cout<<ans[i]<<" ";
      }
    cout<<endl;
  }
  return 0;
}
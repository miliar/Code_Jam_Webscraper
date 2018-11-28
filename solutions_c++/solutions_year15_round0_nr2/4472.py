#include <bits/stdc++.h>
using namespace std;
#define infinity (1000000007)
#define pb push_back
vector<int> cnt(10);
map<vector<int>,int> v;

int dp(vector<int> cnt,int a)
{
 
  if(a==1)
    return (cnt[1]>0?1:0);
  int o1=a;
  if(v.find(cnt)!=v.end())
    return v[cnt];
 
  int o2=infinity;
 
  vector<int> key=cnt;
 
  if(cnt[a]>0)
  {
    --cnt[a];
    for(int i=1;i<a;++i)
    {
      ++cnt[i];
      ++cnt[a-i];
      o2=min(o2,1+dp(cnt,a));
      --cnt[i];
      --cnt[a-i];
    }
    ++cnt[a];
  }
  else
    o2=dp(cnt,a-1);
 
  return v[key]=min(o1,o2);
}
int main()
{
   int t;
  cin>>t;
  for(int tt=1;tt<=t;++tt)
  {
    cout<<"Case #"<<tt<<": ";
 
    int n;
    cin>>n;
    for(int i=0;i<10;++i)
      cnt[i]=0;
    for(int i=0;i<n;++i)
    {
      int x;
      cin>>x;
      ++cnt[x];
    }
    cout<<dp(cnt,9)<<endl;
 
  }
 
 
 
 
}

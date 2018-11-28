#include <iostream>

using namespace std;

bool ii(char a)
{
  if (a=='a')
  return true;if (a=='e')
  return true;if (a=='i')
  return true;if (a=='o')
  return true;if (a=='u')
  return true;
  return false;
}

int main()
{
  int t;
  cin>>t;
  for (int i=1;i<=t;i++)
  {
    string x;
    int y;
    cin>>x>>y;
    int dp[x.size()];
    if (ii(x[0]))
    dp[0]=0;
    else dp[0]=1;
    for (int j=1;j<x.size();j++)
    {
      if (ii(x[j]))
      dp[j]=0;
      else
      dp[j]=dp[j-1]+1;
    }
    //for (int j=0;j<x.size();j++)
    //cout<<dp[j];
    long long ans=0;
    for (int j=0;j<x.size();j++)
    for (int jj=j;jj<x.size();jj++)
    {
      if (ii(x[j]))
    dp[j]=0;
    else dp[j]=1;
    if (dp[j]>=y)
    {
    ans++;
    continue;
    }
    for (int k=j+1;k<=jj;k++)
    {
      if (ii(x[k]))
      dp[k]=0;
      else
      dp[k]=dp[k-1]+1;
      if (dp[k]>=y)
      {
      //cout<<j<<' '<<jj<<endl;
        ans++;
        break;
      }
    }
    
    }
    //if (x.size()==1&&!ii(x[0]))
    //ans=1;
    cout<<"Case #"<<i<<": ";cout<<ans<<endl;
  }
  return 0;
}

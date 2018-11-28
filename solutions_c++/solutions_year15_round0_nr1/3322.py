#include <bits/stdc++.h>
using namespace std;

int main()
{
  freopen("input.txt","r",stdin);
  freopen("output.txt","w",stdout);
  int t;
  cin>>t;
  for(int i = 1; i <= t; i++)
  {
    int n,ans = 0,sum = 0;
    string s;
    cin>>n;
    cin>>s;
    for(int j = 1; j <= n; j++)
    {
      sum += s[j - 1] - '0';
      if(s[j] != '0')
      {
        if(sum < j)
          ans = max(ans,j - sum);
      }
    }

    cout<<"Case #"<<i<<": "<<ans<<endl;
  }
  return 0;
}  
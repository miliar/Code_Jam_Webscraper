#include<bits/stdc++.h>
using namespace std;
int main()
{
  int tc,k=0;
  cin>>tc;
  while(tc--) {
    char s[1001];int sm;
    cin>>sm;
    cin>>s;
    int i,sum=0,ans=0;
    sum=s[0]-'0';
    for(i=1;i<=sm;i++)
    {
      if(sum<i)
      { ans++; sum+=(s[i]-'0'+1); }
      else
      sum+=(s[i]-'0');
    }
    cout<<"Case #"<<++k<<": "<<ans<<endl;
  }
  return 0;
}
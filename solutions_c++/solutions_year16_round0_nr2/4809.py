#include<bits/stdc++.h>
using namespace std;
#define ll long long

int main()
{
  ll i,j,k,m,n,t;
  scanf("%lld",&t);
  for(i=1;i<=t;i++)
  {
    string s;
    cin>>s;
    ll cnt=0;
    ll flag=0;
    ll f1=0,f2=0;
    for(j=1;j<s.size();j++)
    {
      if(s[j]=='-' && s[j-1]=='+')
        cnt++;
    }
    if(s.size()==1)
    {
        if(s[0]=='-')
         cnt++;
        printf("Case #%lld: %lld\n",i,cnt);
        continue;
    }
    for(j=0;j<s.size();j++)
    {
      if(s[j]=='-')
      {
        if(flag==0)
        {
          cnt++;
          flag=1;
        }
      }
      else if(s[j]=='+')
      {
        flag=0;
      }

    }

    printf("Case #%lld: %lld\n",i,cnt);
  }
  return 0;
}

#include<bits/stdc++.h>
using namespace std;
int main()
{
  freopen("B-large.in","r",stdin);
  freopen("kn","w",stdout);
  int t,i,j;
  string s;
  cin>>t;
  for(i=1;i<=t;i++)
  {
    getchar();
    cin>>s;
    int plus[s.size()];
    int minus[s.size()];
    if(s[0]=='+')
    {
      plus[0]=0;
      minus[0]=1;
    }
    else
    {
      plus[0]=1;
      minus[0]=0;
    }
    for(j=1;j<s.size();j++)
    {
      if(s[j]=='+')
      {
        plus[j]=plus[j-1];
        minus[j]=plus[j-1]+1;
      }
      else
      {
        plus[j]=minus[j-1]+1;
        minus[j]=minus[j-1];
      }
    }
    printf("Case #%d: %d\n",i,plus[s.size()-1]);
  }
  return 0;
}

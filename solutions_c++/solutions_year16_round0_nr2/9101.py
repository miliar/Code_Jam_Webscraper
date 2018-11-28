#include<bits/stdc++.h>
using namespace std;
int main()
{
    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);
    int t,k,f=0;
    cin>>t;
    for(int j=1;j<=t;++j)
    { string s;
      cin>>s;
      int c=0;
      int l=s.length();
      int i=0;
      for(int j=1;j<l;++j)
      {
        if(i<l-1)
        {
             if(s[i]!=s[j])
              {
                 for(int a=i;a>=0;a--)
                 s[a]=s[j];
                 c++;
              }
              i++;
        }
      }
        if(s[l-1]=='-')
            c++;

      cout<<"Case #"<<j<<":"<<" "<<c<<'\n';
      }
      return 0;
}


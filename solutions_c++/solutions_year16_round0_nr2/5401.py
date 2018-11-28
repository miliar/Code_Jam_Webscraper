#include <bits/stdc++.h>

using namespace std;

int t,i,ans;
string s;

int main()
 {
  freopen("in.in","r",stdin);
  freopen("2.out","w",stdout);
  cin>>t;
  for (int tt=1;tt<=t;tt++)
   {
    cout<<"Case #"<<tt<<": ";

    cin>>s;
    s+="+"; ans=0;
    for (i=1;i<s.size();i++)
     if (s[i] != s[i-1]) ans++;
    cout<<ans<<endl;
   }
 }

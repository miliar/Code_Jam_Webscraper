#include <bits/stdc++.h>

using namespace std;

int f[2000];
int tt,i,ind,t,ii,j;
string s,q,sec;

int main()
 {
  freopen("1.in","r",stdin);
  freopen("1.out","w",stdout);
  cin>>t;
  for (tt=1;tt<=t;tt++)
   {
    q="";
    sec="";
    cin>>s;
    for (i=0;i<s.size();i++)
     f[i]=0;
    q+=s[0];
    f[0]=1;
    ind=s.size()-1;
    for (j=1;j<s.size();j++)
     {
      int ans=-1,ii=-1;
      for (int x=ind;x>=0;x--)
       if (!f[x] && s[x] > ans)
       {
        ans=s[x];
        ii=x;
       }
      if (ans == -1) break;
      if (ans < s[0]) break;
      sec+=s[ii];
      f[ii]=1;
      ind=ii;
     }
    for (j=1;j<s.size();j++)
     if (!f[j]) q+=s[j];
    cout<<"Case #"<<tt<<": "<<sec<<q<<endl;
   }
 }

#include <bits/stdc++.h>

using namespace std;

int t;
int n,j,i,f[10];

int main()
 {
  freopen("in.in","r",stdin);
  freopen("1.out","w",stdout);
  cin>>t;
  for (int tt=1;tt<=t;tt++)
   {
    cout<<"Case #"<<tt<<": ";

    cin>>n;
    for (i=0;i<10;i++)
      f[i]=0;

    for (j=n;j<n*100;j+=n)
     {
      i=j;
      while (i)
       {
        f[i%10]=1;
        i/=10;
       }
      bool is=1;
      for (i=0;i<10;i++)
       if (!f[i]) is=0;
      if (is){cout<<j<<endl;break;}
     }
    if (j == 100*n) cout<<"INSOMNIA"<<endl;
   }
 }

#include <bits/stdc++.h>

using namespace std;

bool fiy[5],fix[5];
int n,b[5][5];
bool good;

void solve(int now)
 {
  if (now == n) return;
  for (int i=0;i<n;i++)
   if (!fix[i])
    {
     bool cn=1;
     for (int j=0;j<n;j++)
      if (!fiy[j] && b[i][j])
       {
        fiy[j]=1;
        fix[i]=1;
        solve(now+1);
        fiy[j]=0;
        fix[i]=0;
        cn=0;
       }

     if (cn)good=0;
    }
 }

int t1,t,res,all,i,j,f;
char a[5][5];

int main()
 {
  freopen("D.in","r",stdin);
  freopen("D.out","w",stdout);
  cin>>t1;
  for (t=1;t<=t1;t++)
   {
    cout<<"Case #"<<t<<": ";
    cin>>n;
    for (i=0;i<n;i++)
     for (j=0;j<n;j++)
      cin>>a[i][j],a[i][j]-='0';
    res=(n*n)+2;
    for (j=0;j<(1<<(n*n));j++)
     {
      f=1;
      all=0;
      for (i=0;i<n*n;i++)
       {
        if (a[i/n][i%n] && !((1<<i)&j)) { f=0; break; }
        if (!((1<<i)&j)) { b[i/n][i%n]=0; continue; }
        if (a[i/n][i%n]) all--;
        all++;
        b[i/n][i%n]=1;
       }
      if (!f) continue;

      good=1;
      solve(0);

      if (good) res=min(res,all);
     }

    cout<<res<<endl;
   }
 }

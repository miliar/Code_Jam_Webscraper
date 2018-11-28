#include <bits/stdc++.h>
using namespace std;

typedef long double ld;

int k,n;
ld p[220];
ld pr[220][220];

int main() {
  int t; cin>>t; for(int zz=1;zz<=t;zz++) {
    cin>>n>>k;
    for(int i=0;i<n;i++) cin>>p[i];
    sort(p,p+n);

    ld ans=0;

    for(int u=0;u<=k;u++) {
      for(int i=0;i<n+2;i++) pr[0][i]=0;
      pr[0][0]=1;
      for(int i=0;i<u;i++) {
        for(int j=0;j<n+2;j++) {
          pr[i+1][j+1]=pr[i][j]*p[i]+pr[i][j+1]*(1-p[i]);
        }
        pr[i+1][0]=pr[i][0]*(1-p[i]);
      }
      for(int i=u;i<k;i++) {
        int ii=n-(i-u)-1;
        for(int j=0;j<n+2;j++) {
          pr[i+1][j+1]=pr[i][j]*p[ii]+pr[i][j+1]*(1-p[ii]);
        }
        pr[i+1][0]=pr[i][0]*(1-p[ii]);
      }
      ans=max(ans,pr[k][k/2]);

      /*
      cout<<u<<endl;
      for(int i=0;i<=k+1;i++) {
        //for(int j=0;j<n+2;j++) cout<<pr[i][j]<<" ";
        cout<<endl;
      } cout<<endl;
      */
    }

    printf("Case #%d: ",zz), cout<<fixed<<setprecision(8)<<ans<<endl;
  }
}

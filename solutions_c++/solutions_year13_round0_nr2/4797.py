#include <iostream>
#include <cstdio>
#include <string>
using namespace std;
int a[105][105];
int n,m;
int h[105],l[105];
int main()
{
    freopen("B-small-attempt0.in","r",stdin);
    freopen("B-small-attempt0.out","w",stdout);
    int T;int ca=1;
    scanf("%d",&T);
    while(T--){
      scanf("%d%d",&n,&m);
      for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
          scanf("%d",&a[i][j]);
        }
      }
      for (int i=0;i<n;i++){
         h[i]=a[i][0];
         for (int j=1;j<m;j++){
           if(h[i]<a[i][j]) h[i]=a[i][j];
         }
      }
      for (int i=0;i<m;i++){
         l[i]=a[0][i];
         for (int j=1;j<n;j++){
           if(l[i]<a[j][i]) l[i]=a[j][i];
         }
      }
      bool got=true;
      for (int i=0;i<n;i++){
        for (int j=0;j<m;j++){
           if(a[i][j]<h[i]&&a[i][j]<l[j]) {
             got=false;
             break;
           }
        }
        if(!got) break;
      }
      if (!got) cout<<"Case #"<<ca++<<": "<<"NO\n";
      else cout <<"Case #"<<ca++<<": "<<"YES\n";
    }
    return 0;
}

#include<cstdio>
#include<cstring>
#include<algorithm>
#define N 1002
using namespace std;
double a[N],b[N];
bool v[N];
int g[N];
int tt,t,n,y,z;

int main(){
  int i,j,s;
  freopen("1.txt","r",stdin);
  freopen("2.txt","w",stdout);
  scanf("%d",&t);
  for (tt=1;tt<=t;++tt){
    scanf("%d",&n);
    for (i=0;i<n;++i) scanf("%lf",&a[i]);
    for (i=0;i<n;++i) scanf("%lf",&b[i]);
    sort(a,a+n);
    sort(b,b+n);
    y=z=0;
    memset(v,0,sizeof(v));
    for (i=0;i<n;++i){
      for (j=lower_bound(b,b+n,a[i])-b;j<n;++j)
        if (!v[j]) break;
      if (j>=n){
        z=n-i;
        break;
      }
      else v[j]=1;
    }
    s=n-(lower_bound(a,a+n,b[0])-a);
    if (s){
      y=1;
      for (i=1;i<n;++i){
        --s;
        if (s<=0) break;
        j=n-(lower_bound(a,a+n,b[i])-a);
        if (j>=s) ++y;
        else {
          s=j;
          if (s) ++y;
        }
      }
    }
    y=max(y,z);
    printf("Case #%d: %d %d\n",tt,y,z);
  }
  return 0;
}
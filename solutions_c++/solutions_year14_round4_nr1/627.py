#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef long long ll;
#define N 10002
int a[N];
bool v[N];
int n,m;

void solve(){
  int i,j,k;
  scanf("%d%d",&n,&m);
  for (i=0;i<n;++i) scanf("%d",&a[i]);
  sort(a,a+n);
  memset(v,0,sizeof(v));
  int ans=0;
  for (i=0;i<n;++i)
    if (!v[i]){
      v[i]=1;
      ++ans;
      for (j=min(n-1,upper_bound(a,a+n,m-a[i])-a);j>i;--j)
        if (!v[j] && a[i]+a[j]<=m){
          v[j]=1;
          break;
        }
    }
  printf("%d\n",ans);
}

int main(){
  int t,tt;
  freopen("1.txt","r",stdin);
  freopen("3.txt","w",stdout);
  scanf("%d",&t);
  for (tt=1;tt<=t;++tt){
    printf("Case #%d: ",tt);
    solve();
  }
  return 0;
}
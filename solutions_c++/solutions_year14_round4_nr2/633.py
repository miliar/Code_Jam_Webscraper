#include<cstdio>
#include<cstring>
#include<algorithm>
using namespace std;
typedef pair<int,int> pii;
typedef long long ll;
#define N 1002
pii h[N];
int a[N];
int n,m,s;
ll ans;

void solve(){
  int i,j,k,l,r;
  scanf("%d",&n);
  for (i=0;i<n;++i){
    scanf("%d",&a[i]);
    h[i]=pii(a[i],i);
  }
  sort(h,h+n);
  for (i=0;i<n;++i) a[h[i].second]=i;
  l=r=0;
  ans=0;
  for (i=0;i<n;++i){
    for (j=0;j<n;++j)
      if (a[j]==i) k=j;
    if (k-l<=n-r-1-k){
      while (k!=l){
        swap(a[k],a[k-1]);
        --k;
        ++ans;
      }
      ++l;
    }
    else {
      while (k!=n-r-1){
        swap(a[k],a[k+1]);
        ++k;
        ++ans;
      }
      ++r;
    }
  }
  printf("%lld\n",ans);
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
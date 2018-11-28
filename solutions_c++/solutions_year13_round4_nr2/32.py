#include <cstdio>
using namespace std;
int t,tt,n;
long long m,x;
long long guar(long long n, long long m) {
  if (n==2) return m-1LL;
  long long z=n/2;
  if (m<=z) return 0LL;
  return 2*guar(z,m-z)+2LL;
}
long long can(long long n, long long m) {
  if (n==2) return m-1;
  long long z=n/2;
  if (m<z) return 2LL*can(z,m);
  return n-2LL;
}
int main() {
  freopen("Bl.in","r",stdin);
  freopen("Bl.out","w",stdout);
  scanf("%d",&tt);
  for (t=1; t<=tt; t++) {
    scanf("%d%I64d",&n,&m);
	x=1LL<<n;
    printf("Case #%d: %I64d %I64d\n",t,x==m?(m-1LL):guar(x,m),x==m?(m-1LL):can(x,m));
  }
  return 0;
}

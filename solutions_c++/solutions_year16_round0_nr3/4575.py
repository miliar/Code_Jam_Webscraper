#include<cstdio>
#include<cmath>
typedef unsigned long long ull;
typedef long long ll;
int num[40];
int n,m,t;
ll bs[11],ans[11];
bool isp(ll a) {
  ll x=(ll)sqrt((double)a);
  for(ll i=2;i<=x;i++)
    if(a%i==0) return false;
  return true;
}
ll base(int a) {
  ll x=1,sum=0;
  for(int i=0;i<n;i++,x*=(ll)a) {
    sum+=(ll)num[i]*x;
  }
  bs[a]=sum;
  return sum;
}
bool fun() {
  for(int i=2;i<=10;i++)
    if(isp(base(i))) return false;
  for(int i=2;i<=10;i++) {
    for(ll j=2;j<bs[i];j++) {
      if(bs[i]%j==0) {
        ans[i]=j;
        break;
      }
    }
  }
  return true;
}
int main () {
  scanf("%d %d %d",&t,&n,&m);
  //t=1;n=16;m=50;
  ll in=1<<(n-1);
  printf("Case #%d:\n",t);
  for(int i=0;i<m;in++) {
    if(in%2==0) continue;
    ll x=in;
    for(int j=0;j<n;j++,x/=2) num[j]=x%2;
    if(fun()) {
      //printf("%lld ",in);
      for(int j=n-1;j>=0;j--) printf("%d",num[j]);
      for(int j=2;j<=10;j++) printf(" %lld ",ans[j]);
      //for(int j=2;j<=10;j++) printf("(%lld %lld)",bs[j],ans[j]);
      printf("\n");
      i++;
    }
  }
  return 0;
}

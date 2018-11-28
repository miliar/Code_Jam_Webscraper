#include <cstdio>
#define eps 1e-10
double c,f,x;
int sgn(double x) {
  return x<-eps?-1:x>eps;
}
bool ck(double t) {
  double cost=0;
  double cur=2;
  while(1){
    double tmp=cost+x/cur;
    if(sgn(tmp-t)<=0) return true;
    cost+=c/cur;
    cur+=f;
    if(sgn(cost-t)>0) return false;
  }
  return false;
}
int main()
{
  int T,ca=0;
  freopen("B.in","r",stdin);
  freopen("B.out","w",stdout);
  scanf("%d",&T);
  while(T--){
    scanf("%lf%lf%lf",&c,&f,&x);
    double l=0,h=x/2,mid;
    for(int i=0;i<200;i++){
      mid=(l+h)/2;
      if(ck(mid)) {
        h=mid;
      } else {
        l=mid;
      }
    }
    printf("Case #%d: %.7f\n",++ca,mid);
  }
}





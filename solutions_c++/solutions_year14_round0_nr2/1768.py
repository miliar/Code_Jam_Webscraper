#include<cstdio>
#include<algorithm>
using namespace std;

int main () {
  int tt;
  scanf("%d",&tt);
  for (int pp=1;pp<=tt;pp++) {
    double c,f,x;
    double ret = 1e10;
    scanf("%lf %lf %lf",&c,&f,&x);
    double sum = 0;
    double prod = 2;
    for (int i=0;i<1000000;i++){
      double t = sum + x/prod;
      ret = min(ret, t);
      //      printf("%lf\n",t);
      sum += c/prod;
      prod = prod+f;
    }
    printf("Case #%d: %.7lf\n",pp,ret);
  }
  return 0;
}

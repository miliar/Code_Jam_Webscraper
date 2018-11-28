#include<cstdio>
#include<algorithm>
using namespace std;
int n;
double v,t;
double f[255][2];
double solve(){
  if (n==1){
    f[1][1]=f[0][1];
    f[1][0]=0;
  }

  if (f[0][1]==f[1][1]){
    if(f[0][1]!=t){
      return -1;
    }
    return v / (f[0][0]+f[1][0]);
  }
  else{
    double a,b;
    a = (t*v - v*f[1][1])/(f[0][1]-f[1][1]);
    b = (t*v - v*f[0][1])/(f[1][1]-f[0][1]);
    if(a<0 || b < 0)return -1;
    return max(a/f[0][0],b/f[1][0]);
  }
}
int main () {
  int tt;
  scanf("%d",&tt);
  for(int rr=1;rr<=tt;rr++) {
    scanf("%d %lf %lf",&n,&v,&t);
    for(int i=0;i<n;i++){
      scanf("%lf %lf",&f[i][0],&f[i][1]);
    }
    
    double ret = solve();
    if (ret<0){
      printf("Case #%d: IMPOSSIBLE\n",rr);
    }
    else {
      printf("Case #%d: %.9lf\n",rr,ret);
    }
  }
  return 0;
}

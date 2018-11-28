#include <bits/stdc++.h>
using namespace std;
typedef long long LL;
typedef pair<int, int> PII;
typedef double flt;
const int MAXN = 1000 + 10;
flt R[MAXN], C[MAXN];
flt V, X;
int n;

const flt eps = 1e-8;
int sgn(flt x) {
  if (x < -eps) return -1;
  else return x > eps;
}

int main() {
  int T; scanf("%d", &T);
  for (int cas = 1; cas <= T; ++ cas) {
    printf("Case #%d: ", cas);
    scanf("%d%lf%lf", &n, &V, &X);
    for (int i = 0; i < n; ++ i) {
      scanf("%lf%lf", R + i, C + i);
    }
    if (n == 1) {
      if (sgn(C[0] - X) == 0) {
        printf("%.12f\n", V / R[0]);
      }
      else puts("IMPOSSIBLE");
    }
    else {
      if (sgn(C[0] - C[1]) == 0) {
        if (sgn(C[0] - X) == 0) printf("%.12f\n", V / (R[0] + R[1]));
        else puts("IMPOSSIBLE");
      }
      else {
        flt a=C[0]/V,b=C[1]/V;
        flt v1=(X-b*V)/(a-b);
        flt v2=V-v1;
        if(sgn(v1)<0 || sgn(v2)<0){
          puts("IMPOSSIBLE");
          continue;
        }
        flt rr=max(v1/R[0],v2/R[1]);
        if(sgn(C[0]-X) == 0) rr=min(rr,V/R[0]);
        if(sgn(C[1]-X) == 0) rr=min(rr,V/R[1]);
        printf("%.12f\n",rr);
      }
    }
  }
  return 0;
}
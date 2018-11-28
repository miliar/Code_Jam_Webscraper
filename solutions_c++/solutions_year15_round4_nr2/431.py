#include <bits/stdc++.h>
using namespace std;

double V,X,r[105],c[105],t[105];

const double eps = 1e-6;

bool is_equal(double x, double y){
    if(-eps<=x-y && x-y<=eps) return true;
    if((-eps<=x && x<=eps)
    || (-eps<=y && y<=eps)) return false;
    return (-eps<=(x-y)/x && (x-y)/x<=eps)
        || (-eps<=(x-y)/y && (x-y)/y<=eps);
}

void solve1(){
    if(X!=c[1]){
        puts("IMPOSSIBLE");
        return;
    }
    t[1] = V / r[1];
    printf("%.15f\n",t[1]);
}

void solve2(){
    if((c[1]>X && c[2]>X)
    || (c[1]<X && c[2]<X)){
        puts("IMPOSSIBLE");
        return;
    }
    t[1] = V * (X - c[2]) / (r[1] * (c[1] - c[2]));
    t[2] = V * (X - c[1]) / (r[2] * (c[2] - c[1]));
    printf("%.15f\n", max(t[1], t[2]));
}
/*
*/
// volume = t1 * r1 + t2 * r2 = V
// heat = t1 * r1 * c1 + t2 * r2 * c2 = V * X


int main(){
    int cs,n;
    scanf("%d",&cs);
    for(int no=1;no<=cs;no++){
        scanf("%d%lf%lf",&n,&V,&X);
        //printf("%d %f %f\n",n,V,X);
        for(int i=1;i<=n;i++) {
            scanf("%lf%lf",&r[i],&c[i]);
            for(int j=1;j<i;j++){
                if(c[i]==c[j]){
                    r[j]+=r[i];
                    n--;
                    break;
                }
            }
        }
        printf("Case #%d: ",no);
        if(n==1) solve1();
        if(n==2) solve2();
    }
}

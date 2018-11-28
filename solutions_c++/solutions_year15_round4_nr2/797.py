#include<iostream>
#include<stdio.h>
#include<vector>
#include<algorithm>
#define eps -0.000000001
using namespace std;
int T,N;
double t[110],r[110],c[110], V, X;

int main() {
    freopen("input.in","r",stdin);
    freopen("out2.out","w",stdout);
    scanf("%d",&T);
    for(int tt=1;tt<=T;++tt) {
        double rez = 0;
        bool ok = 1;
        scanf("%d%lf%lf",&N,&V,&X);
        for(int i=1;i<=N;++i) {
            scanf("%lf%lf",&r[i],&c[i]);
        } 
        if(N==1) {
            rez = V / r[1];
            if(c[1] != X) {
                ok = 0;
            }
        } 

        if(N==2) {
            if(c[1] == c[2]) {
                if(c[2] == X) {
                    rez = V / (r[1] + r[2]);
                } else {
                    ok = 0;
                }
            } else if(c[1] == X) {
                rez = V / r[1];
            } else if(c[2] == X) {
                rez = V / r[2];
            } else if(c[1]<X && c[2] < X) {
                ok = 0;
            } else if (c[1]>X && c[2] > X) {
                ok = 0;        
            } else {
                double t1 = (X*V - V*c[2])/ (r[1]*c[1]-r[1]*c[2]);
                if(t1 < eps) {
                    ok = 0;
                }
                double t2 = (V - t1*r[1])/r[2];
                if(t2 < eps) {
                    ok= 0;
                }
                rez = max(t1,t2);
            }
        }

        printf("Case #%d: ",tt);
        if(ok) {
            printf("%.10lf\n",rez);
        } else {
            printf("IMPOSSIBLE\n");
        }
    }
    return 0;
}

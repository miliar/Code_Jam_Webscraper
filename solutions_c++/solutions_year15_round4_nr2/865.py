#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <cmath>
using namespace std;
const int maxn  = 111 ;
const double eps = 1e-10 ;

double R[maxn] , C[maxn], p[maxn] ;
double V , X ;
int N ;
bool check(double t) {
    double sum = 0;
    for(int i=1; i<=N; i++) {
        p[i] = min(R[i] * t / V , 1.0);
        sum += p[i] * C[i] ;
    }
    return sum - X > -eps ;
}

int main()
{
    freopen("B-small-attempt2.in", "r" ,stdin) ;
    freopen("out.txt", "w", stdout) ;

    int T , cas = 1 ;
    scanf("%d", &T) ;
    while(T--) {
        scanf("%d%lf%lf", &N, &V, &X) ;
        double maR = 0 , miR = 1e20 ;
        for(int i=1; i<=N; i++) {
            scanf("%lf%lf", &R[i] , &C[i]) ;
            maR = max(maR , R[i]) ;
            miR = min(miR , R[i]) ;
        }

        printf("Case #%d: " , cas++) ;
        if(N == 1) {
            if(fabs(C[1] - X) > eps) puts("IMPOSSIBLE");
            else printf("%.9f\n" , V / R[1]);
            continue ;
        }
        if(N == 2){
            if(fabs(C[1] - C[2]) < eps) {
                if(fabs(C[1] - X) > eps) puts("IMPOSSIBLE");
                else printf("%.9f\n" , V / (R[1] + R[2]));
            }
            else {
                double v2 = V * (X - C[1]) / (C[2] - C[1]) ;
                double v1 = V - v2 ;
                if(v1<-eps || v2<-eps) puts("IMPOSSIBLE");
                else printf("%.9f\n" , max(v1/R[1] , v2/R[2]));
            }
            continue ;
        }


        double L = 0 , R = V / miR + 10 ;

        if(!check(R)) puts("IMPOSSIBLE");
        else {
            while(R - L > eps) {
                double mid = (R+L)/2 ;
                if(check(mid)) R = mid ;
                else L = mid ;
            }
            printf("%.9f\n" , (L+R)/2) ;
        }

    }
    return 0;
}

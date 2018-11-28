
#include <cstdio>

void swapv(double& d1, double& d2){
    double tmp = d1 ;
    d1 = d2 ;
    d2 = tmp ; 
}

double maxv(double d1, double d2){
    return d1 > d2 ? d1 : d2 ; 
}

int main()
{
    int T ;
    scanf("%d", &T) ; 
    for(int time = 1 ; time <= T ; time++){
        printf("Case #%d: ", time) ; 
        int N ;
        double V, X ; 
        scanf("%d%lf%lf", &N, &V, &X) ; 
        if(N == 1){
            double R, C ; 
            scanf("%lf%lf", &R, &C) ;
            if(C != X){
                puts("IMPOSSIBLE") ; 
            }
            else{
                printf("%lf\n", V/R) ; 
            }
        }
        else{
            double R1, C1, R2, C2 ; 
            scanf("%lf%lf%lf%lf", &R1, &C1, &R2, &C2) ; 
            if(C1 > C2){
                swapv(R1, R2) ;
                swapv(C1, C2) ; 
            }
            // now C1 < C2
            if(X < C1 || X > C2){
                puts("IMPOSSIBLE") ; 
            }
            else if(X == C1 && X == C2){
                printf("%lf\n", V/(R1+R2)) ; 
            }
            else if(X == C1){
                printf("%lf\n", V/R1) ;
            }
            else if(X == C2){
                printf("%lf\n", V/R2) ; 
            }
            else{
                double rt = (X-C2)/(C1-X) ; 
                double k = V/(rt+1.) ; 
                printf("%lf\n", maxv(k*rt/R1, k*1./R2)) ; 
            }
        }
    }

    return 0 ; 
}

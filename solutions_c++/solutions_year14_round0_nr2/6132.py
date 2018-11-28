
#include <cstdio>

double C, F, X ;

double calc(int a){
    double now = 0. ;
    for(int i = 0 ; i != a ; i++)
        now += C/(2.+i*F) ;
    now += X/(2.+a*F) ;
    return now ;
}

int main()
{
    int T ;
    scanf("%d", &T) ;
    for(int time = 1 ; time <= T ;  time++){
        printf("Case #%d: ", time) ;
        scanf("%lf%lf%lf", &C, &F, &X) ;
        double ans = X/2. ;
        int lf = 1, rt = 100000 ;
        while(rt-lf > 20){
            int m1 = lf+(rt-lf)/3 ;
            int m2 = lf+(rt-lf)*2/3 ;
            //printf("m1 = %d, m2 = %d\n", m1, m2) ;
            double a1 = calc(m1) ;
            double a2 = calc(m2) ;
            if(a1 < a2)
                rt = m2 ;
            else
                lf = m1 ;
        }
        for(int i = lf-1 ; i <= rt+1 ; i++){
            double now = calc(i) ;
            if(ans > now)
                ans = now ;
        }
        printf("%.10lf\n", ans) ;
    }
}

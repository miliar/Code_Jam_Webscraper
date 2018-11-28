#include <cstdio>
#include <cstdlib>

int main (){
    int t;
    double f, c, x;
    scanf("%d", &t);
    FILE* out = fopen("b.txt", "w");

    for(int ca=1; ca<=t; ca++){
        scanf("%lf %lf %lf", &c, &f, &x);
        //printf("%lf %lf %lf\n", c, f, x);
        fprintf(out, "Case #%d: ", ca);
        double sum = 0;
        double rate = 2.0;
        double n1, n2,a , b;
        while(true){
            n1 = x/rate;
            a = c/rate ;
            b = x/(rate+f);
            n2 = a+ b;
            //printf("%lf %lf+%lf=%lf\n", n1, a, b, n2);

            if(n1<n2){
                sum += n1;
                break;
            }
            else{
                sum += a;
                rate+=f;
            }
            //break;
        }
        fprintf (out, "%.7lf\n", sum);

    }

    return 0;
}

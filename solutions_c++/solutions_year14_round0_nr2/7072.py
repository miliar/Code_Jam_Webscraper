#include <cstdio>

using namespace std;

double izracunaj(double c, double f, double x, int n) { // koliko farmi cu kupiti
    if(c > x) return x / 2.0;

    double proizvodim = 2.0;
    double v = 0;
    for(int i = 0; i < n; ++i) {
        double vremena = c / proizvodim;
        v += vremena;
        proizvodim += f;        
    }
    
    return v + x / proizvodim;
}

int main() {
    int test;
    double c,f,x;
    scanf("%d", &test);
    
    for(int t = 0; t < test; ++t) {
        scanf("%lf %lf %lf", &c, &f, &x);
        double sol = izracunaj(c, f, x, 0);
        double prethodna = -1;
        for(int n = 1; n < 100000; ++n) {
            double cijena = izracunaj(c, f, x, n);
            if(cijena < sol) sol = cijena;
            if(prethodna != -1 && prethodna <= cijena) {
                break;
            }
            prethodna = cijena;

            //printf("%d %lf\n", n, cijena);
        }
        printf("Case #%d: %lf\n", t+1, sol);
    }

    return 0;
}

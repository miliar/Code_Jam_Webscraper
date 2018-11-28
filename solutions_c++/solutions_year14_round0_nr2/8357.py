#include <cstdio>

using namespace std;

double c, f, x, prajs[102];
int T;

int main () {
    scanf("%d", &T);
    /*scanf("%lf %lf %lf", &c, &f, &x);
    printf("%lf", (double) c/f);*/
    for(int i=1; i<=T; ++i) {
        scanf("%lf %lf %lf", &c, &f, &x);
        double curr =  2.00000000;
        while((x/curr) > (c/curr) + (x/(curr+f))) {
            prajs[i]+= (c/curr);
            curr+=f;
        }
        prajs[i]+=(x/curr);
    }
    for(int i=1; i<=T; ++i) printf("Case #%d: %.7lf\n", i, prajs[i]);
    return 0;
}

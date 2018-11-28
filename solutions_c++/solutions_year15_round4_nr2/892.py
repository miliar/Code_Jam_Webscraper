#include <cstdio>
#include <cstring>
#include <cmath>

#define max(a, b) (a > b ? a : b)
#define min(a, b) (a < b ? a : b)
#define EPS 1e-6

using namespace std;

inline long double cmpf(long double a, long double b) {
    if (fabs(a-b) < EPS) return 0;
    return a < b ? -1 : 1;
}

int T, C=1, n;
long double vfinal, tfinal, taxa[128], temp[128];

int main() {

    for(scanf("%d",&T);T--;) {
        printf("Case #%d: ",C++);
        scanf("%d %Lf %Lf",&n,&vfinal,&tfinal);
        for (int i=0;i<n;i++)
            scanf("%Lf %Lf",taxa+i, temp+i);

        if (n==1) {
            if (cmpf(temp[0],tfinal)!=0)
                printf("IMPOSSIBLE\n");
            else
                printf("%.9Lf\n",vfinal/taxa[0]);
            continue;
        }

        if ((cmpf(temp[0],tfinal)>0 and cmpf(temp[1],tfinal)>0) or
            (cmpf(temp[0],tfinal)<0 and cmpf(temp[1],tfinal)<0)) {
            printf("IMPOSSIBLE\n");
            continue;
        }
        if (cmpf(temp[0], temp[1]) ==0) {
            if (cmpf(temp[0],tfinal)!=0)
                printf("IMPOSSIBLE\n");
            else {
                long double ini = 0.0, fim = 1e10;
                for (int tt=0;tt<10000;tt++) {
                    long double meio = (ini+fim)/2.0;
                    long double vol = taxa[0]*meio + taxa[1]*meio;
                    if (vol > vfinal)
                        fim = meio;
                    else
                        ini = meio;
                }
                printf("%.9Lf\n",ini);

            }
            continue;
        }
        long double vol0 = (tfinal*vfinal - vfinal*temp[1])/(temp[0]-temp[1]);
        long double vol1 = vfinal - vol0;
        long double tempo = max( vol0/taxa[0] , vol1/taxa[1] );
        long double menor = tempo;
        printf("%.9Lf\n", menor);

    }

    return 0;
}

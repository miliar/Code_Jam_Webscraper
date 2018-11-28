#include <cstdio>
#include <cstdlib>
#include <algorithm>

#define eps 1.0E-7 // 1e-7
#define N 1000000

using namespace std;

int main() {
    int T;
    double C, F, X;
    scanf("%d", &T);
for(int kase = 1; kase <= T; kase++) {
    double *dist = (double *)malloc(sizeof(double)*(N+10));
    scanf("%lf %lf %lf", &C, &F, &X);
    double g, lin, lux, best;
    lin = 0.0f;
    g = 2.0;
    lux = X/g;
    dist[0] = lin+lux;
        //printf("Paso de %f\n", g);
        //printf("Lineal acumulado de %f\n", lin);
        //printf("Con %d fabricas me toma %f terminar\n", 0, lux);
        //printf("-----La distancia con %d fabricas es %f-----\n", 0, dist[0]);
    for(int i = 1; i <= N; i++) {
        lin += C/g; // acumulado del lineal
        g = 2.0+i*F; // el paso
        //printf("Paso de %f\n", g);
        //printf("Lineal acumulado de %f\n", lin);
        lux = X/g; // lo que tarda en llegar desde este nodo del lineal
        //printf("Con %d fabricas me toma %f terminar\n", i, lux);
        dist[i] = lin + lux;
        //printf("-----La distancia con %d fabricas es %f-----\n", i, dist[i]);
    }
    best = 2000000.0;
    for(int i = 0; i <= N; i++)
        if((dist[i]-best) < eps)
            best = dist[i];
    printf("Case #%d: %.7f\n", kase, best);
}
}

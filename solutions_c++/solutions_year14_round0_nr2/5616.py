#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


double C[100],F[100],X[100],T,TT = 0.0,T2;
int counter = 0, N = 0;

double CalcValue(double C1, double F1, double X1, int N) {
    double T1 = ( X1 / ( 2 + ( F1 * N ) ) );
    TT += ( C1 / ( 2 + ( F1 * ( N - 1 ) ) ) ) ;
    return T1 + TT;
}
void make1( int nt ) {
    scanf("%lf %lf %lf", &C[nt], &F[nt], &X[nt]);
}
void make() {
    printf("Case #%d: ", ++counter);
    T = X[counter - 1] / 2.0;
    T2 = CalcValue(C[counter - 1],F[counter - 1],X[counter - 1],++N);
    while( T2 < T ){
        T = T2;
        T2 = CalcValue(C[counter - 1],F[counter - 1],X[counter - 1],++N);
    }
    printf("%10.7f\n", T);
}

int main() {
    int t,t2; scanf("%d", &t);
    t2 = 0;
    while(t2 < t) {
        make1(t2);
        t2++;
    }
    while(t--) {
        TT = 0.0;
        N = 0;
        make();
    }
    return 0;
}

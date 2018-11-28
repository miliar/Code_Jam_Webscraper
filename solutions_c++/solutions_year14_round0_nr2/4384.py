#include <cstdio>
#include <iostream>

using namespace std;
#define D(x) cout << #x " is " << (x) << endl
#define IMPRIMIR(X,Y) printf("Case #%d: %.7lf\n",(X),(Y))

int main () {

    freopen("B-large.in","r",stdin);
    freopen("B-large.out","w",stdout);

    int k = 1;
    int casos;
    scanf("%d",&casos);
    //float C,F,X;
    double C,F,X;
    while (k <= casos) {
        double tiempo = .0;
        double total_tiempo = .0;
        double cookies = 2.0;
        scanf("%lf %lf %lf",&C,&F,&X);
        double minimo = X / cookies;
        double resultado = minimo;
        while (true) {
            if (resultado <= minimo) {
                minimo = resultado;
            }else {
                break;
            }
            tiempo = X / cookies;
            resultado = tiempo + total_tiempo;
            total_tiempo+= C / cookies;
            cookies+= F;
        }
        IMPRIMIR(k,minimo);
        k++;
    }


return 0;
}

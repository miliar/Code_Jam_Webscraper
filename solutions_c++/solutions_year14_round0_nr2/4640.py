#include <cstdio>
#include <algorithm>
using namespace std;
FILE *in = fopen("B-small-attempt0.in","r");
FILE *out = fopen("saida.txt","w");

double atual;
double C, F, X;

void f(int n) {
    double aux = C-X;
    aux /= (F*(n-1)+2.0);
    atual += aux;
    aux = X;
    aux /= (F*n+2.0);
    atual += aux;
}

int main() {
    int T;
    fscanf(in,"%d",&T);
    for (int t=1; t<=T; t++) {
        fprintf(out,"Case #%d: ",t);
        fscanf(in,"%lf %lf %lf",&C,&F,&X);
        double resp = X;
        resp /= (2.0);
        atual = resp;
        int k = 1;
        while (1) {
            f(k);
            if (resp < atual) break;
            if (resp-atual < (1E-7)) break;
            resp = atual;
            k++;
        }
        fprintf(out,"%.7f\n",resp);
    }
    return 0;
}

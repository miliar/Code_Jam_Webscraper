#include <stdio.h>
#include <fstream>

double eps = 0.01;

using namespace std;

/*ifstream cin("input.txt");
ofstream cout("output2.txt");
*/

double tim(double c, double cf, double f, double x, long double a, long double b){
    long double tm;
    while(true) { // До return.
            tm = x/cf;
            if(tm < eps)
                    return min(b, tm+a);
            b = min(b, tm+a);
            a += c/cf;
            cf += f;
    }
}


int main(){
    int t;
    FILE* fio = fopen("input.txt", "r");
    FILE* fi = fopen("output2.txt", "w");
    fscanf(fio, "%i", &t);
    //cout.precision(8);
    double w[t], c[t], f[t], x[t];
    for(int i = 0; i < t; i++){
        fscanf(fio, "%lf", &c[i]);
        fscanf(fio, "%lf", &f[i]);
        fscanf(fio, "%lf", &x[i]);
    }
    for(int i = 0; i < t; i++)
        fprintf(fi, "Case #%i: %.7lf\n", i+1, tim(c[i], 2, f[i], x[i], 0, x[i]/2));
    return 0;
}


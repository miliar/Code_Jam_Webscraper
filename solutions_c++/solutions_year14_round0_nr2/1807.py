#include <iostream>
#include <cstdio>

using namespace std;

int T;
double C;
double F;
double X;

int caseNum = 0;

double dontget(int num) {
    double n = (double)num;
    return X/(2+n*F);
}

double beforeget(int num) {
    double n = (double)num;
    return C/(2+n*F);
}

double afterget(int num) {
    double n = (double)num;
    return X/(2+n*F+F);
}

void doIt() {
    cin >> C >> F >> X;
    int num = 0;
    double elapsed = 0;
    while (true) {
        double dgf = dontget(num);
        double bf = beforeget(num);
        double af = afterget(num);
        double gf = bf+af;
        //printf("dgf: %.06lf, bg: %.06lf, ag: %.06lf, gf: %.06lf\n", dgf, bf, af, gf);
        if (gf < dgf) {
            num++;
            elapsed += bf;
        } else {
            elapsed += dgf;
            break;
        }
    }
    printf("Case #%d: %.08lf\n", ++caseNum, elapsed);
    //printf("Case #%d: %d\n", ++caseNum, num);
}

int main() {
    cin >> T;
    for (int i = 0; i < T; i++) {
        doIt();
    }
}

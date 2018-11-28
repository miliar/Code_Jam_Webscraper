#include <iostream>
#include <fstream>
#define ABS(x) ((x) < 0 ? - (x) : (x))
using namespace std;

int main() {
    FILE* f = fopen("out.txt","w");
    int T;
    ifstream in("in.txt");
    in>>T;
    for(int k=0;k<T;k++) {
        // target is X
        // cost is C
        // bonus is F/sec
        double C,F,X;
        in>>C>>F>>X;
        double scale = C/F;
        double timeNeeded = 0;
        double cookies = 0;
        double r = 2;
        while(true) {
            double advCookies = X-scale*r;
            if(advCookies > C) {
                double timeForPurchase = max((C - cookies) / r, 0.);
                cookies += timeForPurchase * r;
                timeNeeded += timeForPurchase;
                cookies -= C;
                r += F;
            }
            else
                break;
        }
        timeNeeded += (X - cookies) / r;
        fprintf(f, "Case #%i: %.7f\n",(k+1),timeNeeded);
    }
    fclose(f);
}
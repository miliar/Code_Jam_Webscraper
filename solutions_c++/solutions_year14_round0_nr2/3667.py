#include <iostream>
#include <fstream>
#include <cstdio>
using namespace std;
ifstream fin("cookieclicker.in");

int main(){
    FILE * fout;
    fout = fopen("cookieclicker.out", "w");
    int T;
    fin >> T;
    for(int cases = 1; cases <= T; cases++){
        double C, F, X, r = 2.0;
        fin >> C >> F >> X;
        if(C >= X){
            fprintf(fout, "Case #%d: %.7lf\n", cases, X / r);
            continue;
        }
        double time = C / r, ftime = X / r;
        while(true){
            if(X / (r + F) + time < ftime){
                ftime = X / (r + F) + time;
                r += F;
            }
            else break;
            time += (C / r);
        }
        fprintf(fout, "Case #%d: %.7lf\n", cases, ftime);
    }
}

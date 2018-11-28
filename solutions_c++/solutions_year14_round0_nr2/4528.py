#include <iostream>
#include <algorithm>
#include <iomanip>
#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main() {
    double C, F, X, ans, newAns, prodRate;
    int T;

    FILE *fin, *fout;
    fin = fopen("input.in", "r");
    fout = fopen("output.out", "w");

    //cin >> T;
    fscanf( fin, "%d", &T );
    for( int t = 1; t <= T; t++ ) {
        //cin >> C >> F >> X;
        fscanf( fin, "%lf %lf %lf", &C, &F, &X );
        ans = X / 2.0;
        prodRate = 2.0 + F;
        newAns = C / 2.0 + X / prodRate;
        while( newAns < ans ) {
            ans = newAns;
            newAns -= X / prodRate;
            newAns += C / prodRate;
            prodRate += F;
            newAns += X / prodRate;
        }
        //cout << "Case #" << t << ": " << fixed << setprecision( 7 ) << ans << endl;
        fprintf( fout, "Case #%d: %.7lf\n", t, ans );
    }

    return 0;
}

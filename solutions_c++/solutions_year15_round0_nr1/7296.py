#include <iostream>
#include <stdio.h>
using namespace std;

int main() {
    char members[ 1010 ];
    int T, Smax;

    FILE *fin, *fout;
    fin = fopen("input.in", "r");
    fout = fopen("output.out", "w");

    //cin >> T;
    fscanf(fin, "%d", &T);
    for( int t = 1; t <= T; t++ ) {
        fscanf(fin, "%d %s", &Smax, members);
        //cin >> Smax >> members;

        int stoodUp = members[ 0 ] - '0', invited = 0;
        for( int i = 1; i <= Smax; i++ ) {
            if( i > stoodUp ) {
                int temp = i - stoodUp;
                invited += temp;
                stoodUp += temp;
            }
            stoodUp += members[ i ] - '0';
        }

        //cout << "Case #" << t << ": " << invited << endl;
        fprintf( fout, "Case #%d: %d\n", t, invited );
    }

    return 0;
}

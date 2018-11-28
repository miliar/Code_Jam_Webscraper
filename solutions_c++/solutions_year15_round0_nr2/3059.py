#include <iostream>
#include "math.h"

using namespace std;

int test(){
    int D;
    int minutes;
    cin >> D;
    int plates[1001];
    int trial[1001];
    int max = 0;
    for ( int i = 0; i < D; ++i ){
        cin >> plates[i];
        if ( plates[i] > max ){
            max = plates[i];
        }
    }
    minutes = max;
    for ( int j = 1; j <= max; ++j ) {
        int additional = 0;
        for ( int i = 0; i < D; ++i ){
            additional += ceil(plates[i] / float(j)) - 1;
        }
        if ( j + additional < minutes ){
            minutes = j + additional;
        }
    }

    return minutes;
}

int main(int argc, char const *argv[]){
    int nCase;
    cin >> nCase;

    for ( int k = 0; k < nCase; ++k ){
        int ans = test();
        cout << "Case #" << k + 1 << ": " << ans << endl; 
    }

    return 0;
}
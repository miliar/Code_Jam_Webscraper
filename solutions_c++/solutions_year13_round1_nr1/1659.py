#include <iostream>//#include "gmp.h"
//#include "gmpxx.h"


//#define PI 3.1415926535897

using namespace std;

int main( void ) {
    int T;
    cin >> T;
    for(int k = 0; k < T; ++k) {
        int r, t, rings = 1;
        cin >> r >> t;
        r+=1;
        t -= r*r - (r-1)*(r-1);
         r += 2;
        while(t >= r*r - (r-1)*(r-1)){
            t -= r*r - (r-1)*(r-1);
            r += 2;
            rings += 1;
        }
        cout << "Case #" << k + 1 << ": " << rings << endl;
    }
    return 0;
}

bool canDraw(int t, int r){

}

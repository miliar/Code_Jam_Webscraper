#include <iostream>
#include <cstdio>

using namespace std;

int main() {
    int T;
    double C, F, X, ratio;
    double ntime, current;

    cin >> T;

    for(int ix = 1; ix <= T; ix++) {
        ratio = 2.0;
        cin >> C >> F >> X;
        current = C/ratio;
        ntime = X/ratio;
        ratio += F;

        while(ntime > X/ratio+current) {
            ntime = X/ratio+current;
            current += C/ratio;
            ratio += F;
        }

        printf("Case #%d: %.7f\n", ix, ntime);
    }

    return 0;	
}

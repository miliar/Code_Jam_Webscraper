#include <cstdlib>
#include <cmath>
#include <cstdio>
#include <iostream>
#include <string>
using namespace std;

int main() {
    int t;
    cin >> t;

    for (int i = 1; i <= t; i++) {
        int d;
        cin >> d;
        int* p = new int[d];
        int pmax = 1;

        for (int j = 0; j < d; j++) {
            cin >> p[j];
            if (pmax < p[j]) {
                pmax = p[j];
            }
            //printf("p[j] = %d\n", p[j]);
        }

        int min = 1000;

        if (pmax == 1) {
            min = 1;
        } else if (pmax == 2) {
            min = 2;
        } else if (pmax == 3) {
            min = 3;
        } else {
            for (int m = 2; m <= pmax; m++) {
                //printf("m = %d\n", m);
                int moves = 0;
                for (int j = 0; j < d; j++) {
                    if (p[j] > m) {
                        moves += ceil((float)p[j]/m) - 1;
                    }
                }
                //printf("moves = %d\n", moves);
                if (min > m+moves) {
                    min = m+moves;
                }
            }
        }
        cout << "Case #" << i << ": " << min << endl;
    }

    return 0;
}

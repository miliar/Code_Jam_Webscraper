#include <bits/stdc++.h>
#define CHECK_BIT(var,pos) ((var) & (1<<(pos)))
using namespace std;

// probability that a committee with members up to i have exactly j yes votes
long double probs[20][20];
int t, k, n;
long double ps[205];


int main() {
    cin >> t;
    for (int test = 1; test <= t; test++) {
        cin >> n >> k;
        for (int i = 0; i < n; i++) {
            cin >> ps[i];
        }

        long double max = 0.0;
        for (int i = 0; i < 70000; i++) {
            int numSet = 0;
            for (int k = 0; k <= 16; k++) {
                probs[0][k]= 0;
            }
            for (int j = 0; j < n; j++) {
                if (CHECK_BIT(i, j)) {
                    numSet++;
                if (j == 0) {
                    probs[0][1] = ps[0];
                    probs[0][0] = 1 - (ps[0]);
                    continue;
                }
                    for (int k = 0; k <= 16; k++) {
                        probs[j][k] = probs[j - 1][k] * (1 - ps[j]);
                        if (k > 0) probs[j][k] += probs[j - 1][k - 1] * ps[j];
                    }
                } else {
                if (j == 0) {
                    probs[0][1] = 0;
                    probs[0][0] = 1;
                    continue;
                }
                    for (int k = 0; k <= 16; k++) {
                        probs[j][k] = probs[j - 1][k];
                    }
                }
            }

            // if (i == 0x3C) {
            //     for (int j = 0; j < n; j++) {
            //         for (int k = 0; k <= 16; k++) {
            //             cout << probs[j][k] << " ";
            //         }
            //         cout << endl;
            //     }
            // }
            if (numSet == k && probs[n - 1][k / 2] > max) {
                max = probs[n - 1][k / 2];
            }
        }
        cout << "Case #" << test << ": " << max << endl;
    }
    
}
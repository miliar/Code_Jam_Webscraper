#include <iostream>
#include <stdio.h>
#include <stdlib.h>
#include <math.h>

using namespace std;

int T, N;
int used[10];

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);

    cin >> T;
    for (int t = 1; t <= T; ++t) {
        cin >> N;

        if (N == 0) {
            cout << "Case #" << t << ": " << "INSOMNIA" << endl;
        } else {
            for (int i = 0; i < 10; ++i) {
                used[i] = 0;
            }

            long long ans = N;
            for (int i = 1; i < (int)1e9; ++i) {
                bool zero = false;
                for (int j = 0; j < 10; ++j) {
                    if (used[j] == 0) {
                        zero = true;
                    }
                }

                if (!zero) {
                    break;
                }

                long long NN = i * N;
                ans = NN;
                while (NN) {
                    used[NN % 10] = 1;
                    NN /= 10;
                }
            }
            cout << "Case #" << t << ": " << ans << endl;
        }
    }

    return 0;
}
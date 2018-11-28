#include <iostream>
#include <string>
#include <set>
using namespace std;

int main() {
    long T, K, C, S;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        cin >> K >> C >> S;
        cout << "Case #" << t << ":";
        if (C * S < K) {
            cout << " IMPOSSIBLE" << endl;
            continue;
        }

        long tile = 0;
        while (tile < K) {
            long check = 0;
            for (int i = 0; i < C; i++) {
                check *= K;
                check += tile++ % K;
            }
            cout << " " << 1 + check;
        }
        cout << endl;
    }
}

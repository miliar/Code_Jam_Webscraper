#include <iostream>
#include <string>
using namespace std;

// Not worth thinking if the inputs are so small...

int main() {
    int T;
    cin >> T;
    for (int x = 1; x <= T; x++) {
        cout << "Case #" << x << ": ";
        string S;
        int K;
        cin >> S >> K;
        int i = 0, flips = 0;
        for (; i + K - 1 < S.size(); i++) {
            if (S[i] == '-') {
                for (int j = 0; j < K; j++)
                    S[i + j] ^= '-' ^ '+';
                flips++;
            }
        }
        for (; i < S.size(); i++)
            if (S[i] == '-')
                flips = -1;
        if (flips < 0)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << flips << endl;
    }
}

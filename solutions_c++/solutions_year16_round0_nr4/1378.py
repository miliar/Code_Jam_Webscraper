 
#include <iostream>
using namespace std;

int main() {
    int T, i;
    cin >> T;
    for (i = 0; i < T; i++) {
        int K, C, S, j;
        cin >> K >> C >> S;
        if (S != K) continue;
        cout << "Case #" << (i + 1) << ":";
        long long size = 1, step;
        for (j = 0; j < C; j++) size *= K;
        step = K > 1 ? (size - 1) / (K - 1) : 0;
        for (j = 0; j < S; j++)
            cout << ' ' << (j * step + 1);
        cout << endl;
    }
    return 0;
}

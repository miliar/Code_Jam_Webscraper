
#include <bits/stdc++.h>
using namespace std;

int nbits(int i) {
     i = i - ((i >> 1) & 0x55555555);
     i = (i & 0x33333333) + ((i >> 2) & 0x33333333);
     return (((i + (i >> 4)) & 0x0F0F0F0F) * 0x01010101) >> 24;
}

main() {
    int T, R, C, N, i, n, x, y;
    int *A = new int[16];
    cin >> T;
    for (i = 0; i < T; i++) {
        cin >> R >> C >> N;
        int res = 0;
        if (N != 0) {
            res = 1000;
            for (n = 1; n < (1 << R * C); n++) {
                if (nbits(n) != N) continue;
                for (x = 0; x < R * C; x++)
                    A[x] = (n & (1 << x)) ? 1 : 0;
                int val = 0;
                for (y = 0; y < R; y++)
                    for (x = 1; x < C; x++)
                        if (A[y * C + x] && A[y * C + x - 1]) val++;
                for (x = 0; x < C; x++)
                    for (y = 1; y < R; y++)
                        if (A[y * C + x] && A[y * C + x - C]) val++;
                if (val < res)
                    res = val;
            }
        }
        cout << "Case #" << (i + 1) << ": " << res << endl;
    }
}

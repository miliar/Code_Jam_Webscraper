#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <algorithm>
using namespace std;

int main() {
    int T;
    cin >> T;
    for (int t = 1; t <= T; t++) {
        int K, L, S;
        string k, l;
        cin >> K >> L >> S >> k >> l;
        int offset = 1;
        while (offset < L) {
            if (l.substr(0, L - offset) == l.substr(offset, L - offset)) break;
            offset++;
        }
        double needed = (L <= S) ? 1 + (S - L) / offset : 0;
        double counts[256];
        double lcounts[256];
        for (int i = 0; i < 256; i++) counts[i] = 0;
        for (int i = 0; i < K; i++) counts[k[i]]++;
        for (int i = 0; i < L; i++) if (!counts[l[i]]) needed = 0;

        double expected = 1.0;
        for (int i = 0; i < L; i++) expected *= counts[l[i]] / K;
        expected *= max(0, S - L + 1);
        cout << "Case #" << t << ": ";
        printf("%.9f\n", needed - expected);
    }
}

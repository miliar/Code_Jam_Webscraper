
#include <iostream>
#include <string>
#include <vector>
#include <cmath>

using namespace std;

static int Tmap[4][4] = {
    {1, 2, 3, 4},
    {2, -1, 4, -3},
    {3, -4, -1, 2},
    {4, 3, -2, -1}
};

int combine(int a, int b) {
    int sign = (a * b > 0) ? 1 : -1,
        i1 = abs(a) - 1, i2 = abs(b) - 1;
    return sign * Tmap[i1][i2];
}
int convert(char c) {
    if (c == 'i') return 2;
    if (c == 'j') return 3;
    if (c == 'k') return 4;
    return 1;
}

bool solve(string S, int X, int N) {
    return false;
}

bool simple(string S, int X, int N) {
    string SS;
    int NN = N * X, i, j, k;
    for (i = 0; i < X; i++)
        SS += S;

    vector<int> L(NN + 1), R(NN + 1);
    L[0] = R[0] = 1;
    for (i = 1; i <= NN; i++) {
        L[i] = combine(L[i - 1], convert(SS[i - 1]));
        R[i] = combine(convert(SS[NN - i]), R[i - 1]);
    }

    for (i = 1; i < NN; i++) {
        if (L[i] != 2) continue;
        if (R[NN - i] != 2) continue;
        for (j = i + 1; j < NN; j++) {
            if (R[NN - j] != 4) continue;
            return true;
        }
    }
    return false;
}

main() {
    int T, L, X, i;
    cin >> T;
    for (i = 0; i < T; i++) {
        string S;
        cin >> L >> X >> S;
        bool res = simple(S, X, L);
        cout << "Case #" << (i + 1) << ": " << (res ? "YES" : "NO") << endl;
    }
}

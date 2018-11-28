#include <iostream>
#include <stdio.h>
#include <string.h>

using namespace std;

int T, K, L, S, DP1[110][110], F[110];
long double DP2[110][110];
string C, E;
int getMax(int curr, int match) {
    if (curr == S) return 0;

    if (DP1[curr][match] != -1) return DP1[curr][match];

    int ret = 0;
    for (int i = 0; i < K; i++) {
        int next_match = match;
        while (next_match > 0 && E[next_match] != C[i]) {
            next_match = F[next_match];
        }

        if (E[next_match] == C[i]) {
            if (next_match + 1 == L) {
                ret = max(ret, 1 + getMax(curr + 1, F[next_match + 1]));
            } else {
                ret = max(ret, getMax(curr + 1, next_match + 1));
            }
        } else {
            ret = max(ret, getMax(curr + 1, 0));
        }
    }

    return DP1[curr][match] = ret;
}

long double getExpected(int curr, int match) {
    if (curr == S) return 0;

    if (DP2[curr][match] != -1) return DP2[curr][match];

    long double ret = 0;
    for (int i = 0; i < K; i++) {
        int next_match = match;
        while (next_match > 0 && E[next_match] != C[i]) {
            next_match = F[next_match];
        }

        long double P = 1.0 / K;
        if (E[next_match] == C[i]) {
            if (next_match + 1 == L) {
                ret += P * (1 + getExpected(curr + 1, F[next_match + 1]));
            } else {
                ret += P * getExpected(curr + 1, next_match + 1);
            }
        } else {
            ret += P * getExpected(curr + 1, 0);
        }
    }

    return DP2[curr][match] = ret;
}
int main() {
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);

    cin >> T;
    for(int cs = 0; cs < T; cs++) {
        cin >> K >> L >> S;
        cin >> C >> E;

        for(int c = 1; c <= L; c++) {
            F[c] = 0;
            for(int d = 1; d < c; d++) {
                int ok = true;
                for(int i = 0; i < d; i++)
                    if (E[i] != E[i + c - d]) ok = false;
                if (ok)
                    F[c] = d;
            }
        }

        memset(DP1, -1, sizeof(DP1));
        memset(DP2, -1, sizeof(DP2));
        for(int i = 0; i < 110; i++)
        for(int j = 0; j < 110; j++)
            DP2[i][j] = -1;

        long double mx = getMax(0, 0);
        long double expected = getExpected(0, 0);

        printf("Case #%d: %.12Lf\n", cs + 1, mx - expected);
    }

    return 0;
}

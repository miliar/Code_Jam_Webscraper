// Written by Luis Garcia, 2016.
// OJ-ID: CJ1603B

#include <cstdio>
#include <cstring>
#include <cstdlib>
#include <cmath>

using namespace std;

bool f(int N, int i, char * C, char * J, char * D, char * K, bool e, long long & best, long long & a, long long & b) {
    if (N == i) {
        D[i] = K[i] = 0;
        long long i = atoll(D), j = atoll(K), t = abs(i - j);
        if (t < best || (t == best && (i < a || (i == a && j < b)))) {
            best = t, a = i, b = j;
        }
        return true;
    }

    if (C[i] != '?') D[i] = C[i];
    if (J[i] != '?') K[i] = J[i];
    
    auto next = [&]() { return f(N, i + 1, C, J, D, K, e && D[i] == K[i], best, a, b); };

    bool valid = false;
    if (C[i] != '?' && J[i] != '?') {
        if (e && C[i] > J[i]) return false;
        return next();
    } else if (e) {
        if (C[i] == '?' && J[i] == '?') {
            D[i] = '0';
            for (char c = '0'; c <= '1'; ++c) {
                K[i] = c;
                valid |= next();
            }
        }

        if (J[i] == '?') {
            for (char c = C[i]; c <= C[i] + 1 && c <= '9'; ++c) {
                K[i] = c;
                valid |= next();
            }
        }

        if (C[i] == '?') {
            for (char c = J[i]; c >= J[i] - 1 && c >= '0'; --c) {
                D[i] = c;
                valid |= next();
            }
        }
    } else {
        if (C[i] == '?') D[i] = '9';
        if (J[i] == '?') K[i] = '0';
        valid |= next();
    }

    return valid;
}

int main() {
    char C[20], J[20], D[20], K[20];

    int T;
    scanf("%d", &T);
    for (int _T = 1; _T <= T; ++_T) {
        scanf("%s %s", C, J);
        int N = strlen(C);

        long long best = 0x7fffffffffffffff, a = 0, b = 0;
        f(N, 0, C, J, D, K, true, best, a, b);
        f(N, 0, J, C, K, D, true, best, b, a);

        printf("Case #%d: %0*lld %0*lld\n", _T, N, a, N, b);
    }
    return 0;
}

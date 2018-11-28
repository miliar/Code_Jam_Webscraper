#include <cstdio>
using namespace std;

const int I = 2, J = 3, K = 4;

int conv(char c) {
    switch (c) {
        case '1': return 1;
        case 'i': return I;
        case 'j': return J;
        case 'k': return K;
    }
    return 0;
}

int prod(int a, int b) {
    if (a < 0) return -prod(-a, b);
    if (b < 0) return -prod(a, -b);
    int m[4][4] = {
        {1,  I,  J,  K},
        {I, -1,  K, -J},
        {J, -K, -1,  I},
        {K,  J, -I, -1}
    };
    return m[a-1][b-1];
}

char s[10001];
int intprod[10000][10001];

int main() {
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        int l, x;
        scanf("%d%d%s", &l, &x, s);
        for (int k = 1; k < x; k++)
            for (int i = 0; i < l; i++)
                s[i + l*k] = s[i];
        s[l*x] = '\0';
#pragma omp parallel for
        for (int i = 0; i < l*x; i++) {
            intprod[i][i+1] = conv(s[i]);
            for (int j = i+2; j <= l*x; j++) {
                intprod[i][j] = prod(intprod[i][j-1], conv(s[j-1]));
            }
        }
        bool ans = false;
        for (int i = 1; i < l*x-1; i++) {
            for (int j = i+1; j < l*x; j++) {
                if (intprod[0][i] == I && intprod[i][j] == J && intprod[j][l*x] == K)
                {
                    ans = true; break; 
                }
            }
            if (ans) break;
        }
        printf("Case #%d: %s\n", t, ans ? "YES" : "NO");
    }
    return 0;
}

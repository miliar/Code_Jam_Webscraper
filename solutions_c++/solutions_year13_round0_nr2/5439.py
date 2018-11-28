#include <iostream>
#include <cstdio>
using namespace std;
#define N 101

int n, m;
int d[N][N], s[N][N];

char const * solve() {
    for (int i = 0; i < m; ++i) {
        int max = -1;
        for (int j = 0; j < n; ++j) {
            if (d[j][i] > max) {
                max = d[j][i];
            }
        }
        for (int j = 0; j < n; ++j) {
            s[j][i] = max;
        }
    }
    for (int i = 0; i < n; ++i) {
        bool needCut = false;
        for (int j = 0; j < m; ++j) {
            if (s[i][j] > d[i][j]) {
                needCut = true;
                break;
            }
        }
        if (needCut) {
            for (int j = 0; j < m; ++j) {
                if (s[i][j] > d[i][0]) {
                    s[i][j] = d[i][0];
                }
            }
        }
    }
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            if (s[i][j] != d[i][j]) {
                //char * c = new char[100];
                //sprintf(c, "s[%d][%d] = %d, d = %d\n", i, j, s[i][j], d[i][j]);
                //return c;
                return "NO";
            }
        }
    }
    return "YES";
}    

int main() {
    int t;
    scanf("%d", &t);
    for (int i = 1; i <= t; ++i) {
        scanf("%d", &n);
        scanf("%d", &m);
        for (int j = 0; j < n; ++j) {
            for (int k = 0; k < m; ++k) {
                scanf("%d", &d[j][k]);
            }                
        }
        printf("Case #%d: %s\n", i, solve());
    }
    return 0;
}

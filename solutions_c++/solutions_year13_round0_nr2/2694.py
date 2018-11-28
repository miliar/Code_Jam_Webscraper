#define _CRT_SECURE_NO_DEPRECATE
#include <cstdio>
#include <vector>
#include <algorithm>
#include <functional>
#include <numeric>
using namespace std;

void solveTestCase() {
    int N, M;
    scanf("%d%d", &N, &M);
    vector< vector<int> > a(N, vector<int>(M));
    for (int i = 0; i < N; ++i) {
        for (int j = 0; j < M; ++j) {
            scanf("%d", &a[i][j]);
        }
    }
    while (N != 0 && M != 0) {
        int x = 0, y = 0;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < M; ++j) {
                if (a[i][j] < a[x][y]) {
                    x = i;
                    y = j;
                }
            }
        }
        int v = a[x][y];
        if (all_of(a[x].begin(), a[x].end(), [v](int p){return p == v;})) {
            a.erase(a.begin() + x);
            --N;
        } else {
            for (int i = 0; i < N; ++i) {
                if (a[i][y] != v) {
                    printf("NO\n");
                    return;
                }
                a[i].erase(a[i].begin() + y);
            }
            --M;
        }
    }
    printf("YES\n");
}

int main(void) {
    int T;
    scanf("%d", &T);
    for (int testNo = 1; testNo <= T; ++testNo) {
        printf("Case #%d: ", testNo);
        solveTestCase();
    }
}

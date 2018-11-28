#include <iostream>
#include <vector>
#include <cstdio>
#include <algorithm>

using namespace std;

int main() {
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int test = 0; test < T; ++test) {
        int N, X;
        scanf("%d%d", &N, &X);
        vector <int> S(N);
        for (int i = 0; i < N; ++i) {
            scanf("%d", &S[i]);
        }
        sort(S.begin(), S.end());
        int ls = S.size() - 1;
        int cnt = S.size();
        for (int i = 0; i < ls; ++i) {
            while (i < ls && S[i] + S[ls] > X) {
                --ls;
            }
            if (i < ls && S[i] + S[ls] <= X) {--cnt; --ls;}
        }
        printf("Case #%d: %d\n", (test + 1), cnt);
    }

}
#include <bits/stdc++.h>

using namespace std;

int main() {
    int T;
    scanf("%d", &T);

    for (int i = 1; i <= T; ++i) {
        int N;
        scanf("%d", &N);

        vector<double> naomi(N);
        vector<double> ken(N);

        for (int j = 0; j < N; ++j) {
            scanf("%lf", &naomi[j]);
        }
        for (int j = 0; j < N; ++j) {
            scanf("%lf", &ken[j]);
        }

        sort(naomi.begin(), naomi.end());
        sort(ken.begin(), ken.end());

        int deceit = 0;
        for (int j = N-1, k = N-1; j >= 0 && k >= 0; --k) {
            if (naomi[j] > ken[k]) {
                deceit += 1;
                j -= 1;
            }
        }

        int war = 0;
        for (int j = N-1, k = N-1; j >= 0 && k >= 0; --j) {
            if (naomi[j] < ken[k]) {
                war += 1;
                k -= 1;
            }
        }

        printf("Case #%d: %d %d\n", i, deceit, N-war);
    }

    return 0;
}
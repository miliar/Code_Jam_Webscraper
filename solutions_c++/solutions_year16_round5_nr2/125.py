#include <iostream>
#include <vector>
#include <cstdlib>
#include <cstdio>

using namespace std;

int main() {
    int T;
    cin >> T;
    for(int t=1;t<=T; ++t) {
        int N;
        cin >> N;

        vector<int> P(N);
        vector<char> L(N);
        for (int i = 0; i < N; ++i) {
            cin >> P[i];
            --P[i];
        }
        for (int i = 0; i < N; ++i) {
            cin >> L[i];
        }

        int M;
        cin >> M;
        vector <string> W(M);
        for (int i = 0; i < M; ++i) {
            cin >> W[i];
        }

        const int TR = 10000;
        vector<double> cnt(M, 0);
        for (int k = 0; k < TR; ++k) {
            string perm;
            vector<bool> used(N, 0);

            for (int i = 0; i < N; ++i) {
                int v = rand() % N;
                while (used[v]) {
                    v = rand() % N;
                }
                while (P[v] >= 0 && !used[P[v]]) {
                    v = P[v];
                }
                perm.push_back(L[v]);
                used[v] = true;
            }
            for (int j = 0; j < M; ++j) {
                cnt[j] += (perm.find(W[j]) < 1000 );
            }
        }
        printf("Case #%d:", t);
        for (int j = 0; j < M; ++j) {
            printf(" %.2f", cnt[j]/TR);
        }
        printf("\n");
    }
    return 0;
}
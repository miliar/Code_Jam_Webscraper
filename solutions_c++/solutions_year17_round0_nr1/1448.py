#include <iostream>
using namespace std;

bool mask[1010];

int main() {
    int T;
    cin >> T;
    for (int c = 1; c <= T; c++) {
        string S;
        int K;
        cin >> S >> K;
        for (int i = 0; i < S.length(); i++) {
            mask[i] = (S[i] == '+');
        }
        int ret = 0;
        for (int i = 0; i <= S.length() - K; i++) {
            if (mask[i]) continue;
            ret++;
            for (int j = 0; j < K; j++) {
                mask[i + j] = !mask[i + j];
            }

            /*for (int l = 0; l < S.length(); l++) printf("%d", mask[l]);
            printf("\n");*/

        }
        bool ok = true;
        for (int i = S.length() - K; i < S.length() && ok; i++) {
            ok = mask[i];
        }

        /*for (int l = 0; l < S.length(); l++) printf("%d", mask[l]);
        printf("\n");*/

        printf("Case #%d: ", c);
        if (ok) printf("%d\n", ret);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}

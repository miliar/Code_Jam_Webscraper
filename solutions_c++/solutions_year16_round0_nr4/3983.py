#include <iostream>
#include <vector>
using namespace std;

int main() {
    int T, K, C, S;
    cin >> T;
    for (int ncase = 1; ncase <= T; ++ ncase) {
        cin >> K >> C >> S;
        int minS = (K - 1) / C + 1;
        if (S < minS) {
            printf("Case #%d: IMPOSSIBLE\n", ncase);
        } else {
            int currP = 0;
            printf("Case #%d:", ncase);
            while (currP < K) {
                long long curr = 0;
                for (int c = 1; c <= C; ++ c) {
                    if (currP < K)
                        curr = curr * K + currP ++;
                    else curr = curr;
                }
                printf(" %lld", curr + 1);
            }
            printf("\n");
        }
    }
    return 0;
}

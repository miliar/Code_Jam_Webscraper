#include <bits/stdc++.h>

using namespace std;

int main() {
    //freopen("in.txt", "r", stdin);
    //freopen("out.txt", "w", stdout);

    int T; scanf("%d", &T);
    for(int t = 1; t <= T; ++t) {
        int N; scanf("%d", &N);
        int ppl_up = 0, needed = 0;
        for(int i = 0; i <= N; ++i) {
            char c; scanf(" %c", &c);
            int n = c - '0';
            if(ppl_up < i) {
                needed += i - ppl_up;
                ppl_up = i;
            }
            ppl_up += n;
        }
        printf("Case #%d: %d\n", t, needed);
    }

    return 0;
}

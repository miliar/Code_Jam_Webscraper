#include <cstdio>
#include <cstring>
#include <string>
#include <algorithm>
using namespace std;

#define MAXN 12

int main() {
    int T, N, order[MAXN];
    char str[MAXN][110];
    bool marked[128];

    scanf("%d", &T);
    for (int t = 1; t <= T; t++) {
        scanf("%d", &N);
        for (int i = 0; i < N; i++) {
            scanf("%s", str[i]);
            order[i] = i;
        }

        int cnt = 0;
        do {
            char s[10010];
            s[0] = 0;
            for (int i = 0; i < N; i++)
                strcat(s, str[order[i]]);
            memset(marked, 0, sizeof(marked));
            bool ok = 1;
            marked[s[0]] = 1;
            for (int i = 0; s[i];) {
                int j = i+1;
                while (s[j] == s[i])
                    j++;
                i = j;
                if (!marked[s[j]]) {
                    marked[s[j]] = 1;
                } else {
                    ok = 0;
                    break;
                }
            }
            if (ok)
                cnt++;
        } while (next_permutation(order, order+N));

        printf("Case #%d: %d\n", t, cnt);
    }
}

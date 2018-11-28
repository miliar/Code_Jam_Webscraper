#include <stdio.h>

int main() {
    int T, K;
    char S[1001];
    int cnt;
    int i, j, k;
    
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w", stdout);
    
    scanf("%d", &T);
    for(i = 0; i < T; i++) {
        scanf("%s %d", S, &K);
        cnt = 0;
        for(j = 0; S[j + K - 1] != 0; j++) {
            if(S[j] == '-') {
                for(k = 0; k < K; k++) S[j + k] = (S[j + k] == '+') ? '-' : '+';
                cnt++;
            }
        }
        for(; S[j] != 0; j++) if(S[j] == '-') break;
        printf("Case #%d: ", i + 1);
        if(S[j] == 0) printf("%d\n", cnt);
        else printf("IMPOSSIBLE\n");
    }
    return 0;
}

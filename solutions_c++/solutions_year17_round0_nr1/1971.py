#include <cstdio>
#include <algorithm>
#include <vector>

int main(){
    //freopen("A-large.in", "r", stdin);
    //freopen("A-large.out", "w", stdout);
    int T, K, S;
    int prefixSum[1005];
    char cakes[1005];

    scanf("%d ", &T);
    for(int t = 1; t <= T; t++){
        for(int i = 0; i < 1005; i++)
            prefixSum[i] = 0;

        scanf(" %s", cakes);
        for(int i = 0; i < 1005; i++){
            if(cakes[i] == '\0'){
                S = i;
                break;
            }
            if(cakes[i] == '+'){
                prefixSum[i]++;
                prefixSum[i+1]--;
            }
        }

        scanf("%d", &K);

        int state = 0, ans = 0;
        for(int i = 0; i <= S - K; i++){
            state += prefixSum[i];
            if(state % 2 == 0){
                ans++;
                prefixSum[i+K]++;
                state++;
            }
        }
        for(int i = S - K + 1; i < S; i++){
            state += prefixSum[i];
            if(state % 2 == 0)
                ans = -1;
        }

        printf("Case #%d: ", t);
        if(ans < 0)
            printf("IMPOSSIBLE\n");
        else
            printf("%d\n", ans);
    }
}

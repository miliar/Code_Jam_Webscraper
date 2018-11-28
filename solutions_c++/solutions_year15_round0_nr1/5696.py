#include <cstdio>

int main() {
    int T;
    int S;
    char K[1001];
    int num = 0;
    int sum = 0;
    scanf("%d", &T);
    
    for (int i = 1; i <= T; i++) {
        scanf("%d", &S);
        num = 0;
        sum = 0;
        //printf("Case #%d : %d ", i, S);
        for (int j = 0; j <= S; j++) {
            scanf(" %c ", &K[j]);
        }
        for (int j = 1; j <= S; j++) {
            sum += (int)(K[j-1] - '0');
            if (sum < j) {
                num += (j - sum);
                sum = j;
            }
        }
        printf("Case #%d: %d\n", i, num);
    }
    return 0;
}

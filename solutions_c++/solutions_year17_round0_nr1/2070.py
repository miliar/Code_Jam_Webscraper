#include <cstdio>
#include <cstring>

int N, K;

char S[1003];

int process() {
    int ret = 0;
    for (int i = 0; i <= N - K; i ++) {
        if (S[i] == '-') {
            ret ++;
            for (int j = 0; j < K; j ++) {
                if (S[i + j] == '+') {
                    S[i + j]= '-';
                } else {
                    S[i + j]= '+';
                }
            }
        }
    }

    for (int i = N - K + 1; i < N; i ++){
        if (S[i] == '-') {
            return -1;
        }
    }

    return ret;
}


int main() {
    int T;
    scanf("%d", &T);
    
    for (int test = 1; test <= T; test ++) {
        scanf("%s %d", S, &K);
        N = strlen(S);

        int answer = process();
        printf("Case #%d: ", test);
        if (answer == -1) {
            printf("IMPOSSIBLE\n");
        } else {
            printf("%d\n", answer);
        }
    }
    return 0;
}

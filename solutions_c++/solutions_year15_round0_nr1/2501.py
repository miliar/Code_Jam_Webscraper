#include <cstdio>

const int MAX_N = 1000;

int T;
int N;
int V[1 + MAX_N];

int answer;

int main(void) {
    char character;
    int t;
    int i;

    // citirea datelor
    scanf("%d", &T);
    for (t = 1; t <= T; ++t) {
        scanf("%d ", &N);
        for (i = 0; i <= N; ++i) {
            scanf("%c", &character);
            V[i] = character - '0';
        }

        // calcularea solutiei
        int sum = 0;
        answer = 0;
        for (i = 0; i <= N; ++i) {
            if (V[i] == 0 && sum <= i) {
                sum++;
                answer++;
            } else {
                sum += V[i];
            }
        }

        // afisarea solutiei
        printf("Case #%d: %d\n", t, answer);
    }
    return 0;
}

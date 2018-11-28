#include <cstdio>

unsigned long long solve(int* s, int N, int maxDown) {
    unsigned long mushroomEaten = 0;
    bool down = false;
    int previous = 0;
    for (int* i = s; i < s + N - 1; ++i) {
        if (*i < maxDown) {
            mushroomEaten += *i;
        } else {
            mushroomEaten += maxDown;
        }
    }
    return mushroomEaten;
}

int main(){
    int T;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        int N;
        scanf("%d", &N);
        int* s = new int[N];

        unsigned long answer1 = 0;
        int maxDown = 0;
        bool down = false;
        int previous = 0;
        for (int* j = s; j < s + N; ++j) {
            scanf("%d", j);
            if (previous > *j) {
                down = true;
            }
            if (down) {
                int downAmt = previous - *j;
                answer1 += downAmt;
                downAmt > maxDown ? maxDown = downAmt : maxDown = maxDown;
            }
            previous = *j;
            down = false;
        }

        
        unsigned long long answer2 = solve(s, N, maxDown);

        // Print answer
        printf("Case #%d: %u %u\n", i, answer1, answer2);
    }
    return 0;
}

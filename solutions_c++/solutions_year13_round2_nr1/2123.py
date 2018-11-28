#include <stdio.h>
#include <stdlib.h>

#define min(x, y) ((x) < (y) ? (x) : (y))

int comp(const void *a, const void *b) {
    return *(int *)a - *(int *)b;
}

int solution(int mymote, int *mote, int N, int index, int count) {
    if (index == N) {
        return count;
    }
    if (mymote > mote[index]) {
        return solution(mymote + mote[index], mote, N, index + 1, count);
    } else {
        if (mymote == 1) {
            return solution(mymote, mote, N, index + 1, count + 1);
        } else {
            return min(solution(mymote, mote, N, index + 1, count + 1), solution(2 * mymote - 1, mote, N, index, count + 1));
        }
    }
    
}

void showResult(int index, int result) {
    printf("Case #%d: %d\n", index, result);
}

int main() {
    freopen("A-small-attempt0.in", "r", stdin);
    freopen("A-small-attempt0.out", "w", stdout);

    int T, A, N;
    scanf("%d", &T);
    for (int i = 1; i <= T; ++i) {
        scanf("%d %d", &A, &N);
        int mote[N];
        for (int j = 0; j < N; ++j) {
            scanf("%d", &mote[j]);
        }
        qsort(mote, N, sizeof(int), comp);
        
        showResult(i, solution(A, mote, N, 0, 0));
    }

    fclose(stdout);
    fclose(stdin);
}

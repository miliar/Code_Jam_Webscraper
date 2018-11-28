#include <cstdio>

int main()
{
    int caseCount;

    scanf(" %d", &caseCount);
    for(int caseIndex = 1; caseIndex <= caseCount; caseIndex++) {
        int A, B, K;

        scanf(" %d %d %d", &A, &B, &K);

        int count = 0;
        for(int i = 0; i < A; i++) {
            for(int j = 0; j < B; j++) {
                if((i & j) < K) {
                    count++;
                }
            }
        }

        printf("Case #%d: %d\n", caseIndex, count);
    }

    return 0;
}

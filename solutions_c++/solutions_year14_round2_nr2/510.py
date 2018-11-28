#include <cstdio>
#include <algorithm>
#include <iostream>
#include <set>
using namespace std;

int main(void) {
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);

    int _case, A, B, K;
    scanf("%d", &_case);
    for (int i = 1; i <= _case; i++) {
        scanf("%d%d%d", &A, &B, &K);
        int result = 0;
        for (int i = 0; i < A; i++) {
            for (int j = 0; j < B; j++) {
                if ((i & j) < K)
                    result++;
            }
        }
        printf("Case #%d: %d\n", i , result);
    }
    return 0;
}

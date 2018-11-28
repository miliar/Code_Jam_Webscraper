#include <iostream>

using namespace std;

int solve(int A, int B, int K)
{
    int ans = 0;
    for (int a = 0; a < A; ++a) {
        for (int b = 0; b < B; ++b) {
            if ((a & b) < K)
                ++ans;
        }
    }
    return ans;
}

int main()
{
    int T;
    cin >> T;
    for (int i = 1; i <= T; ++i) {
        int A, B, K;
        scanf("%d %d %d\n", &A, &B, &K);
        printf("Case #%d: %d\n", i, solve(A, B, K));
    }

    return 0;
}


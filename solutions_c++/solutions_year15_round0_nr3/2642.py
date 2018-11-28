#include <cstdio>

const int N = 10000, M = 9, TABLE[M][M] =
{
    {0},
    {0, 1, 2, 3, 4, 5, 6, 7, 8},
    {0, 2, 8, 4, 6, 3, 5, 1, 7},
    {0, 3, 5, 8, 2, 7, 1, 4, 6},
    {0, 4, 3, 7, 8, 1, 2, 6, 5},
    {0, 5, 6, 2, 1, 8, 7, 3, 4},
    {0, 6, 4, 1, 7, 2, 8, 5, 3},
    {0, 7, 1, 5, 3, 6, 4, 8, 2},
    {0, 8, 7, 6, 5, 4, 3, 2, 1}
};

// int transform(char c)
// {
//     return c - 'g';
// }
// int sum(int s[], int n)
// {
//     if (n == 1) return s[0];
//     int m = n >> 1;
//     return TABLE[sum(s, m)][sum(s + m, n - m)];
// }

int main()
{
    char buffer[N+5];
    int T, L, X, sequence[N+5], sum[N+5] = {1};
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d%d", &L, &X);
        scanf("%s", buffer);
        int length = 1, ok = 0, first_i = -1, last_j = -1;
        for (int i = 0; i < X; ++i)
        for (int j = 0; j < L; ++j, ++length)
        {
            sequence[length] = buffer[j] - 'g';
            sum[length] = TABLE[sum[length-1]][sequence[length]];
            if (first_i == -1 && sum[length] == 2)
                first_i = length;
            if (sum[length] == 4)
                last_j = length;
        }
        printf("Case #%d: %s\n", t, first_i > 0 && first_i < last_j && sum[length-1] == 8 ? "YES" : "NO");
    }
    return 0;
}

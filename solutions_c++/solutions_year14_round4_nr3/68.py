#include <cstdio>
#include <algorithm>
using namespace std;

const int N = 1050;
int X1[N], Y1[N], X2[N], Y2[N];
int A[N][N];

inline int dist(int y, int x, int i)
{
    if (y >= Y1[i] && y <= Y2[i] && x >= X1[i] && x <= X2[i])
        return 0;
    if (y >= Y1[i] && y <= Y2[i])
        return min(abs(x - X1[i]), abs(x - X2[i]));
    if (x >= X1[i] && x <= X2[i])
        return min(abs(y - Y1[i]), abs(y - Y2[i]));
    return max(min(abs(x - X1[i]), abs(x - X2[i])), min(abs(y - Y1[i]), abs(y - Y2[i])));
}

inline int dist(int i, int j)
{
    int ans = 1e9;
    for (int it = 0; it < 2; it++)
    {
        swap(i, j);
        ans = min(ans, dist(Y1[i], X1[i], j));
        ans = min(ans, dist(Y1[i], X2[i], j));
        ans = min(ans, dist(Y2[i], X1[i], j));
        ans = min(ans, dist(Y2[i], X2[i], j));
    }
    return ans;
}

void solve(int cs)
{
    int n, w, h;
    scanf("%d %d %d", &w, &h, &n);
    X1[0] = -1, Y1[0] = 0, X2[0] = 0, Y2[0] = h;
    X1[1] = w, Y1[1] = 0, X2[1] = w + 1, Y2[1] = h;
    n += 2;
    for (int i = 2; i < n; i++)
        scanf("%d %d %d %d", &X1[i], &Y1[i], &X2[i], &Y2[i]), X2[i]++, Y2[i]++;

    for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++)
            A[i][j] = (i == j) ? 0 : dist(i, j);
    for (int k = 0; k < n; k++)
        for (int i = 0; i < n; i++)
            for (int j = 0; j < n; j++)
                A[i][j] = min(A[i][j], A[i][k] + A[k][j]);
    printf("Case #%d: %d\n", cs, A[0][1]);
}

int main()
{
    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; i++)
        solve(i + 1), fflush(stdout);
}

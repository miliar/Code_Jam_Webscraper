#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

const int N = 101;
struct node
{
    int x, y, z;
} b[N * N];
int a[N][N];

bool cmp(const node &a, const node &b)
{
    return a.z < b.z;
}

int main()
{
    int T, n, m, k;
    bool q1, q2, ans;
    
    //freopen("input.txt", "r", stdin);
    freopen("B-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        scanf("%d%d", &n, &m);
        k = 0;
        for (int i = 0; i < n; ++i)
            for (int j = 0; j < m; ++j)
            {
                scanf("%d", &a[i][j]);
                b[k].x = i;
                b[k].y = j;
                b[k++].z = a[i][j];
            }
        sort(b, b + k, cmp);
        ans = true;
        for (int i = 0; i < k; ++i)
        {
            q1 = q2 = true;
            for (int j = 0; j < n; ++j)
                if (a[j][b[i].y] > b[i].z) q1 = false;
            for (int j = 0; j < m; ++j)
                if (a[b[i].x][j] > b[i].z) q2 = false;      
            if (!q1 && !q2) ans = false;
        }
        printf("Case #%d: ", cas);
        if (ans) printf("YES\n");
        else printf("NO\n");
    }
    return 0;
}

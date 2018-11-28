#include <cstdio>
#include <cstring>
using namespace std;
#define NUM 105

char str[NUM][NUM], all[NUM * NUM];
int len[NUM], tmp[NUM];
int T, N, ans;
bool u[26], v[NUM];

void dfs(int d, int x)
{
    if (d > N)
    {
        memset(u, false, sizeof(u));
        u[all[0] - 'a'] = true;
        bool ok = true;
        for (int i = 1; all[i]; i++)
            if (all[i - 1] != all[i])
            {
                if (u[all[i] - 'a'])
                {
                    ok = false;
                    break;
                } else
                    u[all[i] - 'a'] = true;
            }
        if (ok)
            ans++;
        return;
    }
    for (int i = 1; i <= N; i++)
        if (!v[i])
        {
            v[i] = true;
            tmp[d] = i;
            strcpy(all + x, str[i]);
            dfs(d + 1, x + len[i]);
            v[i] = false;
        }
}

int main()
{
    freopen("input.txt", "r", stdin);
    freopen("output.txt", "w",stdout);
    scanf("%d", &T);
    for (int x = 1; x <= T; x++)
    {
        scanf("%d", &N);
        for (int i = 1; i <= N; i++)
        {
            scanf("%s", str[i]);
            len[i] = strlen(str[i]);
        }
        ans = 0;
        memset(v, false, sizeof(v));
        dfs(1, 0);
        printf("Case #%d: %d\n", x, ans % 1000000007);
    }
    return 0;
}

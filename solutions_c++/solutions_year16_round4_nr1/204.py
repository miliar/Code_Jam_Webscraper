#include <iostream>

using namespace std;
bool can;
bool check()
{
    for (int j = n; j; j /= 2)
    {
        for (int i = 0; i < n; ++i)
        {
            state[i] = state[i] ^ state[i + 1];
        }
    }
    return state[i / n];
}
void dfs(int index)
{
    if (can) return;
    for (int i = 0; i < 3; ++i)
    {
        if (can) break;
        if (num[i] == 0) continue;
        state[index] = i;
        num[i]--;
        if (index == n)
            check();
        else
            dfs(index + 1);
        num[i]++;
    }
}
int main()
{
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        can = false;
        scanf("%d%d%d%d", &n, &num[1], &num[0], &num[2]);
        n = 1 << n;
        dfs(1);
        printf("%s\n", ans);
    }
    return 0;
}

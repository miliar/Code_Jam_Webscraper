#include<iostream>
#include<cstdio>
#include<cstring>
#define LL long long
using namespace std;

int N,T,kase = 0;
bool vis[15];

bool check(int x)
{
    while (x > 0)
    {
        vis[x % 10] = true;
        x = x / 10;
    }
    int i;
    for (i = 0; i <= 9; i++)
        if (!vis[i]) return false;
    return true;
}

int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    cin >> T;
    while (T--)
    {
        cin >> N;
        if (N == 0)
        {
            printf("Case #%d: INSOMNIA\n", ++kase);
            continue;
        }
        memset(vis, 0, sizeof(vis));
        int i;
        for (i = 1; i <= 100; i++)
            if (check(i * N))
        {
            printf("Case #%d: %d\n", ++kase, i * N);
            break;
        }
    }
    return 0;
    fclose(stdin);
    fclose(stdout);
}

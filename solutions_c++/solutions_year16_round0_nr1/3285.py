#include <bits/stdc++.h>
using namespace std;
bool used[10];
void add(int x)
{
    if (x == 0)
    {
        used[0] = true;
    }
    else
    {
        while(x > 0)
        {
            used[x % 10] = true;
            x /= 10;
        }
    }
}
bool check()
{
    for(int i = 0; i < 10; i++)
    {
        if (!used[i]) return false;
    }
    return true;
}
int main()
{
    freopen("a.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    int t;
    scanf("%d", &t);
    for (int tt = 1; tt <= t; tt++)
    {
        for (int i = 0; i < 10; i++)
        {
            used[i] = false;
        }
        int n;
        scanf("%d", &n);
        int ans = -1;
        int cur = n;
        for (int it = 0; it < 1000; it++)
        {
            add(cur);
            if (check())
            {
                ans = cur;
                break;
            }
            cur += n;
        }
        if (ans == -1)
        {
            printf("Case #%d: INSOMNIA\n", tt);
        }
        else
        {
            printf("Case #%d: %d\n", tt, ans);
        }
        cerr << tt << endl;
    }
}

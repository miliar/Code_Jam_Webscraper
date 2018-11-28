#include <iostream>
#include <cstdio>
#include <string.h>

using namespace std;
char s[109];
int ti[2000], q[2000], l;
bool v[2000];
int change(int x, int len)
{
    bool state[20] = {false};
    int tx = x;
    for (int i = 0; i < l; ++i)
    {
        state[i] = tx % 2;
        tx /= 2;
    }
    bool h[20] = {false};
    for (int i = l - 1; i >= l - len; --i)
    {
        if (h[2 * l - len - 1 - i]) break;
        h[i] = true;
        state[i] ^= 1;
        if (i != 2 * l - len - 1 - i)
        state[2 * l - len - 1 - i] ^= 1;
        swap(state[i], state[2 * l - len - 1 - i]);
    }
    tx = 0;
    for (int i = l - 1; i >= 0; --i)
    {
        tx = tx * 2 + state[i];
    }
    return tx;

}
int main()
{
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
    int T;
    cin >> T;
    for (int cas = 1; cas <= T; ++cas)
    {
        printf("Case #%d: ", cas);
        scanf("%s", s);
        int state = 0,ans = 0;
        for (int i = 0; s[i]; ++i)
        {
            state = state * 2 + (s[i] == '-');
        }
        int top = 1, tail = 1;
        l = strlen(s);
        memset(v, false, sizeof(v));
        memset(ti, 0, sizeof(ti));
        q[top] = state;
        v[state] = 1;
        while (top <= tail)
        {
            int now = q[top];
            if (now == 0)
            {
                ans = ti[now];
                break;
            }
            top++;
            for (int i = 1; i <= l; ++i)
            {
                int statenow = change(now, i);
                if (!v[statenow])
                {
                    v[statenow] = true;
                    q[++tail] = statenow;
                    ti[statenow] = ti[now] + 1;
                }
            }
        }
        printf("%d\n", ans);
    }
    return 0;
}

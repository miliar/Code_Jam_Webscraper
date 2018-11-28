#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int f[1030], list[1030];

int flip(int x, int k)
{
    int mask((1<<(k+1))-1);
    x = ~(x & mask) & mask | (x & ~mask);
    for (int k1=(1<<k), p1=k, k2=1, p2=0; k1>k2; k1>>=1, p1--, k2<<=1, p2++)
    {
        int t1(x & k1), t2(x & k2);
        t1 >>= p1 - p2;
        t2 <<= p1 - p2;
        x = (x & ~k1 & ~k2 | t1 | t2);
    }
    return x;
}

int main()
{
    freopen("b.in", "r", stdin);
    freopen("b.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int tt=1; tt<=T; tt++)
    {
        char s[15];
        scanf("%s", s);
        int n = strlen(s);
        memset(f, 255, sizeof f);
        int st=1, en=1, cur=0;
        for (int i=n-1; i>=0; i--)
            cur = (cur<<1) + (s[i]=='-');
        list[1] = cur;
        f[cur] = 0;
        for (; st<=en && !~f[0]; st++)
        {
            int cur(list[st]);
            for (int i=0; i<n && !~f[0]; i++)
            {
                int next(flip(cur, i));
                if (~f[next]) continue;
                f[next] = f[cur] + 1;
                list[++en] = next;
            }
        }
        printf("Case #%d: %d\n", tt, f[0]);
    }
    return 0;
}


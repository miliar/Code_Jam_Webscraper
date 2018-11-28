#include<iostream>
#include<cstring>
#include<cstdio>
#include<algorithm>
#include<fstream>
using namespace std;
char s[1010];
int h[1010];
int main()
{
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
    int T, p, cur, ans, i, k, l;
    scanf("%d", &T);
    for(int cas = 1; cas <= T; ++cas)
    {
        scanf("%s%d", s + 1, &k);
        l = strlen(s + 1);
        memset(h, 0, sizeof(h));
        cur = 0;
        ans = 0;
        for(i = 1; i <= l - k + 1; ++i)
        {
            if(s[i] == '-' && cur % 2 == 0)
            {
                ans++;
                cur++;
                h[i + k - 1]++;
            }else
            if(s[i] == '+' && cur % 2 == 1)
            {
                ans++;
                cur++;
                h[i + k - 1]++;
            }
            cur -= h[i];
        }
        p = 0;
        for(i = l - k + 2; i <= l; ++i)
        {
            if(s[i] == '-' && cur % 2 == 0 || s[i] == '+' && cur % 2 == 1)
            {
                p = 1;
                break;
            }
            cur -=  h[i];
        }
        printf("Case #%d: ", cas);
        if(p)
            puts("IMPOSSIBLE");
        else
            printf("%d\n", ans);
    }
    return 0;
}

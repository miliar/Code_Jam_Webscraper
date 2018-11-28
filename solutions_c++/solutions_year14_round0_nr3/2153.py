//#pragma comment(linker, "/STACK:1024000000,1024000000")
#include<algorithm>
#include<iostream>
#include<cstring>
#include<cstdio>
#include<vector>
#include<queue>
#include<stack>
#include<set>
#include<map>
#define LL long long
#define lson l, m, rt << 1
#define rson m + 1, r, rt << 1|1
#define CLR(a, b) memset(a, b, sizeof(a))
using namespace std;
const int maxn = 70;

char ch[maxn][maxn];

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int r, c, m, T, cas = 1;
    scanf("%d", &T);
    while(T --)
    {
        scanf("%d%d%d", &r, &c, &m);
        int mm = m;
        printf("Case #%d:\n", cas ++);
        if(r == 1)
        {
            for(int i = 1; i <= m; i ++) putchar('*');
            for(int i = m + 1; i < c; i ++) putchar('.');
            puts("c");
            continue;
        }
        if(c == 1)
        {
            for(int i = 1; i <= m; i ++) puts("*");
            for(int i = m + 1; i < r; i ++) puts(".");
            puts("c");
            continue;
        }
        if(r * c == m + 1)
        {
            putchar('c');
            for(int i = 0; i < r; i ++)
            {
                for(int j = 0; j < c; j ++)
                    if(i||j) putchar('*');
                puts("");
            }
            continue;
        }
        if(c == 2)
        {
            if(m & 1) puts("Impossible");
            else
            {
                if(m / 2 > r - 2) puts("Impossible");
                else
                {
                    for(int i = 1; i <= m / 2; i ++)
                        puts("**");
                    for(int i = m / 2 + 1; i < r; i ++)
                        puts("..");
                    puts(".c");
                }
            }
            continue;
        }
        if(r == 2)
        {
            if(m & 1) puts("Impossible");
            else
            {
                if(m / 2 > c - 2) puts("Impossible");
                else
                {
                    for(int i = 1; i <= m / 2; i ++)
                        printf("*");
                    for(int i = m / 2 + 1; i < c; i ++)
                        printf(".");
                    puts(".");
                    for(int i = 1; i <= m / 2; i ++)
                        printf("*");
                    for(int i = m / 2 + 1; i < c; i ++)
                        printf(".");
                    puts("c");
                }
            }
            continue;
        }
        bool flag = true;
        CLR(ch, 0);
        for(int i = 1; i <= r; i ++)
            for(int j = 1; j <= c; j ++) ch[i][j] = '.';
        for(int i = 1; i <= r - 2; i ++)
            for(int j = 1; j <= c; j ++)
            {
                if(m)
                {
                    ch[i][j] = '*';
                    m --;
                }
            }
        if(!m)
        {
            int rn = mm / c, cn = mm % c; if(cn) rn ++;
            if(cn == c - 1)
            {
                if(rn == r - 2)
                {
                    if(c < 4) flag = false;
                    ch[r - 2][c - 2] = ch[r - 2][c - 1] = '.';
                    ch[r - 1][1] = ch[r][1] = '*';
                }
                else
                {
                    ch[rn][cn] = '.';ch[rn + 1][1] = '*';
                }
            }
        }
        else
        {
            if(m & 1)
            {
                if(c == 3 || c == 4)flag = false;///
                else
                {
                    m += 3;
                    for(int i = c; i > c - 3; i --)
                        ch[r-2][i] = '.';
                    if(m / 2 > c - 3) flag = false;
                    else
                    {
                        for(int i = 1; i <= m / 2; i ++)
                            ch[r][i] = ch[r - 1][i] = '*';
                    }
                }
            }
            else
            {
                if(m / 2 > c - 2) flag = false;
                else
                {
                    for(int i = 1; i <= m / 2; i ++)
                        ch[r][i] = ch[r - 1][i] = '*';
                }
            }
        }
        if(!flag) puts("Impossible");
        else
        {
            ch[r][c] = 'c';
            for(int i = 1; i <= r; i ++)
            {
                for(int j = 1; j <= c; j ++)
                    putchar(ch[i][j]);
                puts("");
            }
        }
    }
}

#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

#define INF 2000000000

int T, L, X;

int mul(int x, int y)
{
    int sign = 1;
    if( x < 0 ) x *= -1, sign *= -1;
    if( y < 0 ) y *= -1, sign *= -1;

    int re = 0;

    if( x == 1 ) re = y;
    else if( y == 1 ) re = x;
    else if( x == 2 )
    {
        if( y == 2 ) re = -1;
        else if( y == 3 ) re = 4;
        else re = -3;
    }
    else if( x == 3 )
    {
        if( y == 3 ) re = -1;
        else if( y == 4 ) re = 2;
        else re = -4;
    }
    else if( x == 4 )
    {
        if( y == 4 ) re = -1;
        else if( y == 2 ) re = 3;
        else re = -2;
    }

    return re*sign;
}

char c[20000];

int main()
{
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);

    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%d %d", &L, &X);
        scanf("%s", c);

        printf("Case #%d: ", Ti);

        int bk = 1;

        for(int Li = 0; Li < L; Li++)
            bk = mul(bk, c[Li]-'i'+2);

        int now;
        bool OK;

        int lef1 = 1, cnt1 = 0, pt1;
        now = 1; OK = false;

        for(int Xi = 1; Xi <= 4 && !OK; Xi++, cnt1++)
            for(int Li = 0; Li < L; Li++)
            {
                if( OK ) lef1 = mul(lef1, c[Li]-'i'+2);
                else
                {
                    now = mul(now, c[Li]-'i'+2);
                    if( now == 2 )
                    {
                        OK = true;
                        pt1 = Li;
                    }
                }
            }

        if( !OK )
        {
            puts("NO");
            continue;
        }

        int lef2 = 1, cnt2 = 0, pt2;
        now = 1; OK = false;

        for(int Xi = 1; Xi <= 4 && !OK; Xi++, cnt2++)
            for(int Li = L-1; Li >= 0; Li--)
            {
                if( OK ) lef2 = mul(c[Li]-'i'+2, lef2);
                else
                {
                    now = mul(c[Li]-'i'+2, now);
                    if( now == 4 )
                    {
                        OK = true;
                        pt2 = Li;
                    }
                }
            }

        if( cnt1+cnt2 > X+1 ) OK = false;
        else if( cnt1+cnt2 == X+1 )
        {
            int p = 1;

            for(int i = pt1+1; i < pt2; i++)
                p = mul(p, c[i]-'i'+2);

            if( p != 3 ) OK = false;
        }
        else
        {
            int t = X-cnt1-cnt2;
            t %= 4;

            int p = lef1;

            for(int i = 0; i < t; i++)
                p = mul(p, bk);

            p = mul(p, lef2);

            if( p != 3 ) OK = false;
        }

        if( OK ) puts("YES");
        else puts("NO");
    }
}

#include<bits/stdc++.h>
#define ll long long

using namespace std;
ll x, r, c, t, T, a, b;
int main()
{
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    scanf("%lld", &t);
    for(T = 1; T <= t; T++)
    {
        cin >> x >> r >> c;
        a = r * c;
        if(x == 1)
        {
            printf("Case #%d: GABRIEL\n", T);
            continue;
        }
        if(x == 2)
        {
            if(a % 2 == 0)
                printf("Case #%d: GABRIEL\n", T);
            else
                printf("Case #%d: RICHARD\n", T);
            continue;
        }
        if(x == 3)
        {
            if(a % 3 != 0)
            {
                printf("Case #%d: RICHARD\n", T);
                continue;
            }
            if(r == 3)
                swap(r, c);
            if(r == 1)
                printf("Case #%d: RICHARD\n", T);
            else
                printf("Case #%d: GABRIEL\n", T);
            continue;
        }
        if(a % 4 != 0)
            printf("Case #%d: RICHARD\n", T);
        else
        {
            if(r == 2 && c == 2)
                printf("Case #%d: RICHARD\n", T);
            else
            {
                if(r == 4)
                   swap(r,c);
                if(r == 1 || r == 2)
                    printf("Case #%d: RICHARD\n", T);
                else printf("Case #%d: GABRIEL\n", T);
            }
        }


    }
    return 0;
}



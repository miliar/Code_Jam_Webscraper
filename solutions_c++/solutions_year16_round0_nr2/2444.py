#include <iostream>
#include <cstring>
#include <cstdio>

using namespace std;

char s[200]; int sn;

int main()
{
    freopen("B_large.in", "r", stdin);
    freopen("B_large.out", "w", stdout);

    int T;
    scanf("%d", &T);

    for(int Ti = 1; Ti <= T; Ti++)
    {
        scanf("%s", s);
        sn = strlen(s);

        s[sn] = '+';

        int cnt = 0;
        for(int si = 0; si < sn; si++)
            if( s[si] != s[si+1] ) cnt++;

        printf("Case #%d: %d\n", Ti, cnt);
    }
}

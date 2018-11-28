// vim:set sw=4 et smarttab:
// Round 1C 2013

#include <cstdio>
#include <cstring>
#include <cassert>

char name[1000001];
int n;

bool iscon(char c)
{
    return !(c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u');
}

long long solve()
{
    int l = strlen(name);
    int last_con = -1;
    int current = 0;
    long long ret = 0;
    for (int i = 0; i < l; ++i)
    {
        if (iscon(name[i]))
        {
            ++current;
            if (current >= n)
            {
                current = n - 1;
                last_con = i - current;
            }
        }
        else
            current = 0;
        if (last_con != -1)
        {
            //printf("DEBUG %d %d\n", i, last_con);
            ret += last_con + 1;
        }
    }
    return ret;
}

/*
    int st = 0;
    int en = 0;
    int nc = 0;
    long long ret = 0;
    while (name[en] != '\0')
    {
        if (iscon(name[en]))
            ++nc;
        if (nc == n)
        {
            printf("DEBUG %d %d\n", st, en);
            ret += st + 1;
            assert(iscon(name[st]));
            ++st;
            --nc;
        }
        ++en;
        while (st < en && !iscon(name[st]))
            ++st;
    }
    return ret;
}
*/

int main()
{
    int ntc;
    scanf("%d", &ntc);
    for (int tc = 1; tc <= ntc; ++tc)
    {
        scanf("%s%d", name, &n);
        long long answer = solve();
        printf("Case #%d: %lld\n", tc, answer);
    }
}

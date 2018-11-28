// CodeJam2.cpp : Defines the entry point for the console application.
//

//#include "stdafx.h"
#include <cstdio>
#include <cstring>
using namespace std;
int main()
{
    freopen("B-large.in", "r", stdin);
    freopen("B-large.out", "w", stdout);

    int T;
    char s[110];
    int ans;

    scanf("%d", &T);
    for (int kase = 1; kase <= T; ++kase)
    {
        scanf("%s", s);
        ans = 0;
        int i = strlen(s) - 1;
        while (i >= 0 && s[i] == '+') --i;
        if (i >= 0)
            ans += 1;
        for (; i > 0; --i)
        {
            if (s[i] == s[i - 1])
                continue;
            ans += 1;
        }
        printf("Case #%d: %d\n", kase, ans);
    }
    fclose(stdin);
    fclose(stdout);
    return 0;
}


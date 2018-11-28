#include "stdafx.h"

#include <stdio.h>
#include <string.h>
#include <algorithm>

using namespace std;

void ovation()
{
    int T, Smax;
#ifdef DEV_MODE
    freopen("A-large.in.txt", "r", stdin);
#endif
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t)
    {
        scanf("%d ", &Smax);
        int friends = 0, standing = 0;
        for (int S = 0; S <= Smax; ++S)
        {
            char d;
            scanf("%c", &d);
            for (int i = 0; i < d - '0'; ++i)
                friends = max(friends, S - standing++);
        }
        printf("Case #%d: %d\n", t, friends);
    }
}

#ifndef DEV_MODE
int main(int argc, char* argv[])
{
    ovation();
    return 0;
}
#endif

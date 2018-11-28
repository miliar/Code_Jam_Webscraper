/**
 * Copyright (c) 2013 Authors. All rights reserved.
 * 
 * FileName: C.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2013-04-13
 */
#include <cstdio>
#include <algorithm>
#include <cstring>

using namespace std;

const int INF = 0x3f3f3f3f;
const int SIZE = 23;
const int list[SIZE] = {0, 1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944,
        1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121,
        123454321, 125686521, 400080004, 404090404, INF};

int f(int x)
{
        return upper_bound(list, list + SIZE, x) - list;
}

int main()
{
        //freopen("C-small-attempt0.in", "r", stdin);
        //freopen("C-small-attempt0.out", "w", stdout);

        int T, cas = 0;

        scanf("%d", &T);

        while (T--) {
                char x[105], y[105];
                int l, h;

                scanf("%s%s", x, y);

                if (strlen(x) > 9)
                        l = 500000000;
                else
                        sscanf(x, "%d", &l);

                if (strlen(y) > 9)
                        h = 500000000;
                else
                        sscanf(y, "%d", &h);

                printf("Case #%d: %d\n", ++cas, f(h) - f(l - 1));
        }

        return 0;
}

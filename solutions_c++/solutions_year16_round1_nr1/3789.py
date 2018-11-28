/**
 * Copyright © 2016 Authors. All rights reserved.
 * 
 * FileName: A.cpp
 * Author: Beiyu Li <sysulby@gmail.com>
 * Date: 2016-04-16
 */
#include <bits/stdc++.h>

using namespace std;

#define rep(i,n) for (int i = 0; i < (n); ++i)
#define For(i,s,t) for (int i = (s); i <= (t); ++i)
#define foreach(i,c) for (__typeof(c.begin()) i = c.begin(); i != c.end(); ++i)

typedef long long LL;
typedef pair<int, int> Pii;

const int inf = 0x3f3f3f3f;
const LL infLL = 0x3f3f3f3f3f3f3f3fLL;

const int maxn = 1000 + 5;

char s[maxn];

int main()
{
        int T, cas = 0;
        scanf("%d", &T);

        while (T--) {
                scanf("%s", s);
                string ret;
                for (int i = 0; s[i]; ++i)
                        ret = max(s[i] + ret, ret + s[i]);
                printf("Case #%d: %s\n", ++cas, ret.c_str());
        }

        return 0;
}

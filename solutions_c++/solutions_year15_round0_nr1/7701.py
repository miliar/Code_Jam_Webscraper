//
//
//
//  Created by TaoSama on 2015-04-11
//  Copyright (c) 2015 TaoSama. All rights reserved.
//
#include <algorithm>
#include <cctype>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iomanip>
#include <iostream>
#include <map>
#include <queue>
#include <string>
#include <set>
#include <vector>

using namespace std;
const int INF = 0x3f3f3f3f;
const int MOD = 1e9 + 7;
const int N = 1e5 + 10;

char a[1005];

int main() {
#ifdef LOCAL
    freopen("in.txt", "r", stdin);
    freopen("out.txt", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);

    int kase = 0;
    int t; scanf("%d", &t);
    while(t--) {
        int n; scanf("%d%s", &n, a);

        int ans = 0, cur = a[0] - '0';
        for(int i = 1; i <= n; ++i) {
            if(a[i] - '0' > 0) {
                if(i > cur) {
                    ans += i - cur;
                    cur += i - cur;
                }
                cur += a[i] - '0';
            }
        }
        printf("Case #%d: %d\n", ++kase, ans);
    }
    return 0;
}

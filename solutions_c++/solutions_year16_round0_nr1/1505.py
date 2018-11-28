//
//  Created by TaoSama on 2016-04-09
//  Copyright (c) 2016 TaoSama. All rights reserved.
//
#pragma comment(linker, "/STACK:102400000,102400000")
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
#include <cassert>
#include <string>
#include <set>
#include <vector>

using namespace std;
#define pr(x) cout << #x << " = " << x << "  "
#define prln(x) cout << #x << " = " << x << endl
const int N = 1e5 + 10, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int n;

int main() {
#ifdef LOCAL
    freopen("A-large.in", "r", stdin);
    freopen("A-large.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);

    int t; scanf("%d", &t);
    while(t--) {
        scanf("%d", &n);
        static int kase = 0;
        if(!n) {printf("Case #%d: INSOMNIA\n", ++kase); continue;}

        int ans = n;
        set<int> s;
        while(true) {
            char buf[100]; sprintf(buf, "%d", ans);
            for(int i = 0; buf[i]; ++i) s.insert(buf[i] - '0');
            if(s.size() == 10) break;
            ans += n;
        }
        printf("Case #%d: %d\n", ++kase, ans);
    }
    return 0;
}

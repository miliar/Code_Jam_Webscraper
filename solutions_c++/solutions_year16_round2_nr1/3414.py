//
//  Created by TaoSama on 2016-04-30
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
#include <string>
#include <set>
#include <vector>

using namespace std;
#define pr(x) cout << #x << " = " << x << "  "
#define prln(x) cout << #x << " = " << x << endl
const int N = 1e5 + 10, INF = 0x3f3f3f3f, MOD = 1e9 + 7;

int cnt[26];
char s[N];
char digit[][10] = {"ZERO", "ONE", "TWO", "THREE", "FOUR", "FIVE", "SIX", "SEVEN", "EIGHT", "NINE"};

void dfs(int lft, int u, string& ans) {
    if(!lft) {
        puts(ans.c_str());
        throw 1;
    }
    for(int i = u, j; i < 10; ++i) {
        bool ok = true;
        for(j = 0; digit[i][j]; ++j) {
            if(--cnt[digit[i][j] - 'A'] < 0)
                ok = false;
        }
        ans += char(i + '0');
        if(ok) dfs(lft - j, i, ans);
        ans.pop_back();
        for(j = 0; digit[i][j]; ++j)
            ++cnt[digit[i][j] - 'A'];
    }
}

int main() {
#ifdef LOCAL
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
#endif
    ios_base::sync_with_stdio(0);

    int t; scanf("%d", &t);
    while(t--) {
        scanf("%s", s + 1);
        memset(cnt, 0, sizeof cnt);
        int n = strlen(s + 1);
        for(int i = 1; s[i]; ++i) cnt[s[i] - 'A']++;
        string ans;
        static int kase = 0;
        printf("Case #%d: ", ++kase);
        try {
            dfs(n, 0, ans);
        } catch(int) {}
    }
    return 0;
}

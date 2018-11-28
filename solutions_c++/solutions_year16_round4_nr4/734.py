/*
 * $File: brute.cpp
 * $Date: Sun May 29 00:20:49 2016 +0800
 * $Author: jiakai <jia.kai66@gmail.com>
 */

#include <cstdio>
#include <algorithm>
#include <vector>
#include <utility>
#include <iostream>
#include <string>
#include <tuple>
#include <cstring>

namespace solve {

    int m2w[4], w2m[4], N, min_cost = 1000000;
    std::vector<std::pair<int, int>> to_test;

    void dfs(size_t pos, int cost) {
        if (pos == to_test.size()) {
            bool good = true;
            for (int w = 0; w < N; ++ w) {
                int compete = 0, nr_m = 0;
                for (int m = 0; m < N; ++ m) {
                    if (w2m[w] & (1 << m)) {
                        compete |= m2w[m];
                        ++ nr_m;
                    }
                }
                compete &= ~(1 << w);
                int nr_comp = 0;
                for (int i = 0; i < 4; ++ i)
                    nr_comp += (compete >> i) & 1;
                if (nr_comp >= nr_m) {
                    good = false;
                    break;
                }
            }
            if (good)
                min_cost = std::min(cost, min_cost);
            return;
        }
        dfs(pos + 1, cost);
        int w, m;
        std::tie(w, m) = to_test[pos];
        int bk_m2w = m2w[m], bk_w2m = w2m[w];
        m2w[m] |= 1 << w;
        w2m[w] |= 1 << m;
        dfs(pos + 1, cost + 1);
        m2w[m] = bk_m2w;
        w2m[w] = bk_w2m;
    }

    void solve() {
        int T;
        using std::cin;
        cin >> T;
        for (int tcase = 0; tcase < T; ++ tcase) {
            min_cost = 10000000;
            cin >> N;
            to_test.clear();
            memset(m2w, 0, sizeof(m2w));
            memset(w2m, 0, sizeof(w2m));
            for (int i = 0; i < N; ++ i) {
                std::string s;
                cin >> s;
                for (int j = 0; j < N; ++ j){
                    if (s[j] == '1') {
                        w2m[i] |= 1 << j;
                        m2w[j] |= 1 << i;
                    } else {
                        to_test.emplace_back(i, j);
                    }
                }
            }
            dfs(0, 0);
            printf("Case #%d: %d\n", tcase + 1, min_cost);
        }
    }
}

int main() {
    solve::solve();
}

// vim: syntax=cpp.doxygen foldmethod=marker foldmarker=f{{{,f}}}


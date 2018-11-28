#include <bits/stdc++.h>
using namespace std;

int T, N;
char buf1[20000];
char buf2[10000];

vector<string> words[202];

int main() {
    freopen("C-small-attempt0.in", "r", stdin);
    freopen("C-small-attempt0.out", "w", stdout);
    int T;
    scanf("%d", &T);
    for (int t = 1; t <= T; ++t) {
        scanf("%d\n", &N);
        for (int i = 0; i < N; ++i) {
            gets(buf1);
            words[i].clear();
            int k = 0;
            for (int j = 0; buf1[j]; ++j) {
                if (buf1[j] == ' ') {
                    if (k > 0) {
                            buf2[k] = 0;
                    words[i].push_back(buf2);
                    }
                    k = 0;
                } else {
                    buf2[k++] = buf1[j];
                }
            }
            if (k > 0) {
                    buf2[k] = 0;
                words[i].push_back(buf2);
            }
        }
        int ans = 0x3f3f3f3f;
        for (int i = 0; i < (1 << N); ++i) {
            if ((i & 3) != 2) {
                continue;
            }
            set<string> s1, s2;
            for (int j = 0; j < N; ++j) {
                if (i & (1<<j)) {
                    for (auto word : words[j]) {
                        s1.insert(word);
                    }
                } else {
                    for (auto word : words[j]) {
                        s2.insert(word);
                    }
                }
            }
            int cnt = 0;
            for (auto s : s1) {
                if (s2.find(s) != s2.end()) {
                    ++cnt;
                }
            }
            ans = min(ans, cnt);
        }
        printf("Case #%d: %d\n", t, ans);
    }
    return 0;
}

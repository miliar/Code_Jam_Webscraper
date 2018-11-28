#include <cstdio>
#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <cstdlib>
#include <string.h>

using namespace std;

const int N = 13;
int ans[3][N + 1][1 << (N + 1)];
const char imp[] = "IMPOSSIBLE";
char str[1 << (N + 1)];

void solve(int n, int r, int p, int s) {
    int cnt[3][3] = {0};
    for (int i = 0; i < 3; ++i) {
        for (int j = 0; j < (1 << n); ++j) {
            ++cnt[i][ans[i][n][j]];
        }
    }
    pair<int, char> seq[3];
    seq[0] = make_pair(p, 'P');
    seq[1] = make_pair(r, 'R');
    seq[2] = make_pair(s, 'S');
    vector<string> ansStr;
    for (int i = 0; i < 3; ++i) {
        bool same = true;
        for (int j = 0; j < 3; ++j) {
            if (seq[j].first != cnt[i][j]) {
                same = false;
                break;
            }
        }
        if (same) {
            for (int j = 0; j < (1 << n); ++j) {
                str[j] = seq[ans[i][n][j]].second;
            }
            ansStr.push_back(string(str, str + (1 << n)));
        }
    }
    if (ansStr.empty()) {
        memcpy(str, imp, sizeof(imp));
    } else {
        sort(ansStr.begin(), ansStr.end());
        memcpy(str, ansStr[0].c_str(), 1 << n);
        str[1 << n] = '\0';
    }
}

void srt(int num, int s[]) {
    if (num <= 1) {
        return;
    }
    int half = num >> 1;
    srt(half, s);
    srt(half, s + half);
    for (int i = 0; i < half; ++i) {
        if (s[i] > s[i + half]) {
            for (int j = 0; j < half; ++j) {
                swap(s[j], s[j + half]);
            }
            return;
        } else if (s[i] < s[i + half]) {
            break;
        }
    }
}

int main() {
    for (int l = 0; l < 3; ++l) {
        ans[l][0][0] = l;
        for (int i = 0; i < N; ++i) {
            for (int j = 0; j < (1 << i); ++j) {
                int a = j * 2, b = j * 2 + 1;
                int v1 = ans[l][i][j];
                int v2 = (ans[l][i][j] + 1) % 3;
                ans[l][i + 1][a] = min(v1, v2);
                ans[l][i + 1][b] = max(v1, v2);
            }
            srt(1 << (i + 1), ans[l][i + 1]);
        }
    }

    int T;
    scanf("%d", &T);
    for (int i = 0; i < T; ++i) {
        int n, r, p, s;
        scanf("%d%d%d%d", &n, &r, &p, &s);
        /*
         * solve here
         */
        solve(n, r, p, s);
        printf("Case #%d: %s", (i + 1), str);
        
        /*
         * print here
         */
        
        if (i + 1 < T) {
            printf("\n");
        }
    }
    return 0;
}
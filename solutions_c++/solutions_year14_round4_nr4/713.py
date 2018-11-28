#include <iostream>
#include <stdio.h>
#include <algorithm>
#include <string>

using namespace std;

int N, M, T, ans1, ans2;
string str[8];
int trieSize[4];
int node[4][90][26];

void add(int cur, string s) {
    int now = 0;
    for(int i = 0; i < s.size(); i++) {
        if (node[cur][now][s[i] - 'A'] == -1) {
            node[cur][now][s[i] - 'A'] = trieSize[cur];
            trieSize[cur]++;
        }
        now = node[cur][now][s[i] - 'A'];
    }
}

void solve(int cur) {
    if (cur == M) {
        int cnt = 0;
        for(int i = 0; i < N; i++)
            if (trieSize[i] > 1)
                cnt += trieSize[i];
        if (ans1 == -1 || cnt > ans1) {
            ans1 = cnt;
            ans2 = 1;
        } else if (cnt == ans1) {
            ans2++;
        }
        return;
    }
    int tmp[90][26];
    for(int i = 0; i < N; i++) {
        int tmpSize = trieSize[i];
        memcpy(tmp, node[i], sizeof(tmp));
        add(i, str[cur]);
        solve(cur + 1);
        trieSize[i] = tmpSize;
        memcpy(node[i], tmp, sizeof(tmp));
    }
}

int main() {
    freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small-attempt1.out", "w", stdout);
    cin >> T;
    for(int t = 1; t <= T; t++) {
        cin >> M >> N;
        for(int i = 0; i < M; i++)
            cin >> str[i];
        for(int i = 0; i < N; i++) {
            trieSize[i] = 1;
            memset(node, -1, sizeof(node));
        }
        ans1 = -1;
        solve(0);
        cout << "Case #" << t << ": " << ans1 << " " << ans2 << endl;
    }
    return 0;
}

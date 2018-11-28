#include <bits/stdc++.h>
using namespace std;

const int N = 205;
const int M = 2000 + N * 10;
int T, n, mark[M];
vector<int> v[N];
map<string,int> mp;

int idx(const char *s) {
    auto it = mp.find(s);
    if (it == mp.end()) {
        int id = mp.size();
        mp.insert(make_pair(s, id));
        return id;
    }
    return it->second;
}
int main() {
    scanf("%d", &T);
    for (int cas = 1; cas <= T; ++cas) {
        fprintf(stderr, "case %d\n", cas);
        mp.clear();
        scanf("%d", &n);
        for (int i = n-1; i >= 0; --i) {
            v[i].clear();
            char s[15], c;
            while (1) {
                scanf("%s%c", s, &c);
                v[i].push_back(idx(s));
                if (c == '\n') break;
            }
        }
        vector<int> mark(mp.size());
        for (int i = 1; i <= 2; ++i) {
            for (auto x : v[n-i]) {
                mark[x] |= i;
            }
        }
        n -= 2;
        int ans = mp.size();
        for (int msk = 0; msk < (1 << n); ++msk) {
            vector<int> temp = mark;
            for (int i = 0; i < n; ++i) {
                int b = ((msk >> i) & 1) + 1;
                for (auto x : v[i]) {
                    temp[x] |= b;
                }
            }
            int cnt = 0;
            for (auto x : temp) cnt += x == 3;
            ans = min(ans, cnt);
        }
        printf("Case #%d: %d\n", cas, ans);
    }
}

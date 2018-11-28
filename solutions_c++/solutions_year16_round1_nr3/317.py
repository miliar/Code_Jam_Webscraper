#include <bits/stdc++.h>

using namespace std;

const int maxn = 10000;

int p[maxn];
bool inCycle[maxn];
int lenCycle[maxn];
int nC[maxn];
int sTC[maxn];
int maD[maxn];

void solve() {
    int n = 0;
    cin >> n;
    for (int i = 1; i <= n; i++) {
        inCycle[i] = false;
        lenCycle[i] = 0;
        nC[i] = 0;
        sTC[i] = 0;
        maD[i] = 0;
    }
    for (int i = 1; i <= n; i++) {
        cin >> p[i];
    }
    for (int i = 1; i <= n; i++) {
        int x = i;
        int cnt = 0;
        for (int j = 1; j <= n + 1; j++) {
            x = p[x];
            cnt++;
            if (x == i) {
                if (!inCycle[i]) {
                    inCycle[i] = true;
                    lenCycle[i] = cnt;
                    break;
                }
            }
        }
    }
    for (int i = 1; i <= n; i++) {
        int x = i;
        while (!inCycle[x]) {
            sTC[i]++;
            x = p[x];
        }
        nC[i] = x;
        maD[x] = max(sTC[i], maD[x]);
    }
    int ans = 0;
    int cnt2C = 0;
    for (int i = 1; i <= n; i++) {
        if (inCycle[i] && lenCycle[i] == 2)
            cnt2C++;
    }
    ans = cnt2C;
    cnt2C >>= 1;
    int go1 = 0;
    for (int i = 1; i <= n; i++) {
        if (lenCycle[i] == 2) {
            go1 += 2 + maD[i] + maD[p[i]];
        }
    }
    ans = max(ans, go1 / 2);
    for (int i = 1; i <= n; i++) {
        if (inCycle[i]) {
            ans = max(ans, lenCycle[i]);
            if (lenCycle[i] == 2) {
                ans = max(ans, 2 + maD[i] + maD[p[i]]);
            }
        } else {
            int tmp = sTC[i];
            int v = nC[i];
            if (lenCycle[v] == 2) {
                ans = max(ans, cnt2C * 2 + tmp + maD[p[v]]);
            }
        }
    }
    assert(ans <= n);
    cout << ans << endl;
}

int main() {
    ios_base :: sync_with_stdio(false);
    cin.tie(0);
    int test = 0;
    cin >> test;
    for (int id = 1; id <= test; id++) {
        cout << "Case #" << id << ": ";
        solve();
    }
    return 0;
}
#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
using namespace std;

#define rep(i, n)       rep2(i, 0, n)
#define rep2(i, m, n)   for (int i = (int)(m); i < (int)(n); ++i)
#define all(c)          (c).begin(), (c).end()

int t, k, n, a;
int init[202], type[22], visit[1050000];
vector<int> contain[22], memo[1050000];

bool ok(int state, int next)
{
    vector<int> have(init, init + 200);
    rep(i, n) if (state & (1 << i)) {
        rep(j, contain[i].size()) ++have[contain[i][j]];
        --have[type[i]];
    }
    return have[type[next]] > 0;
}

void dp(int state)
{
    if (state == (1 << n) - 1) { visit[state] = 1; return; }
    rep(i, n) if (!(state & (1 << i))) {
        if (!ok(state, i)) continue;
        if (!visit[state+(1<<i)]) dp(state + (1 << i));
        if (visit[state+(1<<i)] == -1) continue;
        visit[state] = 1;
        memo[state].assign(1, i);
        memo[state].insert(memo[state].end(), all(memo[state+(1<<i)]));
        return;
    }
    visit[state] = -1;
}

int main()
{
    cin >> t;
    rep(caseno, t) {
        cin >> k >> n;
        fill_n(init, 202, 0);
        rep(i, k) cin >> a, ++init[--a];
        rep(i, n) {
            cin >> type[i]; --type[i];
            cin >> k;
            contain[i].resize(k);
            rep(j, k) cin >> contain[i][j], --contain[i][j];
        }
        fill_n(visit, 1 << n, 0);
        dp(0);
        cout << "Case #" << caseno + 1 << ": ";
        if (visit[0] == -1) {
            cout << "IMPOSSIBLE" << endl;
        } else {
            rep(i, n) cout << memo[0][i] + 1 << (i == n - 1 ? "\n" : " ");
        }
    }
}

#include <bits/stdc++.h>

#define rep(i,n) for(int i=0;i<(int)(n);i++)
#define each(it,n) for(__typeof((n).begin()) it=(n).begin();it!=(n).end();++it)

using namespace std;

typedef long long ll;

int N, D;
ll S0, As, Cs, Rs;
ll M0, Am, Cm, Rm;
vector<int> salary, manager;
vector<vector<int> > G;

int doit(int v, int l, int r) {
    if (salary[v] < l || r < salary[v]) return 0;
    int ans = 1;
    rep(i, G[v].size()) {
        int u = G[v][i];
        ans += doit(u, l, r);
    }
    return ans;
}

void solve() {
    cin >> N >> D;
    cin >> S0 >> As >> Cs >> Rs;
    cin >> M0 >> Am >> Cm >> Rm;
    
    salary.clear();
    manager.clear();

    G = vector<vector<int> >(N);
    rep(i, N) {
        salary.push_back(S0);
        if (i == 0) manager.push_back(-1);
        else {
            manager.push_back(M0 % i);
            G[M0 % i].push_back(i);
        }
        S0 = (S0 * As + Cs) % Rs;
        M0 = (M0 * Am + Cm) % Rm;
    }

    int ans = 0;
    rep(i, D + 1) {
        ans = max(ans, doit(0, salary[0] - D + i, salary[0] + i));
    }
    cout << ans << endl;
}

int main() {
    int T;
    cin >> T;
    rep(i, T) {
        cout << "Case #" << i + 1 << ": "; 
        solve();
    }
    return 0;
}

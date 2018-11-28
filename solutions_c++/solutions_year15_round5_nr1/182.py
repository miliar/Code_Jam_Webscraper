#include <fstream>
#include <vector>
#include <algorithm>

using namespace std;

const int MAXN = 1000 * 1000 + 5, INF = 1000 * 1000 * 1000 + 5;
int s[MAXN];
vector<int> g[MAXN];
vector< pair<int, int> > ev;

void dfs(int v, int p, int mins, int maxs, int d) {
    mins = min(mins, s[v]);
    maxs = max(maxs, s[v]);
    if(maxs <= mins + d) {
        ev.push_back(make_pair(maxs, -1));
        ev.push_back(make_pair(mins + d, 1));
    }
    for(size_t i = 0; i < g[v].size(); i++)
        if(g[v][i] != p)
            dfs(g[v][i], v, mins, maxs, d);
}

int main() {
    ifstream in("input.txt");
    ofstream out("output.txt");
    int t;
    in >> t;
    for(int tt = 0; tt < t; tt++) {
        int n, d;
        in >> n >> d;
        for(int i = 0; i < n; i++)
            g[i].clear();
        ev.clear();
        int as, cs, rs, m, am, cm, rm;
        in >> s[0] >> as >> cs >> rs >> m >> am >> cm >> rm;
        for(int i = 1; i < n; i++) {
            s[i] = (s[i - 1] * as + cs) % rs;
            m = (m * am + cm) % rm;
            g[m % i].push_back(i);
        }
        dfs(0, -1, INF, -INF, d);
        sort(ev.begin(), ev.end());
        int sum = 0, ans = 0;
        for(size_t i = 0; i < ev.size(); i++) {
            sum -= ev[i].second;
            ans = max(ans, sum);
        }
        out << "Case #" << tt + 1 << ": " << ans << '\n';
    }
    return 0;
}

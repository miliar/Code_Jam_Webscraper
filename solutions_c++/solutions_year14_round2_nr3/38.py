#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

const int MN = 1011;

int n, m;
string id[MN];
vector<int> ke[MN];
bool visited[MN], exited[MN], blocked[MN], ok[MN];

void dfs(int u) {
    ok[u] = true;
    REP(i,ke[u].size()) {
        int v = ke[u][i];

        if (visited[v] || ok[v] || blocked[v]) continue;
        ok[v] = true;
        dfs(v);
    }
}

vector<int> path;
string path_id;

void visit(int u) {
    path_id += id[u];
    // cout << "Enter " << u << endl;
    path.push_back(u);
    visited[u] = true;
    string res = id[u];

    vector< pair<string,int> > cur; cur.clear();
    REP(i,ke[u].size()) {
        int v = ke[u][i];
        if (visited[v]) continue;

        cur.push_back(make_pair(id[v], v));
    }

    sort(cur.begin(), cur.end());

    REP(i,cur.size()) {
        string best = cur[i].first;
        // DEBUG(best);

        memset(blocked, false, sizeof blocked);
        FORD(x,path.size()-1,1) {
            blocked[path[x]] = true;
            memset(ok, false, sizeof ok);

            REP(y,x) if (!ok[path[y]]) {
                dfs(path[y]);
            }

            bool can = true;
            FOR(i,1,n) if (!ok[i] && !visited[i]) can = false;

            if (can) {
                REP(t,ke[path[x-1]].size())
                if (!visited[ke[path[x-1]][t]])
                    best = min(best, id[ke[path[x-1]][t]]);
            }
        }

        if (best == cur[i].first && !visited[cur[i].second]) {
            visit(cur[i].second);
        }
    }
    exited[u] = true;
    path.pop_back();
    // cout << "Exit " << u << endl;
}

void solve() {
    int start = 1;
    FOR(i,1,n) {
        if (id[i] < id[start]) start = i;
    }
    // DEBUG(start);
    memset(visited, false, sizeof visited);
    memset(exited, false, sizeof exited);

    path_id = "";
    visit(start);
}

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        cin >> n >> m;
        FOR(i,1,n) {
            cin >> id[i];
            ke[i].clear();
        }
        FOR(i,1,m) {
            int u, v; cin >> u >> v;
            ke[u].push_back(v);
            ke[v].push_back(u);
        }

        solve();
        cout << "Case #" << test << ": " << path_id << endl;
        cerr << test << endl;
    }
    return 0;
}

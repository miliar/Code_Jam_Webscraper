#include <bits/stdc++.h>
#define FOR(i, n) for (int i = 0; i < n; ++i)
using namespace std;

typedef long long ll;
const int MAX_N = 60000;
const int INF = INT_MAX / 2;
int S, T;
const int dir_x[] = {-1, 1, 0, 0};
const int dir_y[] = {0, 0, 1, -1};
int get(char c) {
    if (c == '^') return 0;
    if (c == 'v') return 1;
    if (c == '>') return 2;
    if (c == '<') return 3;
    assert(false);
    return -1;
}

class MinCostMaxFlow {
public:
    int total, pv[MAX_N], pe[MAX_N], pnt[MAX_N];
    int flow[MAX_N], cost[MAX_N];
    int head[MAX_N], next[MAX_N];
    queue<int> q;
    bool visited[MAX_N];
    int dis[MAX_N];
    MinCostMaxFlow() {
        total = 0;
        memset(head, -1, sizeof head);        
    }
    void addedge(int f, int t, int cp, int cs) {
        // cout << f << " " << t << " " << cp << " " << cs << endl;
        next[total] = head[f]; head[f] = total; pnt[total] = t; flow[total] = cp; cost[total++] = cs;
        next[total] = head[t]; head[t] = total; pnt[total] = f; flow[total] = 0; cost[total++] = -cs;
    }
    int mincost(int& maxflow) {
        int mincost = 0;
        maxflow = 0;
        while (true) {
            memset(visited, false, sizeof(visited));
            for (int i = 0; i < MAX_N; ++i) {
                pv[i] = -1;
                dis[i] = INF;
            }
            while (!q.empty()) q.pop();
            dis[S] = 0; q.push(S); visited[S] = true;
            while (!q.empty()) {
                int cur = q.front(); q.pop(); visited[cur] = false;
                for (int i = head[cur]; i >=0; i = next[i]) {
                    int b = pnt[i];
                    if (flow[i] > 0 && dis[b] > dis[cur]+cost[i]) {
                        dis[b] = dis[cur] + cost[i];
                        pv[b] = cur; pe[b] = i;
                        if (!visited[b]) { q.push(b); visited[b] = true; }
                    }
                }
            }
            if (dis[T] == INF) break; 
            // find minimal flow on shortest
            int mn_flow = INF;
            for (int i = T; i != S; i = pv[i]) {
                mn_flow = min(mn_flow, flow[pe[i]]);
            }
            maxflow += mn_flow;
            mincost += mn_flow * dis[T];
            cout << "delta: " << mn_flow * dis[T] << endl;
            // update residual flow network
            for (int i = T; i != S; i = pv[i]) {
                flow[pe[i]] -= mn_flow;
                flow[pe[i] ^ 1] += mn_flow;
            }
        }
        return mincost;
    }
};

string g[205];
void solve() {
    int row, col, nx, ny;
    MinCostMaxFlow network;
    S = 0; T = 1;
    cin >> row >> col;
    FOR(i, row) cin >> g[i];
    int idx = 2;
    map<pair<int, int>, int> mp;
    FOR(i, row) FOR(j, col) {
        if (g[i][j] != '.') mp[make_pair(i, j)] = idx++;
    }
    if (mp.size() == 1) {
        cout << "IMPOSSIBLE" << endl;
        return;
    }
    if (mp.size() == 0) { cout << 0 << endl; return; }
    int start = mp.size() + 5;
    int pp, res = 0;
    FOR(i, row) FOR(j, col) {
        if (g[i][j] == '.') continue;
        int x = i, y = j;
        pair<int, int> from = make_pair(i, j);        
        int cc = get(g[i][j]);
        set<int> st;
        FOR(k, 4) {
            nx = x + dir_x[k]; ny = y + dir_y[k];
            while (nx < row && ny < col && nx >= 0 && ny >= 0 && g[nx][ny] == '.') {
                nx += dir_x[k]; ny += dir_y[k];
            }
            pair<int, int> t = make_pair(nx, ny);
            if (mp.find(t) != mp.end()) {
                st.insert(k);                
            }
        }
        if (st.empty()) { cout << "IMPOSSIBLE" << endl; return; }
        else res += (st.find(cc) == st.end());
    }
    cout << res << endl; return;    
}

int main() {
    int TestCase;
    cin >> TestCase;
    FOR(caseID, TestCase) {
        cout << "Case #" << caseID + 1 << ": ";
        solve();
    }
    return 0;
}

#include <bits/stdc++.h>

#define FOR(i,a,b) for(int i=(a),_b=(b); i<=_b; i++)
#define FORD(i,a,b) for(int i=(a),_b=(b); i>=_b; i--)
#define REP(i,a) for(int i=0,_a=(a); i<_a; i++)

#define DEBUG(x) { cout << #x << " = "; cout << (x) << endl; }
#define PR(a,n) { cout << #a << " = "; FOR(_,1,n) cout << a[_] << ' '; cout << endl; }
#define PR0(a,n) { cout << #a << " = "; REP(_,n) cout << a[_] << ' '; cout << endl; }
using namespace std;

struct Edge {
    int from, to, cap, flow, index;
    Edge(int from, int to, int cap, int flow, int index) :
        from(from), to(to), cap(cap), flow(flow), index(index) {}
};
#define LL int
struct PushRelabel {
    int N;
    vector<vector<Edge> > G;
    vector<LL> excess;
    vector<int> dist, active, count;
    queue<int> Q;

    PushRelabel(int N) : N(N), G(N), excess(N), dist(N), active(N), count(2*N) {}

    void AddEdge(int from, int to, int cap) {
        G[from].push_back(Edge(from, to, cap, 0, G[to].size()));
        if (from == to) G[from].back().index++;
        G[to].push_back(Edge(to, from, 0, 0, G[from].size() - 1));
    }
    void Enqueue(int v) { 
        if (!active[v] && excess[v] > 0) { active[v] = true; Q.push(v); } 
    }
    void Push(Edge &e) {
        int amt = int(min(excess[e.from], LL(e.cap - e.flow)));
        if (dist[e.from] <= dist[e.to] || amt == 0) return;
        e.flow += amt;
        G[e.to][e.index].flow -= amt;
        excess[e.to] += amt;        
        excess[e.from] -= amt;
        Enqueue(e.to);
    }
    void Gap(int k) {
        for (int v = 0; v < N; v++) {
            if (dist[v] < k) continue;
            count[dist[v]]--;
            dist[v] = max(dist[v], N+1);
            count[dist[v]]++;
            Enqueue(v);
        }
    }
    void Relabel(int v) {
        count[dist[v]]--;
        dist[v] = 2*N;
        for (int i = 0; i < G[v].size(); i++) 
            if (G[v][i].cap - G[v][i].flow > 0)
        dist[v] = min(dist[v], dist[G[v][i].to] + 1);
        count[dist[v]]++;
        Enqueue(v);
    }
    void Discharge(int v) {
        for (int i = 0; excess[v] > 0 && i < G[v].size(); i++) Push(G[v][i]);
        if (excess[v] > 0) {
            if (count[dist[v]] == 1) 
        Gap(dist[v]); 
            else
        Relabel(v);
        }
    }
    LL GetMaxFlow(int s, int t) {
        count[0] = N-1;
        count[N] = 1;
        dist[s] = N;
        active[s] = active[t] = true;
        for (int i = 0; i < G[s].size(); i++) {
            excess[s] += G[s][i].cap;
            Push(G[s][i]);
        }
        while (!Q.empty()) {
            int v = Q.front();
            Q.pop();
            active[v] = false;
            Discharge(v);
        }
        LL totflow = 0;
        for (int i = 0; i < G[s].size(); i++) totflow += G[s][i].flow;
        return totflow;
    }
};

bool good[511][511];

int main() {
    ios :: sync_with_stdio(false);
    int ntest; cin >> ntest;
    FOR(test,1,ntest) {
        int w, h, b;
        cin >> w >> h >> b;

        memset(good, true, sizeof good);
        FOR(i,1,b) {
            int x0, y0, x1, y1;
            cin >> x0 >> y0 >> x1 >> y1;
            if (x0 > x1) swap(x0, x1);
            if (y0 > y1) swap(y0, y1);
            FOR(y,y0,y1) FOR(x,x0,x1) good[y][x] = false;
        }
        int n;
        n = 2 * w * h + 2;

        PushRelabel flow(n + 1);

        REP(i,h) REP(j,w) if (good[i][j]) {
            int getIn = i*w + j + 2;
            int getOut = getIn + w*h;

            flow.AddEdge(getIn, getOut, 1);

            if (i == 0) {
                flow.AddEdge(1, getIn, 1);
            }
            if (i == h-1) {
                flow.AddEdge(getOut, n, 1);
            }

            if (i < h-1 && good[i+1][j]) {
                flow.AddEdge(getOut, getIn+w, 1);
                flow.AddEdge(getOut+w, getIn, 1);
            }
            if (j < w-1 && good[i][j+1]) {
                flow.AddEdge(getOut, getIn+1, 1);
                flow.AddEdge(getOut+1, getIn, 1);
            }
        }

        cout << "Case #" << test << ": " << flow.GetMaxFlow(1, n) << endl;
        cerr << test << endl;
    }
    return 0;
}

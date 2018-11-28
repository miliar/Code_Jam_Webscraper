#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <string>
#include <vector>
#include <deque>
#include <list>
#include <algorithm>
#include <numeric>
#include <functional>
#include <cmath>
#include <cstring>
#include <cctype>
#include <sstream>
#include <set>
#include <map>
#include <queue>
#include <complex>
using namespace std;
#define REP(i,n) for(int i = 0; i < (int)n; i++)
#define FOR(i,a,b) for(int i = a; i < (int)b; i++)
#define FOREQ(i,a,b) for(int i = a; i <= (int)b; i++)
#define FOREACH(it, c) for(__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)
#define ALL(c) (c).begin(), (c).end()
#define SZ(c) (c).size()
template <class T> void pp(T v) { FOREACH(it, v) cout << *it << ' '; cout << endl ; }
template <class T> void pp(T v, int n) { REP(i,n) cout<<v[i]<< ' '; cout << endl; }
template <class T> inline void chmax(T &a, const T b) { a = max(a, b); }
template <class T> inline void chmin(T &a, const T b) { a = min(a, b); }
typedef vector<int> vint;
typedef pair<int, int> pint;
//typedef complex<double> P;
#define mp make_pair
typedef long long ll;
typedef long double ld;
typedef unsigned uint;
//const int INF = 1<<28;
const double EPS = 1.0e-9;
static const int dx[] = {1, 0, -1, 0}, dy[] = {0, -1, 0, 1};
#define MOD_CALC
#ifdef MOD_CALC
const ll MOD = 1000002013 ; // 1000000007
inline void chadd(ll &a, const ll b) { a = (a + b) % MOD;}
inline ll add(const ll a, const ll b){ return (a + b) %  MOD;}
inline void chsub(ll &a, const ll b) { a = (a - b + MOD) % MOD;}
inline ll sub(const ll a, const ll b){ return (a - b + MOD) % MOD; }
inline void chmul(ll &a, const ll b) { a = (a * b) %  MOD;}
inline ll mul(const ll a, const ll b){ return (a * b) %  MOD;}
#endif

// from Ari book pp. 203-204
const int INF = 1000000;
typedef pair<int, int> P;
const int MAX_V = 128;
struct edge {
    int to, cap, cost, rev;
};
int V;
vector<edge> G[MAX_V];
int h[MAX_V];
int dist[MAX_V];
int prevv[MAX_V], preve[MAX_V];
void add_edge(const int from, const int to, const int cap, const int cost) {
    G[from].push_back((edge){to, cap, cost, G[to].size()});
    G[to].push_back((edge){from, 0, -cost, G[from].size() - 1});
}
int min_cost_flow(const int s, const int t, int f) {
    int res = 0;
    fill(h, h + V, 0);
    while(f > 0) {
        priority_queue<P, vector<P>, greater<P> > que;
        fill(dist, dist + V, INF);
        dist[s] = 0;
        que.push(P(0, s));
        while(! que.empty()) {
            P p = que.top(); que.pop();
            int v = p.second;
            if(dist[v] < p.first) continue;
            for(int i = 0; i < (int)G[v].size(); i++) {
                edge &e = G[v][i];
                if(e.cap > 0 && dist[e.to] > dist[v] + e.cost + h[v] - h[e.to]) {
                    dist[e.to] = dist[v] + e.cost + h[v] - h[e.to];
                    prevv[e.to] = v;
                    preve[e.to] = i;
                    que.push(P(dist[e.to], e.to));
                }
            }
        }
        if(dist[t] == INF) return -1;
        for(int v = 0; v < V; v++) h[v] += dist[v];

        int d = f;
        for(int v = t; v != s; v = prevv[v]) {
            d = min(d, G[prevv[v]][preve[v]].cap);
        }
        f -= d;
        res += d * h[t];
        for(int v = t; v != s; v = prevv[v]) {
            edge &e = G[prevv[v]][preve[v]];
            e.cap -= d;
            G[v][e.rev].cap += d;
        }
    }
    return res;
}
//
int fee[MAX_V];
void init()
{
    fee[0] = 0;
    int N = 100;
    for(int i = 1; i <= 100; i++) {
        fee[i] = fee[i-1] + N;
        fee[i] -= (i-1);
        //cout << i << " " << fee[i] << endl;
    }
}

int solve() {
    int N, M; cin>>N>>M;
    V = N + 2;
    int num = 0;
    int org = 0;
    for(int i = 0; i < MAX_V; i++) {
        G[i].clear();
    }
    set<int> s_set;
    for(int i = 0; i < M; i++) {
        int o, e, p; cin>>o>>e>>p;
        add_edge(0, o, p, 0);
        add_edge(e, N+1, p, 0);
        s_set.insert(o);
        s_set.insert(e);
        num += p;
        org += fee[e-o] * p;
    }
    vector<int> station(ALL(s_set));
    REP(i, station.size()) {
        for(int j = i + 1; j < (int)station.size(); j++) {
            add_edge(station[i], station[j], INF, fee[station[j]-station[i]]);
        }
    }
    //for(int i = 0; i < V; i++) {
        //cout << G[i].size() << endl;
    //}
    int min_cost = min_cost_flow(0, N+1, num);
    //cout << min_cost << " " << org << endl;
    return org - min_cost;

}
int main(void)
{
    int T; cin>>T;
    init();
    for(int case_no = 1; case_no <= T; case_no++) {
        int ans = solve();
        cout << "Case #" << case_no << ": ";
        cout << ans << endl;

    }
    return 0;
}

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int, int> ii;
typedef vector<int> vi;
typedef vector<ii> vii;
template <class T> int size(const T &x) { return x.size(); }
const int INF = 2147483647;
#define rep(i,a,b) for (__typeof(a) i=(a); i<(b); ++i)
#define iter(it,c) for (__typeof((c).begin()) it = (c).begin(); it != (c).end(); ++it)

#define MAXN 5000
int dist[MAXN+1], q[MAXN+1];
#define dist(v) dist[v == -1 ? MAXN : v]
struct bipartite_graph {
    int N, M, *L, *R; vi *adj;
    bipartite_graph(int _N, int _M) : N(_N), M(_M),
        L(new int[N]), R(new int[M]), adj(new vi[N]) {}
    ~bipartite_graph() { delete[] adj; delete[] L; delete[] R; }
    bool bfs() {
        int l = 0, r = 0;
        rep(v,0,N) if(L[v] == -1) dist(v) = 0, q[r++] = v;
            else dist(v) = INF;
        dist(-1) = INF;
        while(l < r) {
            int v = q[l++];
            if(dist(v) < dist(-1)) {
                iter(u, adj[v]) if(dist(R[*u]) == INF)
                    dist(R[*u]) = dist(v) + 1, q[r++] = R[*u];
            }
        }
        return dist(-1) != INF;
    }
    bool dfs(int v) {
        if(v != -1) {
            iter(u, adj[v])
                if(dist(R[*u]) == dist(v) + 1)
                    if(dfs(R[*u])) {
                        R[*u] = v, L[v] = *u;
                        return true;
                    }
            dist(v) = INF;
            return false;
        }
        return true;
    }
    void add_edge(int i, int j) { adj[i].push_back(j); }
    int maximum_matching() {
        int matching = 0;
        memset(L, -1, sizeof(int) * N);
        memset(R, -1, sizeof(int) * M);
        while(bfs()) rep(i,0,N)
            matching += L[i] == -1 && dfs(i);
        return matching;
    }
};

bool can[100][100];
bool curcan[100][100];

int main() {
    int ts;
    cin >> ts;
    rep(t,0,ts) {
        int n;
        cin >> n;
        rep(i,0,n) {
            string line;
            cin >> line;
            rep(j,0,n) {
                can[i][j] = line[j] == '1';
            }
        }
        int mn = INF;
        rep(s,0,(1<<(n*n))) {
            bool ok = true;
            int cost = 0;
            rep(i,0,n) {
                rep(j,0,n) {
                    if (s & (1<<(i*n+j))) {
                        curcan[i][j] = true;
                        if (!can[i][j]) {
                            cost++;
                        }
                    } else {
                        curcan[i][j] = false;
                        if (can[i][j]) {
                            ok = false;
                            break;
                        }
                    }
                }
                if (!ok) break;
            }
            if (!ok) continue;
            if (cost > mn) continue;
            // if (t == 0) {
            //     printf("checking\n");
            //     rep(i,0,n) {
            //         rep(j,0,n) {
            //             printf("%d", curcan[i][j]);
            //         }
            //         printf("\n");
            //     }
            //     printf("\n");
            // }
            rep(i,0,n) {
                bipartite_graph G(n,n);
                int left = 0;
                rep(j,0,n) {
                    if (curcan[i][j]) {
                        left++;
                        rep(k,0,n) {
                            if (i == k)
                                continue;
                            if (curcan[k][j]) {
                                G.add_edge(k,j);
                            }
                        }
                    }
                }
                if (G.maximum_matching() == left) {
                    ok = false;
                    break;
                }
            }
            if (ok) {
                mn = min(mn, cost);
            }
        }
        printf("Case #%d: %d\n", t+1, mn);
    }

    return 0;
}


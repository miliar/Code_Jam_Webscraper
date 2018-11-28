#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>
#include <vector>
#include <queue>

#define FOR(i,a,b) for(int i = (a); i <= (b);i++)
#define FR(i,a) for(int i = 0; i < (a); i++)
#define DOWN(i,a,b) for(int i = (a); i >= (b); i--)

using namespace std;
#define maxn 120005
const int dx[4] = {0,1,0,-1};
const int dy[4] = {1,0,-1,0};
queue<int> q;
vector<int> a[maxn], f[maxn], c[maxn], inv[maxn];
int pos[1000][1000];
bool dd[1000][1000];
int n,W,H,k,Trace[maxn], Trace_f[maxn];
void add_edge(int u, int v, int ca) {
    inv[u].push_back(a[v].size());
    inv[v].push_back(a[u].size());
    a[u].push_back(v);
    f[u].push_back(0);
    c[u].push_back(ca);
    
    a[v].push_back(u);
    f[v].push_back(0);
    c[v].push_back(0);
}
bool find_path() {
    while (!q.empty()) q.pop();
    FOR(i,0,2*n+1) Trace[i] = -1;
    q.push(0);
    Trace[0] = 0;
    while (!q.empty()) {
        int u = q.front(); q.pop();
        FR(i,a[u].size()) {
            int v = a[u][i];
            if (Trace[v] == -1 && f[u][i] < c[u][i]) {
                Trace[v] = u;
                Trace_f[v] = i;
                if (v == 2*n+1) return true;
                q.push(v);
            }
        }
    }
    return false;
}
void inc_flow() {
    int j = 2*n+1,i , delta=1000000009;
    do {
        i = Trace[j];
        delta = min(delta, c[i][ Trace_f[j]] - f[i][Trace_f[j]]);
        j = i;
    } while (j != 0);
    j=2*n+1;
    do {
        i = Trace[j];
        f[i][Trace_f[j]] += delta;
        f[j][ inv[i][Trace_f[j]] ] -= delta;
        j = i;
    } while (j != 0);
}
void solve() {
    //careful khoi tao
    cerr << 2*n+1 << endl;
    FOR(i,0,2*n+1) {
        inv[i].clear();
        a[i].clear();
        f[i].clear();
        c[i].clear();
    }
    //
    FOR(i,1,W) 
    if (dd[i][1]) {
        add_edge(0,pos[i][1],1);
    }
    FOR(i,1,W)
    if (dd[i][H]) {
        add_edge(pos[i][H]+n,2*n+1,1);
    }
    FOR(i,1,W) FOR(j,1,H) {
        if (dd[i][j]) {
            add_edge(pos[i][j], pos[i][j]+n, 1);
            FR(k,4)
            if (i + dx[k] > 0 && i + dx[k] <= W && j + dy[k] > 0 && j + dy[k] <= H) {
                add_edge(pos[i][j] + n, pos[i+dx[k]][j+dy[k]],1);
            }
        }
    }
    do {
        if (!find_path()) break;
        inc_flow();
    } while (true);
    int res = 0;
    FR(i,f[0].size()) res += f[0][i];
    cout << res << endl;
}
int main() 
{
    freopen("CC.in","r",stdin);
    freopen("test.out","w",stdout);
    int ntest;
    cin >> ntest;
    FOR(test,1,ntest) {
        cout << "Case #" << test << ": ";
        cin >> W >> H >> k;
        n = 0;
        memset(dd,false,sizeof(dd));
        FOR(i,1,W) FOR(j,1,H) {
            pos[i][j] = ++n;
            dd[i][j] = true;
        }
        int X,Y,X2,Y2;
        FOR(iter,1,k) {
            cin >> X >> Y >> X2 >> Y2;
            X++; Y++; X2++; Y2++;
            FOR(i,X,X2)
            FOR(j,Y,Y2) {
                dd[i][j] = false;
            }
        }
        solve();
    }        
    return 0;
}


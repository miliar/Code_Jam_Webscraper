#define debug if(0)
#include <string>
#include <iostream>
#include <vector>
#include <set>
#include <map>
#include <algorithm>
#include <cctype>
#include <queue>
#include <climits>
#include <sstream>
#include <cassert>
#include <iostream>
#include <cstdio>
#include <iostream>
using namespace std;

#define REP(i,n) for(int i=0; i<(n); i++)
#define FOR_EACH(it,v) for(__typeof((v).begin()) it = (v).begin(); it!=(v).end(); ++it)
#define show(x) debug cout << #x << ": " << x << endl;

#define ALL(v) (v).begin(), (v).end()

template<typename T>
ostream& operator<<(ostream &o, const vector<T>&v){
    FOR_EACH(x, v){
        if(x==v.begin()) o << "[";
        else o << ", ";
        o << *x;
    }
    o << "]";
    return o;
}

typedef long long LL;
typedef pair<int,int> PII;
typedef vector<int>VI;
typedef vector<vector<int> >VII;

const int N = 21;
const int inf = 1000000009;
int n,m,p;
vector<int>path;

struct Route{
    int from;
    int dest;
    int a, b;
    int id;
    Route(int f_, int d_, int a_, int b_, int id_):
        from(f_), dest(d_), a(a_), b(b_), id(id_){
    }
};

vector<Route>adj[N];
vector<Route>E;
vector<Route>PATH;
VI vertices;

int MASK;

inline void check(int &a, int b){
    if(b<a) a = b;
}

int dist[N][N];

int cost(int id){
    Route e = E[id];
    int cost = e.a;
    if(MASK & (1<<e.id)) cost = e.b;
    return cost;
}

int comp_pref(){
    REP(i,n) REP(j,n) dist[i][j] = inf;
    REP(i,n) dist[i][i] = 0;

    FOR_EACH(e, E){
        check(dist[e->from][e->dest], cost(e->id));
        //debug printf("edge %d->%d, cost %d\n", e->from, e->dest, cost(e->id));
    }

    REP(k,n){
        REP(i,n){
            REP(j,n){
                check(dist[i][j], dist[i][k] + dist[k][j]);
            }
        }
    }

    /*
    debug {
        printf("dist:\n");
        REP(i,n){
            REP(j,n){
                printf("%d ", dist[i][j]);
            }
            printf("\n");
        }
    } // */
    int res = 0;
    int best = dist[0][1];

    int act = 0;
    FOR_EACH(e, PATH){
        int c = 0;
        c += dist[0][e->from];
        c += cost(e->id);
        c += dist[e->dest][1];
        if(c>best) break;
        res++;
    }
    return res;
}

void solve(){
    scanf("%d %d %d", &n, &m, &p);
    REP(i,m){
        int u,v,a,b;
        scanf("%d %d %d %d", &u, &v, &a, &b);
        u--;v--;
        adj[u].push_back(Route(u,v,a,b,i));
        E.push_back(Route(u,v,a,b,i));
    }
    REP(i,p){
        int x; scanf("%d", &x);
        x--;
        path.push_back(x);
        PATH.push_back(E[x]);
        vertices.push_back(E[i].dest);
    }
    int mx_pref = 0;

    REP(i, (1<<m)){
        MASK = i;
        int pref = comp_pref();
        mx_pref = max(pref, mx_pref);
    }

    show(mx_pref);

    if(mx_pref==PATH.size()){
        printf("Looks Good To Me\n");
    } else {
        printf("%d\n", path[mx_pref]+1);
    }
    REP(i,n) adj[i].clear();
    E.clear();
    vertices.clear();
    path.clear();
    PATH.clear();
}

int main(int argc,char *argv[]) {
    int T; scanf("%d", &T);
    for(int t=1; t<=T; t++){
        printf("Case #%d: ", t);
        debug cout << endl;
        solve();
        fflush(stdout);
    }
}

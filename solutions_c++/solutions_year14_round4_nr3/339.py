#include <bits/stdc++.h>
#define int ll
// def //{{{
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,sz(v))
#define let(v, x) __typeof(x) v = (x)
#define foreach(i,v) for(let(i, (v).begin());i!=(v).end();i++)
#define pb push_back
#define eb emplace_back
#define mp make_pair
#define mt make_tuple
#define fst first
#define snd second
#define all(x) (x).begin(),(x).end()
#define rall(x) (x).rbegin(),(x).rend()
#define sz(x) ((int)(x).size())
#define cauto const auto &
//}}}
using namespace std;
// typedef//{{{
typedef long long ll;
typedef unsigned long long ull;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef pair<int,int> pii;
typedef pair<int,pii> pipii;
//}}}
// tr << ( vector, map, pair, tuple, etc... ) << endl//{{{
template <typename T, typename U>
struct sfinae_helper{typedef void type;};
template <typename T, typename U = void>
struct Print{ static ostream &pp(ostream &os, const T &x){ return os << x; } };
struct trace{//{{{
    ostream& os;
    trace(ostream& os): os(os) { }
    template<typename T>
        trace& operator<<(const T& x){ Print<T>::pp(os, x); return *this;}
    trace &operator<<(ostream& f(ostream&)){ f(os); return *this; }
    operator ostream &(){ return os; }
} tr(cout);//}}}
// Container//{{{
template <typename T> struct Print<T, typename sfinae_helper<T, typename T::iterator>::type>{
    static ostream &pp(ostream &os, const T &v){
        trace(os) << '[';
        for(const auto &x : v) trace(os) << x << ", ";
        return trace(os) << ']';
    }
};//}}}
// Pair//{{{
template <typename T> struct Print<T, typename sfinae_helper<T, typename T::first_type>::type>{
    static ostream &pp(ostream &os, const T &x){
        return trace(os) << '(' << x.first << ", " << x.second << ')';
    }
};//}}}
// Tuple//{{{
template<class T, size_t N> struct TuplePrint{
    static ostream &print(ostream &os, const T &x){
        TuplePrint<T, N-1>::print(os, x) << ", ";
        return trace(os) << get<N-1>(x);
    }
};
template<class T> struct TuplePrint<T, 1>{
    static ostream &print(ostream &os, const T &x){
        return trace(os) << get<0>(x);
    }
};
template <typename... Args>//Tuple
struct Print<tuple<Args...>>{
    static ostream &pp(ostream &os, const tuple<Args...> &x){
        os << "(";
        return TuplePrint<decltype(x), sizeof...(Args)>::print(os, x) << ")";
    }
};//}}}
//}}}
template<typename T> T s_to(string s){ //{{{
    stringstream ss;
    T res;
    ss << s;
    ss >> res;
    return res;
} //}}}
template<typename T> string to_s(T t){ //{{{
    stringstream ss;
    ss << t;
    return ss.str();
} //}}}
template<class T> T mineq(T &a, const T &b){ return a = min(a, b); }
template<class T> T maxeq(T &a, const T &b){ return a = max(a, b); }
#define bit(n) (1LL<<(n))
static const int INF = 1<<25;
static const double EPS = 1e-5;

inline void pre(){
}

struct Dinic{//{{{
    typedef int Cap;
    static const Cap INF = 1<<29;
    struct E{//{{{
        int dst;
        Cap cap;
        int rev;
        E(int dst, Cap cap, int rev) : dst(dst), cap(cap), rev(rev) {}
    };//}}}
    int n;
    vector<vector<E> > g;
    Dinic(int n) : n(n), g(n) {}
    inline void add_edge(int src, int dst, Cap cap){//{{{
        if(src == dst) return;
        g[src].push_back(E(dst,cap,g[dst].size()));
        g[dst].push_back(E(src, 0 ,g[src].size() - 1));
    }//}}}
    inline void add_undirected_edge(int src, int dst, Cap cap){//{{{
        if(src == dst) return;
        g[src].push_back(E(dst,cap,g[dst].size()));
        g[dst].push_back(E(src,cap,g[src].size() - 1));
    }//}}}

    vector<int> level, iter;
    Cap dfs(const int &s, const int &u, Cap crr){//{{{
        if(s == u || crr == 0) return crr;
        Cap sum = 0;
        for(int &i = iter[u]; i < g[u].size(); ++i){
            E &e = g[u][i], &ee = g[e.dst][e.rev];
            const int &v = e.dst; // s -- v - u -- t
            if(level[v] >= level[u] || ee.cap <= 0) continue;
            Cap f = dfs(s, v, min(crr - sum, ee.cap));
            if(f <= 0) continue;
            ee.cap -= f; e.cap += f;
            sum += f;
            if(sum == crr) break;
        }
        return sum;
    }//}}}
    Cap run(int s, int t){//{{{
        vector<int> q(n);
        for(Cap flow = 0; ;){
            level.assign(n, -1);
            int ql = 0, qr = 0;
            level[q[qr++] = s] = 0;
            while(ql != qr && level[t] == -1){
                int u = q[ql++];
                foreach(e, g[u]) if(e->cap > 0 && level[e->dst] == -1)
                    level[ q[qr++] = e->dst ] = level[u] + 1;
            }
            if(level[t] == -1) return flow;
            iter.assign(n, 0);
            flow += dfs(s, t, INF);
        }
    }//}}}
};//}}}

int dx[] = { 1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
#define IN(i, j) ((i)*w+(j))
#define OUT(i, j) ((i)*w+(j)+h*w)
inline void solve(){
    int w, h, b; cin >> w >> h >> b;
    vector<vi> in(h, vi(w, 0));
    const int n = w*h, src = n+n, dst = n+n+1;
    Dinic mf(n+n+2);
    rep(i, b){
        int x0, x1, y0, y1;
        cin >> x0 >> y0 >> x1 >> y1;
        REP(i, y0, y1+1) REP(j, x0, x1+1) in[i][j] = 1;
    }
    rep(i, w) mf.add_edge(src, IN(0, i), 1);
    rep(i, w) mf.add_edge(OUT(h-1, i), dst, 1);
    rep(i, h) rep(j, w) mf.add_edge(IN(i, j), OUT(i, j), 1);
    rep(i, h) rep(j, w){
        rep(dir, 4){
            int ii = i + dx[dir], jj = j + dy[dir];
            if(0 <= ii && ii < h && 0 <= jj && jj < w) if(!in[i][j] && !in[ii][jj]){
                mf.add_edge(OUT(i, j), IN(ii, jj), 1);
            }
        }
    }
    cout << mf.run(src, dst) << endl;
}

signed main(){
    pre();
    //cin.tie(0);
    //ios_base::sync_with_stdio(0);
    cout.setf(ios::fixed); cout.precision(10);
    string s;
    getline(cin, s);
    int T = s_to<int>(s);
    rep(i, T){
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
    return 0;
}
/* vim:set foldmethod=marker commentstring=//%s : */

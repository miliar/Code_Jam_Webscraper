#include <bits/stdc++.h>//{{{
#define all(x) begin(x),end(x)
#define rall(x) (x).rbegin(),(x).rend()
#define REP(i,b,n) for(int i=(int)(b);i<(int)(n);++i)
#define rep(i,n) REP(i,0,n)
#define repsz(i,v) rep(i,(v).size())
#define aur auto&
#define bit(n) (1LL<<(n))
#define eb emplace_back
#define mt make_tuple
#define fst first
#define snd second
using namespace std;
typedef long long ll;
//#define int long long
template<class C>int size(const C &c){ return c.size(); }
template<class T>bool chmin(T&a,const T&b){if(a<=b)return false;a=b;return true;}
template<class T>bool chmax(T&a,const T&b){if(a>=b)return false;a=b;return true;}//}}}
template<typename T> T s_to(string s){ //{{{
    stringstream ss;
    T res;
    ss << s;
    ss >> res;
    return res;
} //}}}

vector<string> split(const string &s, const char &del){ //{{{
    vector<string> res;
    int p = 0, q;
    while((q = s.find_first_of(del, p)) != string::npos){
        res.eb(s.substr(p, q-p));
        p = q+1;
    }
    res.eb(s.substr(p));
    return res;
} //}}}


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
                for(auto &e : g[u]) if(e.cap > 0 && level[e.dst] == -1)
                    level[ q[qr++] = e.dst ] = level[u] + 1;
            }
            if(level[t] == -1) return flow;
            iter.assign(n, 0);
            flow += dfs(s, t, INF);
        }
    }//}}}
};//}}}
template<typename T> struct Zipper{//{{{
    map<T, int> zip;
    vector<T> unzip;
    template<typename It> inline void add(It b, It e){ while(b != e) add(*b++); }
    inline void add(const T &x){//{{{
        if(zip.count(x)) return;
        zip[x] = unzip.size();
        unzip.emplace_back(x);
    }//}}}
    inline void compile(){//{{{
        int i = 0;
        for(auto &x : zip) unzip[x.second = i++] = x.first;
    }//}}}
    inline const int operator[](const T &x){//{{{
        add(x);
        return zip[x];
    }//}}}
    inline const T operator()(const int &i) const { return unzip[i]; }
    inline int size() const { return zip.size(); }
    typename vector<T>::const_iterator begin(){ return unzip.begin(); }
    typename vector<T>::const_iterator end(){ return unzip.end(); }
    T ub1(T x){ return zip.upper_bound(x)->first; }
    T lb1(T x){ return zip.lower_bound(x)->first; }
    T ub2(T x){ return zip.upper_bound(x)->second; }
    T lb2(T x){ return zip.lower_bound(x)->second; }
};//}}}

constexpr int INF = 1E8;
bool solve(){
    int n; cin >> n; cin.ignore();

    vector<set<int>> in(n);
    Zipper<string> zip;
    {//{{{
        rep(i, n){
            string s; getline(cin, s);
            for(auto &c : split(s, ' ')) in[i].emplace(zip[c]);
        }
    }//}}}

    const int geta = n;
    const int src = geta + size(zip) * 2 + 10, dst = src + 1;
    Dinic mf(dst + 1);
    rep(i, n){
        for(auto &x : in[i]){
            mf.add_edge(i, geta + x, INF);
            mf.add_edge(geta + x + size(zip), i, INF);
        }
    }
    rep(i, size(zip)){
        mf.add_edge(geta + i, geta + i + size(zip), 1);
        mf.add_edge(geta + i + size(zip), geta + i, 1);
    }
    mf.add_edge(src, 0, INF);
    mf.add_edge(1, dst, INF);
    cout << mf.run(src, dst) << endl;
    return true;
}
signed main(){
    cin.tie(nullptr);
    ios_base::sync_with_stdio(false);
    cout << std::fixed << std::setprecision(10);
    string s;
    getline(cin, s);
    int T = s_to<int>(s);
    rep(i, T){
        cout << "Case #" << (i+1) << ": ";
        solve();
    }
    return 0;
}
// vim:set foldmethod=marker commentstring=//%s:

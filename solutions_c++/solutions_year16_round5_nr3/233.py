#include<algorithm>
#include<bitset>
#include<cassert>
#include<complex>
#include<cstdio>
#include<cstring>
#include<iomanip>
#include<iostream>
#include<map>
#include<queue>
#include<set>
#include<stack>
#include<string>
#include<vector>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define debug(x) {cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {{cerr <<#x <<" = "; FORE(itt, (x)) cerr <<*itt <<", "; cerr <<endl; }}
#define dprintf(...) fprintf(stderr, __VA_ARGS__)
using namespace std;
typedef long long LL;
typedef long double LD;
typedef pair<int, int> PII;
typedef vector<int> VI;

template<class C> void mini(C&a4, C b4){a4=min(a4, b4); }
template<class C> void maxi(C&a4, C b4){a4=max(a4, b4); }
template<class T1, class T2>
ostream& operator<< (ostream &out, pair<T1, T2> pair) { return out << "(" << pair.X << ", " << pair.Y << ")";}

struct pt3{
    int x[3];
    void read() {
        REP(i,3) cin >> x[i];
    }
    pt3 operator - (pt3 const &a) const {
        pt3 res;
        REP(i,3) res.x[i] = x[i] - a.x[i];
        return res;
    }
    pt3 operator + (pt3 const &a) const {
        pt3 res;
        REP(i,3) res.x[i] = x[i] + a.x[i];
        return res;
    }
    LL dist() const {
        LL res = 0;
        REP(i,3) res += (LL) x[i]*x[i];
        return res;
    }
    LL operator *(pt3 const &a) const {
        LL res = 0;
        REP(i,3) res += (LL) x[i]*(a.x[(i+1)%3] - a.x[(i+2)%3]);;
        return res;
    }

};

struct pr {
    LL d;
    LD v,t;
};

struct comet {
    pt3 pos;
    pt3 v;
};




pr compute(comet A, comet B) {
    pr res;
    pt3 p0 = A.pos - B.pos;
    pt3 p1 = A.pos + A.v - (B.pos + B.v);
    LL area = p0 * p1;
    LL delta = (p0-p1).dist();
    res.v = sqrtl(delta); 
    if (delta == 0) {
        res.d = p0.dist();
        res.t = 0;
        return res;
    }
    LL h = area*area/delta;
    LL l0 = p0.dist();
    LL delta0 = l0-h;
    LL l1 = p1.dist();
    bool plus = true;
    if (l1 > l0 + delta) plus = false;
    res.d = h;
    res.t = sqrtl((LD) delta0/delta);
    if (!plus) res.t *= -1;
    return res;
}
const LD eps = 1e-9;
const LD INF = 1e9;
// R squared
pair<LD,LD> frame(pr p, LD R) {
    if (R < p.d + eps) return MP(INF, -INF);
    if (p.v < eps) return MP(-INF,INF);
    LD d = sqrtl(R-p.d)/p.v;
    return MP(p.t -d, p.t+d);
}

typedef pair<LD, int> event;

struct edge{
    int to;
    LD on, off;
};

struct vertex {
    vector<edge> out;
    LD t0;

    vertex(): out(), t0(INF) {}

};

void solve(int tc) {
    cout << "Case #" << tc << ": ";
    int n,s;
    cin >> n >> s;
    vector<comet> V(n);
    REP(i,n) {
        V[i].pos.read();
        V[i].v.read();
    }
    vector<vector<pr> > W(n, vector<pr>(n));
    REP(i, n) REP(j,n) {
        W[i][j] = compute(V[i], V[j]);
      //  debug(MP(i,j));
     //   debug(MP(MP(W[i][j].d,W[i][j].v),W[i][j].t));
    }

    LD nd = (V[0].pos-V[1].pos).dist();
    LD bg = 0;
    REP(_, 100) {
        LD R = (bg + nd)/2;
        vector<vector<LD>> on(n, vector<LD>(n)), off(n, vector<LD>(n));
        vector<VI> who(n, VI(n, -1));
        vector<vertex> G;
        int target = -1;
        REP(i, n) {
            if (i == 1) target = SZ(G);
            G.PB(vertex());
            vector<event> E;
            REP(j,n) {
                if (j == i) continue; 
                auto a = frame(W[i][j], R);
                on[i][j] = a.X;
                off[i][j] = a.Y;
                if (a.X > a.Y) continue;
                //debug(MP(i,j));
                //debug(MP(on[i][j], off[i][j]));
                E.PB({a.X, -j-1});
                E.PB({a.Y+s, j+1});
            }
            if (i == 0) {
                E.PB({0, -1});
                E.PB({s, 1});
            }
            sort(ALL(E));
            int cnt = 0;

            for (event e : E) {
                int j = e.Y;
                if (j < 0) {
                    j = -j-1;
                    who[i][j] = SZ(G)-1;
                    ++cnt;
                } else {
                    --j;
                    --cnt;
                }
                if (cnt == 0) {
                    G.PB(vertex());
                }
            }
        }
        REP(i, n) REP(j,n) {
            if (i == j || who[i][j] == -1) continue;
            edge e;
            e.on = on[i][j];
            e.off = off[i][j];
            e.to = who[j][i];
           // debug(MP(i,j));
           // debug(MP(who[i][j], who[j][i]));
            G[who[i][j]].out.PB(e);
        }
        G[0].t0 = 0;
        priority_queue<pair<LD, int> > Q;
        Q.push({0,0});
        while(!Q.empty()) {
            auto t = Q.top();
            Q.pop();
            int i = t.Y;
            LD d = -t.X;
            if (G[i].t0 != d) continue;
            for (auto it : G[i].out) {
                if (it.off < d) continue;
                LD dt = min(d, it.on);
                if (G[it.to].t0 > dt) {
                    Q.push({-dt, it.to});
                    G[it.to].t0 = dt;
                }
            }
        }
        if (G[target].t0 != INF) {
            nd = R;
        } else {
            bg = R;
        }
    }
  //  debug(bg);
    cout << sqrtl(bg) << endl;

}


int main(){
    ios_base::sync_with_stdio(false);
    cout << fixed << setprecision(10);
    int T;
    cin >> T;
    REP(i,T) solve(i+1);


    return 0;
}


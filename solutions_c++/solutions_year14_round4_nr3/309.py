#include <algorithm>
#include <array>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <exception>
#include <fstream>
#include <functional>
#include <iostream>
#include <map>
#include <numeric>
#include <regex>
#include <set>
#include <sstream>
#include <stdexcept>
#include <string>
#include <tuple>
#include <typeinfo>
#include <vector>

using namespace std;
template <typename T, size_t N> struct ma : array<T,N> { T& operator[](size_t n) {
#ifdef DEBUG
           assert(n < N);
#endif
return (*static_cast<array<T,N>*>(this))[n]; } } ; 

typedef long long ll; typedef long double ld; typedef vector<int> vi; typedef vector<string> vs; typedef ostringstream oss; typedef istringstream iss; 

template<class T> string to_str(const T &a) { oss os; os << a; return os.str(); } 
template<> string to_str<ld>(const ld& a) { oss os; os.precision(10); os.setf(ios::fixed); os << a; return os.str(); } 
template<class T> T from_str(const string &s) { iss is; T val; is >> val; return val; }
#define rep(i,b) for(auto i=(0);i<(b);++i)
#define fo(i,a,b) for(auto i=(a);i<=(b);++i)
#define ford(i,a,b) for(auto i=(a);i>=(b);--i)
#define fore(a,b) for(auto &a:(b))
#define v vector
#define pb push_back
#define all(x) (x).begin(),(x).end()
#define clr(x,a) memset(x,a,sizeof(x))


int cond = (ll)1;
#define db(x...) { if (cond > 0) { cond--; rep (xxx, 1) cerr << __LINE__ << " " << #x << " " << x << endl; cerr.flush(); } }
#define dbv(x, a, b) { if (cond > 0) { cerr << __LINE__<<": " << #x << " "; for (auto __it = (x).begin() + (a); __it < (x).begin() + (b); __it++) cerr << *__it <<" "; cerr << endl; } cerr.flush(); }

template <class C, class=typename C::iterator> struct _cprint { }; 
template<> struct _cprint<string> {};
template <class C, class=typename _cprint<C>::type> ostream& operator<<(ostream &o, const C& v){ for(auto x:v) o<<x<<" "; return o; }

#define d4 array<int, 4>


#define pii pair<int, int>
#define x first
#define y second

namespace mf {
    const int nsz = 1000011;
    const int msz = 10000011;
    const int inf = 0x7f7f7f7f;
    vector<pii> ed[nsz];
    int fl[msz], dist[nsz], qq[nsz];
    int n, mid = 0;
    vector<pii>::iterator kr[nsz];
    
    void init(int n_) { n = n_; mid = 0; rep (i, n) ed[i].clear(); }
    
    void add_edge(int i, int j, int fleft, int fright) {
        ed[i].pb(pii(j, mid));
        fl[mid++] = fleft;
        ed[j].pb(pii(i, mid));
        fl[mid++] = fright;
        //assert(mid < msz);
    }
    
    bool bfs(int sta, int end) {
        rep (i, n) dist[i] = inf;
        int ss = 0, ee = 0;
        dist[sta] = 0; qq[ee++] = sta;
        while (ss < ee) {
            int top = qq[ss++];
            fore (it, ed[top]) if (fl[it.y] > 0 && dist[it.x] == inf) {
                dist[it.x] = dist[top] + 1;
                qq[ee++] = it.x;
            }
        }
        return dist[end] != inf;
    }
    
    int dfs(int i, int flow, int end) {
        if (flow == 0) return 0;
        if (i == end) return flow;
        int ret = 0;
        for (vector<pii>::iterator &it = kr[i]; it != ed[i].end(); ++it)
            if (dist[it->x] == dist[i] + 1 && fl[it->y] > 0) {
                int tadd = dfs(it->x, min(fl[it->y], flow), end);
                ret += tadd;
                flow -= tadd;
                fl[it->y] -= tadd;
                fl[it->y^1] += tadd;
                if (flow == 0) break;
            }
        return ret;
    }
    
    int flow(int sta, int end) {
        int ret = 0;
        while (bfs(sta, end)) {
            rep (i, n) kr[i] = ed[i].begin();
            ret += dfs(sta, inf, end);
        }
        return ret;
    }
};




int ary[3333][3333];

void solve() { db(1);
    int W, H, B;
    cin >> W >> H >> B;
    vector<d4> dat(B);
    rep (i, B) {
        rep (j, 4) cin >> dat[i][j];
        rep (j, 4) dat[i][j]++;
    }

    v<int> dx, dy;
    dx.pb(0); dx.pb(W+1);
    dy.pb(0); dy.pb(H+1);
    fo (i, 1, W) dx.pb(i);
    fo (i, 1, H) dy.pb(i);
    rep (i, B) {
        dx.pb(dat[i][0]);
        dx.pb(dat[i][2]);
        dy.pb(dat[i][1]);
        dy.pb(dat[i][3]);
        assert(dat[i][0] <= dat[i][2]);
        assert(dat[i][1] <= dat[i][3]);
        if (dat[i][0] != 0)
            dx.pb(dat[i][0] - 1);
        if (dat[i][1] != 0)
            dy.pb(dat[i][1] - 1);
    }
    sort(all(dx)); sort(all(dy));
    dx.erase(unique(all(dx)), dx.end());
    dy.erase(unique(all(dy)), dy.end());

    rep (i, B) {
        dat[i][0] = lower_bound(all(dx), dat[i][0]) - dx.begin();
        dat[i][2] = lower_bound(all(dx), dat[i][2]) - dx.begin();

        dat[i][1] = lower_bound(all(dy), dat[i][1]) - dy.begin();
        dat[i][3] = lower_bound(all(dy), dat[i][3]) - dy.begin();
    }
    db("");

//   W = dx.size() - 2;
// H = dy.size() - 2;
    fo (x, 0, W+1) fo (y, 0, H+1) ary[x][y] = (x == 0 || x == W+1 || y == 0 || y == H+1) ? 1 : 0;

    rep (i, B) {
        fo (x, dat[i][0], dat[i][2])
            fo (y, dat[i][1], dat[i][3]) {
                ary[x][y] = 1;
            }
    }
    db("");

        
    /*
    if (cond)
    fo (y, 1, H) {
        fo (x, 1, W) cerr << ary[x][y] <<" ";
        cerr << endl;
    }
    */

    db("");
    int X = H+4;
    db(X);
    db(2*X*(W+4));
    mf::init(2*X*(W+5));
    db("");

    fo (x, 1, W) fo (y, 1, 1) mf::add_edge(0, 2*(x*X + y), 1, 0);
    fo (x, 1, W) fo (y, H, H) mf::add_edge(2*(x*X + y) + 1, 1, 1, 0);

    db("");
    fo (y, 1, H) {
        fo (x, 1, W) {
            if (y+1<=H) mf::add_edge(2*(x*X + y)+1, 2*(x*X + y+1), 1, 0);
            if (x+1<=W) mf::add_edge(2*(x*X + y)+1, 2*((x+1)*X + y), 1, 0);
            if (y+1>=1) mf::add_edge(2*(x*X + y)+1, 2*(x*X + y-1), 1, 0);
            if (x+1>=1) mf::add_edge(2*(x*X + y)+1, 2*((x-1)*X + y), 1, 0);
            if (ary[x][y] == 0)
                mf::add_edge(2*(x*X + y), 2*(x*X + y) + 1, 1, 0);
        }
    }
    db("");
    int xx = mf::flow(0, 1);
    db("");
    db(xx);
    cout << xx;

}

void brute() {}
void gen() {}

int main(int argc, char ** argv) {
    ios::sync_with_stdio(false);
    //  freopen("../1.in","r",stdin); 
    //  freopen("../2.in","r",stdin); 
    //  freopen("../3.in","r",stdin); 
    //  freopen("../A-small.in","r",stdin); freopen("../A-small.out","w",stdout);
    //  freopen("../A-small-attempt0.in","r",stdin);freopen("../A-small-attempt0.out","w",stdout);
    //  freopen("../A-small-attempt1.in","r",stdin);freopen("../A-small-attempt1.out","w",stdout);
    //  freopen("../A-small-attempt2.in","r",stdin);freopen("../A-small-attempt2.out","w",stdout);
    //  freopen("../A-large.in","r",stdin); freopen("../A-large.out","w",stdout)

    cond = argc >= 2 && argv[1][0] == 'q' ? 1000 : 0;
    int t;
    cin>>t;
    for (int i = 1; i <= t; i++) {
        if (cond)
            cerr << __LINE__ << " " << i << endl;
        cout << "Case #" << i << ": ";
        solve();
        cout << endl;
        cout.flush();
        cerr.flush();
    }
	return 0;
}


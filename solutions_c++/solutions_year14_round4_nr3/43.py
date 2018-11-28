
#include<algorithm>
#include<cassert>
#include<complex>
#include<map>
#include<iomanip>
#include<sstream>
#include<queue>
#include<set>
#include<string>
#include<vector>
#include<iostream>
#include<cstring>
#define FOR(i, a, b) for(int i =(a); i <=(b); ++i)
#define FORD(i, a, b) for(int i = (a); i >= (b); --i)
#define fup FOR
#define fdo FORD
#define REP(i, n) for(int i = 0;i <(n); ++i)
#define VAR(v, i) __typeof(i) v=(i)
#define FORE(i, c) for(VAR(i, (c).begin()); i != (c).end(); ++i)
#define ALL(x) (x).begin(), (x).end()
#define SZ(x) ((int)(x).size())
#define siz SZ
#define CLR(x) memset((x), 0, sizeof(x))
#define PB push_back
#define MP make_pair
#define X first
#define Y second 
#define FI X
#define SE Y
#define SQR(a) ((a)*(a))
#define DEBUG 1
#define debug(x) {if (DEBUG)cerr <<#x <<" = " <<x <<endl; }
#define debugv(x) {if (DEBUG) {cerr <<#x <<" = "; FORE(it, (x)) cerr <<*it <<", "; cout <<endl; }}
using namespace std;

typedef long long LL;
typedef long double LD;
typedef pair<int, int> P;
typedef vector<int> VI;
const int INF=1E9+7;
template<class C> void mini(C&a4, C b4) { a4 = min(a4, b4); }
template<class C> void maxi(C&a4, C b4) { a4 = max(a4, b4); }

#define MAXN 200005

struct MaxFlow1 { // indeksy: 1..n, dozwolone krawedzie wielokrotne
    int n, d;
    VI c, v, G[MAXN+1];
    bool vis[MAXN+1];

    void init(int n_) {
        n = n_;
        c.clear();
        v.clear();
        FOR(i,1,n) G[i].clear();
    }

    void add(int a,int b,int cc=1) {
        G[a].PB(SZ(v)); v.PB(b); c.PB(cc);
        G[b].PB(SZ(v)); v.PB(a); c.PB(0);
    }

    bool aug(int x) {
        if(x == d) return true;
        vis[x] = true;
        FORE(i,G[x])
            if(!vis[v[*i]] && c[*i] > 0 && aug(v[*i])) {
                c[*i]--; c[1^*i]++;
                return true;
            }
        return false;
    }

    int flow(int s,int d_) {
        d = d_;
        int res = 0;
        while(aug(s)) {
            CLR(vis); // mozna zamienic na petle, jesli duzo malych flowow
            res++;
        }
        CLR(vis);
        return res;
    }

};

struct MaxFlow1Wrapper {
    MaxFlow1 f;
    void init(int n) {f.init(2*n);}
    void add(int a,int b,int c=1) {f.add(2*a, 2*b-1, c);}
    int flow(int s, int d) {
        FOR(i,1,f.n/2) f.add(2*i-1, 2*i);
        return f.flow(2*s, 2*d-1);
    }
};


#define maxn 505
bool zle[maxn][maxn];
MaxFlow1Wrapper F;
int dx[] = {1, 0, -1, 0};
int dy[] = {0, 1, 0, -1};
int w, h, b;
bool oki(int x, int y) { return x >= 0 && x < w && y >= 0 && y < h; }
int num[maxn][maxn];
int main(){
    ios_base::sync_with_stdio(false);
    int cas;
    cin >> cas;
    fup(cc, 1, cas) {
        cin >> w >> h >> b;
        F.init(w * h + 5);
        int a = 0;
        fup(i, 0, w - 1) fup(j, 0, h - 1) num[i][j] = ++a;
        CLR(zle);
        fup(i, 1, b) { 
            int x0, y0, x1, y1;
            cin >> x0 >> y0 >> x1 >> y1;
            fup(a, x0, x1) fup(b, y0, y1) zle[a][b] = 1;
        }

        fup(i, 0, w - 1) fup(j, 0, h - 1) {
            fup(k, 0, 3) {
                int xx = i + dx[k];
                int yy = j + dy[k];
                if (oki(xx, yy) && !zle[i][j] && !zle[xx][yy]) {
//                    cout << "ADD " << i << " " << j << " " << xx << " " << yy << endl;
                    F.add(num[i][j], num[xx][yy]);
                }
            }
        }
        int s = a + 1;
        int t = a + 2;
        fup(i, 0, w - 1) {
            if (!zle[i][0])
            F.add(s, num[i][0]);
            if (!zle[i][h - 1])
            F.add(num[i][h - 1], t);
        }
        cout << "Case #" << cc << ": ";
        cout << F.flow(s, t) << endl;
    }

    return 0;
}


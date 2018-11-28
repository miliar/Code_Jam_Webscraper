/*********************************************************************\
   |--\        ---       /\        |-----------| -----   /-------|    |
   |   \        |       /  \       |               |    /             |
   |    \       |      /    \      |               |   |              |
   |     \      |     /      \     |               |   |----|         |
   |      \     |    / ------ \    |-------|       |        |-----|   |
   |       \    |   /          \   |               |              |   |
   |        \   |  /            \  |               |              /   |
  ---        -------            ------           ----- |---------/    |
                                                                      |
    codeforces = nfssdq  ||  topcoder = nafis007                      |
    mail = nafis_sadique@yahoo.com || nfssdq@gmail.com                |
    IIT,Jahangirnagar University(41)                                  |
                                                                      |
**********************************************************************/

#include <bits/stdc++.h>

using namespace std;

#define xx         first
#define yy         second
#define pb         push_back
#define mp         make_pair
#define LL         long long
#define inf        INT_MAX/3
#define mod        1000000007ll
#define PI         acos(-1.0)
#define linf       (1ll<<60)-1
#define FOR(I,A,B) for(int I = (A); I < (B); ++I)
#define REP(I,N)   FOR(I,0,N)
#define ALL(A)     ((A).begin(), (A).end())
#define set0(ar)   memset(ar,0,sizeof ar)
#define vsort(v)   sort(v.begin(),v.end())
#define setinf(ar) memset(ar,126,sizeof ar)

//cout << fixed << setprecision(20) << p << endl;

template <class T> inline T bigmod(T p,T e,T M){
    LL ret = 1;
    for(; e > 0; e >>= 1){
        if(e & 1) ret = (ret * p) % M;
        p = (p * p) % M;
    } return (T)ret;
}
template <class T> inline T gcd(T a,T b){if(b==0)return a;return gcd(b,a%b);}
template <class T> inline T modinverse(T a,T M){return bigmod(a,M-2,M);}


char pp[111][111];
int vis[111][111], n, m;
int nxt[4][2] = { {-1, 0}, {0, -1}, {1, 0}, {0, 1} };
map < char, int > mm;
int go(int x, int y, char p){
//    cout << x << " " << y << endl;
    if(x < 0 || y < 0 || x >= n || y >= m) return 1;
    if(vis[x][y] == 1 && pp[x][y] != '.') return 0;
    vis[x][y] = 1;
    if(pp[x][y] != '.') p = pp[x][y];
    int c = mm[p];
    int x1 = x + nxt[c][0];
    int y1 = y + nxt[c][1];
    return go(x1, y1, p);
}
int main() {
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    mm['^'] = 0;
    mm['<'] = 1;
    mm['v'] = 2;
    mm['>'] = 3;
    ios_base::sync_with_stdio(0); cin.tie(0);
    int T; cin >> T;
    FOR(ts, 1, T+1){
        cin >> n >> m;
        REP(i, n) cin >> pp[i];
        set0(vis);
        int fl = 0, res = 0;
        REP(i, n){
            REP(j, m){
                if(vis[i][j] || pp[i][j] == '.') continue;
                int f1 = 0;
                REP(k, n) if(k != i && pp[k][j] != '.') f1 = 1;
                REP(k, m) if(k != j && pp[i][k] != '.') f1 = 1;
                if(f1 == 0) fl = 1;
                res += go(i, j, pp[i][j]);
            }
        }

        cout << "Case #" << ts << ": ";
        cerr << "Case #" << ts << ": ";

        if(fl == 0) {
            cout << res << endl;
            cerr << res << endl;
        } else {
            cout << "IMPOSSIBLE" << endl;
            cerr << "IMPOSSIBLE" << endl;
        }
    }
}

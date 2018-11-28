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
#define PI         2.0*acos(0.0)
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


    struct edge {
        int a, b, cap, flow ;
        edge(int _a,int _b,int _c,int _d) {
            a=_a,b=_b,cap=_c,flow=_d;
        }
    } ;

    int INF = 1500000001 ;

    int n, s, t, d [ 120001 ] , ptr [ 120001 ] , q [ 120001 * 10 ] ;
    vector < edge > e ;
    vector < int > g [ 120001 ] ;

    void add_edge ( int a, int b, int cap ) {
        edge e1 =edge( a, b, cap, 0 ) ;
        edge e2 =edge( b, a, 0 , 0 ) ;
        g [ a ] . push_back ( ( int ) e. size ( ) ) ;
        e. push_back ( e1 ) ;
        g [ b ] . push_back ( ( int ) e. size ( ) ) ;
        e. push_back ( e2 ) ;
    }

    bool bfs ( ) {
        int qh = 0 , qt = 0 ;
        q [ qt ++ ] = s ;
        memset ( d, -1 , sizeof d ) ;
        d [ s ] = 0 ;
        while ( qh < qt && d [ t ] == - 1 ) {
            int v = q [ qh ++ ] ;
            for ( size_t i = 0 ; i < g [ v ] . size ( ) ; ++ i ) {
                int id = g [ v ] [ i ] ,
                    to = e [ id ] . b ;
                if ( d [ to ] == - 1 && e [ id ] . flow < e [ id ] . cap ) {
                    q [ qt ++ ] = to ;
                    d [ to ] = d [ v ] + 1 ;
                }
            }
        }
        return d [ t ] != - 1 ;
    }

    int dfs ( int v, int flow ) {
        if ( ! flow )  return 0 ;
        if ( v == t )  return flow ;
        for ( ; ptr [ v ] < ( int ) g [ v ] . size ( ) ; ++ ptr [ v ] ) {
            int id = g [ v ] [ ptr [ v ] ] ,
                to = e [ id ] . b ;
            if ( d [ to ] != d [ v ] + 1 )  continue ;
            int pushed = dfs ( to, min ( flow, e [ id ] . cap - e [ id ] . flow ) ) ;
            if ( pushed ) {
                e [ id ] . flow += pushed ;
                e [ id ^ 1 ] . flow -= pushed ;
                return pushed ;
            }
        }
        return 0 ;
    }

    int dinic ( ) {
        int flow = 0 ;
        for ( ;; ) {
            if ( !bfs () )  break ;
            memset ( ptr, 0 , sizeof ptr ) ;
            while ( int pushed = dfs ( s, INF ) ) {
                flow += pushed ;
                if(pushed == 0)break;
            }
        }
        return flow ;
    }


int ar[101][501], pos[101][501];
int nxt[4][2] = { {-1, 0}, {1, 0}, {0, 1}, {0, -1} };
main(){
    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);
    ios_base::sync_with_stdio(0); cin.tie(0);
    LL a,b,c,d1 = 0,e1 = 0,f = 0,g1,h = 0,x = 0,y,z;
    cin >> a;
    FOR(ts, 1, a + 1){
        cout << "Case #" << ts << ": ";
        cerr << "Case #" << ts << ": ";
        cin >> b >> c >> d1;
        set0(ar);
        REP(i, d1){
            cin >> e1 >> f >> g1 >> h;
            for(int j = min(e1, g1); j <= max(e1, g1); j++){
                for(int k = min(f, h); k <= max(f, h); k++) ar[j][k] = 1;
            }
        }
        e1 = 0;
        for(int i = 0; i < b; i++){
            for(int j = 0; j < c; j++){
                e1++;
                pos[i][j] = e1;
                e1++;
            }
        }
        REP(i, 120000) g[i].clear();
        e.clear();
        n = e1 + 5; s = 0; t = e1 + 1;
        for(int i = 0; i < b; i++){
            for(int j = 0; j < c; j++){
                if(ar[i][j] == 1) continue;
                add_edge(pos[i][j], pos[i][j] + 1, 1);
                for(int k = 0; k < 4; k++){
                    x = i + nxt[k][0];
                    y = j + nxt[k][1];
                    if(x < 0 || x >= b || y < 0 || y >= c || ar[x][y] == 1) continue;
                    add_edge(pos[i][j] + 1, pos[x][y], 1);
                }
            }
        }
        for(int i = 0; i < b; i++){
            add_edge(0, pos[i][0], 1);
            add_edge(pos[i][c - 1] + 1, e1 + 1, 1);
        }
        f = dinic();
        cout << f << endl;
        cerr << f << endl;
     }
}


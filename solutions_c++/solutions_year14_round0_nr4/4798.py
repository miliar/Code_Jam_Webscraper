//{ Template
using namespace std;
//{ C-headers
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>
#include <climits>
#include <cfloat>
#include <cctype>
#include <cassert>
#include <ctime>
//}
//{ C++-headers
#include <iostream>
#include <iomanip>
#include <sstream>
#include <algorithm>
#include <utility>
#include <string>
#include <stack>
#include <queue>
#include <vector>
#include <set>
#include <map>
//}
//{ Loops
#define forab(i,a,b) for (__typeof(b) i = (a); i <= (b); ++i)
#define rep(i,n) forab (i, 0, (n) - 1)
#define For(i,n) forab (i, 1, n)
#define rofba(i,a,b) for (__typeof(b) i = (b); i >= (a); --i)
#define per(i,n) rofba (i, 0, (n) - 1)
#define rof(i,n) rofba (i, 1, n)
#define forstl(i,s) for (__typeof ((s).end ()) i = (s).begin (); i != (s).end (); ++i)
//}
//{ Floating-points
#define EPS 1e-10
#define abs(x) (((x) < 0) ? - (x) : (x))
#define zero(x) (abs (x) < EPS)
#define equal(a,b) (zero ((a) - (b)))
#define PI 2 * acos (0.0)
//}
#define max(a,b) (a)>(b)?(a):(b)
#define min(a,b) (a)<(b)?(a):(b)
#define memo(a,v) memset(a,v,sizeof(a))
#define all(a) a.begin(),a.end()
#define INF 1<<29
#define ll long long
#define db double
#define pb push_back
#define pii pair<int ,int >
#define NL puts("")
#define N 105
//{
//Intput_Output
#define II ({ int a; scanf("%d",&a); a;})
#define IL ({ ll a; scanf("%lld",&a);  a;})
#define ID ({ db a; scanf("%lf",&a);  a;})
#define IC ({ char a; scanf("%c",&a);  a;})
#define IS ({ string a; cin >> a;  a;})
#define ICA(n) ({ char a[n]; scanf("%s",&a);  a;})
#define OC printf("Case #%d:",cs);
#define FI freopen("in.txt","r",stdin);
#define FO freopen("out.txt","w",stdout);
//}
//}

//int dx[]={1,0,-1,0};int dy[]={0,1,0,-1}; //4 Direction
//int dx[]={1,1,0,-1,-1,-1,0,1};int dy[]={0,1,1,1,0,-1,-1,-1};//8 direction
//int dx[]={2,1,-1,-2,-2,-1,1,2};int dy[]={1,2,2,1,-1,-2,-2,-1};//Knight Direction
//int dx[6]={2,1,-1,-2,-1,1};int dy[6]={0,1,1,0,-1,-1}; //Hexagonal Direction

int cost[N][N], n, max_match;
int lx[N], ly[N];
int xy[N], yx[N];
bool S[N], T[N];
int slack[N], slackx[N], prev[N];

void init_labels() {
    memset( lx, 0, sizeof(lx) );
    memset( ly, 0, sizeof(ly) );
    for( int x = 0; x < n; x++ ) for( int y = 0; y < n; y++ ) lx[x] = max(lx[x], cost[x][y]);
}
void update_labels() {
    int x, y, delta = INF;
    for (y = 0; y < n; y++) if (!T[y]) delta = min(delta, slack[y]);
    for (x = 0; x < n; x++) if (S[x]) lx[x] -= delta;
    for (y = 0; y < n; y++) if (T[y]) ly[y] += delta;
    for (y = 0; y < n; y++) if (!T[y]) slack[y] -= delta;
}
void add_to_tree( int x, int prevx ) {
    S[x] = true;
    prev[x] = prevx;
    for (int y = 0; y < n; y++)
        if (lx[x] + ly[y] - cost[x][y] < slack[y]) {
            slack[y] = lx[x] + ly[y] - cost[x][y];
            slackx[y] = x;
        }
}
void augment() {
    if( max_match == n ) return;
    int x, y, root;
    int q[N], wr = 0, rd = 0;
    memset(S, false, sizeof(S));
    memset(T, false, sizeof(T));
    memset(prev, -1, sizeof(prev));
    for( x = 0; x < n; x++ ) if (xy[x] == -1) {
            q[wr++] = root = x;
            prev[x] = -2;
            S[x] = true;
            break;
        }
    for( y = 0; y < n; y++ ) {
        slack[y] = lx[root] + ly[y] - cost[root][y];
        slackx[y] = root;
    }
    while( true ) {
        while( rd < wr ) {
            x = q[rd++];
            for( y = 0; y < n; y++ )
                if( cost[x][y] == lx[x] + ly[y] && !T[y] ) {
                    if( yx[y] == -1 ) break;
                    T[y] = true;
                    q[wr++] = yx[y];
                    add_to_tree( yx[y], x);
                }
            if(y < n) break;
        }
        if(y < n) break;
        update_labels();
        wr = rd = 0;

        for(y = 0; y < n; y++) if(!T[y] &&  slack[y] == 0) {
                if(yx[y] == -1) {
                    x = slackx[y];
                    break;
                } else {
                    T[y] = true;
                    if (!S[yx[y]]) {
                        q[wr++] = yx[y];
                        add_to_tree(yx[y], slackx[y]);
                    }
                }
            }
        if(y < n) break;
    }
    if(y < n) {
        max_match++;
        for( int cx = x, cy = y, ty; cx != -2; cx = prev[cx], cy = ty ) {
            ty = xy[cx];
            yx[cy] = cx;
            xy[cx] = cy;
        }
        augment();
    }
}
int hungarian() {
    int ret = 0;
    max_match = 0;
    memset(xy, -1, sizeof(xy));
    memset(yx, -1, sizeof(yx));
    init_labels();
    augment();
    for(int x = 0; x < n; x++) {
        ret += cost[x][xy[x]];
    }
    return ret;
}


int main() {
#ifdef Sanim
    freopen ("in.txt", "r", stdin);
    freopen ("output.txt", "w", stdout);
#endif

    int t = II;
    For(cs,t) {
        n = II;
        db a1[N],a2[N];
        rep(i,n)
        a1[i] = ID;
        rep(i,n)
        a2[i] = ID;
        memo(cost,0);
        rep(i,n) {
            rep(j,n) {
                if(a1[i]<a2[j])
                    cost[i][j] = 0;
                else
                    cost[i][j] = 1;
            }
        }
        OC;
        printf(" %d ",hungarian());
        memo(cost,0);
        rep(i,n) {
            rep(j,n) {
                if(a1[i]>a2[j])
                    cost[i][j] = 0;
                else
                    cost[i][j] = 1;
            }
        }
        printf(" %d\n",n-hungarian());

    }
}

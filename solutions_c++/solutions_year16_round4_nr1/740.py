#include <bits/stdc++.h>
using namespace std;

typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;

#define mp make_pair
#define pb push_back
#define fi first
#define se second
#define forn(i,a,b) for( int i = (a); i < (b); i++ )
#define rep(i,n) forn(i,0,n)
#define repe(i,n) for( i = 0; i < (n); i++ )
#define pii pair<int,int>
#define pdd pair<double,double>
#define pll pair<ll,ll>


const int MXN = 20; 

int cc [3] = {'P', 'R', 'S'};

int w [3][MXN];

void out(int c, int n){
    if(n==0){
        printf("%c", cc[c]);
        return;
    }
    int a = c;
    int b = (c+1) % 3;
    if(w[a][n-1] > w[b][n-1]) swap(a,b);
    out(a,n-1);
    out(b,n-1);
}

void solve(){
    int n, p, r, s;
    scanf("%d%d%d%d", &n, &r, &p, &s);
    
    rep(i,n){
        int P = (p+r+s) / 2;
        int p1 = P - s;
        int r1 = P - p;
        int s1 = P - r;
        p = p1;
        r = r1;
        s = s1;
        if( p < 0 || r < 0 || s < 0 ){
            printf("IMPOSSIBLE");
            return;        
        }
    }
    w[0][0] = 0;
    w[1][0] = 1;
    w[2][0] = 2;
    forn(i,1,n){
        vector<pair<pii, int> > v { mp(mp(w[0][i-1], w[1][i-1]), 0), mp(mp(w[1][i-1], w[2][i-1]), 1), mp(mp(w[2][i-1], w[0][i-1]), 2) };
        for(auto& q : v){
            if(q.fi.fi > q.fi.se){
                swap(q.fi.fi, q.fi.se);
            }
        }
        sort(v.begin(), v.end());
        rep(j,3){
            w[v[j].se][i] = j;
        }
    }
    if(p) out(0, n);
    if(r) out(1, n);
    if(s) out(2, n);
}

int main() {
    freopen("A-large.in", "r", stdin); freopen("output.txt", "w", stdout);
    

    int T;
    scanf("%d", &T);
    
    rep(i,T){
        printf("Case #%d: ", i+1);
        solve();
        printf("\n");
    }

    return 0;
}

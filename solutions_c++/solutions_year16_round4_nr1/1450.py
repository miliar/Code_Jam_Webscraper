// Time erodes gratitude more quickly than it does beauty!
#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef pair<int,int> pii;
typedef pair<ll,ll> pll;
typedef vector<int> vi;
typedef vector<ll> vll;

#define X first
#define Y second
#define rep(i,n) for(int i = 0, _n = (n); i != _n; i++)
#define rep1(i,a,b) for(int i = a, _b = (b); i <= _b; i++)
#define rep2(i,b,a) for(int i = b, _a = (a); i >= _a; i--)
#define mem(a,val) memset(a, (val), sizeof a)
#define mp make_pair
#define mt make_tuple
#define eb emplace_back
#define all(c) (c).begin(), (c).end()
#define uni(c) c.resize(distance(c.begin(), unique(all(c))))
#define fix(c,sz_val...) c.clear(); c.resize(sz_val);
#define tr(c,it) for(__typeof(c.begin()) it = c.begin(); it != c.end(); ++it)
#define cases int t; cin >> t; rep1(_t,1,t)
#define case(ans) "Case #" << _t << ": " << ans << "\n"
#define cout(d) cout << fixed << setprecision(d)
#define io ios_base::sync_with_stdio(false); cin.tie(NULL);
#define err(x) cerr << #x << " = " << x << '\n'
const int mod = 1e9 + 7;

int main() {
    freopen("A-large.in", "r", stdin);
    freopen("output.txt", "w", stdout);
    map<string,pair<string,string>> my[15];
    my[0]["P"]=mp("P","R"); my[0]["R"]=mp("R","S"); my[0]["S"]=mp("P","S");
    rep1(i,1,12) {
        for(auto x: my[i-1]) {
            string a = my[i-1][x.Y.X].X + my[i-1][x.Y.X].Y;
            string b = my[i-1][x.Y.Y].X + my[i-1][x.Y.Y].Y;
            if(a > b) my[i][x.Y.X + x.Y.Y] = mp(b,a);
            else my[i][x.Y.X + x.Y.Y] = mp(a,b);
        }
    }
    
    cases {
        int n, x, y, z, xx,yy,zz;
        cin>>n>>y>>x>>z;
        if(abs(x-y)>1 or abs(y-z)>1 or abs(z-x)>1) cout<<case("IMPOSSIBLE");
        else {
            rep(i,n) {
                xx=x+y-z;
                yy=y+z-x;
                zz=z+x-y;
                x=xx/2, y=yy/2, z=zz/2;
            }
            
            string s;
            if(x==1 and y==0 and z==0) s="P";
            else if(x==0 and y==1 and z==0) s="R";
            else if(x==0 and y==0 and z==1) s="S";
            else assert(1 == 2);
            
            rep(i,n) {
                // flatten(s);
                s = my[i][s].X + my[i][s].Y;
            }
            cout<<case(s);
        }
    }
    return 0;
}
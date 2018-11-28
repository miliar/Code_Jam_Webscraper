#include <bits/stdc++.h>
using namespace std;

#define forn(i,n) for(int i=0;i<(int)(n);i++)
#define si(c) ((int)(c).size())
#define forsn(i,s,n) for(int i = (int)(s); i<((int)n); i++)
#define dforsn(i,s,n) for(int i = (int)(n)-1; i>=((int)s); i--)
#define decl(v, c) typeof(c) v = c
#define forall(i, c) for(decl(i, c.begin()); i!=c.end(); ++i)
#define dforall(i, c) for(decl(i, c.rbegin()); i!=c.rend(); ++i)
#define all(c) (c).begin(), (c).end()
#define rall(c) (c).rbegin(), (c).rend()
#define D(a) cout << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair
typedef long long int tint;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<tint> vt;
typedef vector<vt> vvt;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;
typedef vector<pii> vpii;

int main() {
    ios_base::sync_with_stdio(false);

    freopen("a.in", "r", stdin);
    freopen("a.out", "w", stdout);

    int nc;
    cin >> nc;
    forn(c, nc) {
        cout << "Case #" << c+1 << ": ";
        int n; 
        cin >> n;
        vector<int> a(n);
        forn(i, n) cin >> a[i];

        int res=0, p=0;
        forn(i, n) {
            if (a[i]<=p) res+=p-a[i];
            p=a[i];
        } 
        cout << res << ' ';
        int mx=0;
        forn(i, n-1) mx=max(mx, a[i]-a[i+1]);
        res=0;
        forn(i, n-1) {
            res+=min(a[i], mx);
        }
        cout << res << endl;
    }

    return 0;
}

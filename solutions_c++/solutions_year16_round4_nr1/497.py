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
#define D(a) cerr << #a << "=" << a << endl;
#define pb push_back
#define mp make_pair
#define endl '\n'

typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vll;
typedef vector<vll> vvll;
typedef vector<double> vd;
typedef vector<vd> vvd;
typedef vector<bool> vb;
typedef vector<vb> vvb;
typedef vector<string> vs;
typedef pair<int,int> pii;

char c[] = {'P', 'R', 'S'};
string dp[14][3];

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0); cout.tie(0);

    forn(i,3) dp[0][i] = string(1,c[i]);

    forsn(l,1,14) {
        forn(r,3) {
            int x = r, y = (r+1)%3;
            dp[l][r] = min(dp[l-1][x] + dp[l-1][y], dp[l-1][y] + dp[l-1][x]);
        }
    }

    int ncas; cin >> ncas;
    forn(cas, ncas) {
        cout << "Case #" << cas+1 << ": ";
        int n, cnt[3];
        cin >> n >> cnt[1] >> cnt[0] >> cnt[2];

        string ans = "Z";
        forn(r,3) {
            int ncnt[3] = {0,0,0};
            for (auto c : dp[n][r]) {
                if (c == 'P') ncnt[0]++;
                if (c == 'R') ncnt[1]++;
                if (c == 'S') ncnt[2]++;
            }
            bool ok = true;
            forn(i,3) if (cnt[i] != ncnt[i]) ok = false;
            if (ok) ans = min(ans, dp[n][r]);
        }

        if (ans == "Z") cout << "IMPOSSIBLE\n";
        else cout << ans << '\n';
    }
    return 0;
}

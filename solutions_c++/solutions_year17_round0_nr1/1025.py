#include <bits/stdc++.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rall(v) v.rbegin(),v.rend()
#define sz size()
#define rep(i,m) for(int i=0;i<(int)(m);i++)
#define rep2(i,n,m) for(int i=n;i<(int)(m);i++)
#define For(it,c) for(__typeof(c.begin()) it=c.begin();it!=c.end();++it)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define popc32(x) __builtin_popcount(x)
#define popc64(x) __builtin_popcountll(x)
#define MOD 1000007
#define INF 1e9
#define EPS 1e-9

typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<double> vd;
typedef vector<vector<int> > vii;
typedef long long ll;
typedef long double ld;

static const double PI = 2 * acos(0);

int main() {
    ios::sync_with_stdio(false); cin.tie(0);
    //////////////start//////////////

    int T;
    cin >> T;
    for (int tc = 1; tc <= T; tc++) {
        cout << "Case #" << tc << ": ";

        string row;
        int flipper;
        cin >> row >> flipper;
        
        int flips = 0;
        vector<bool> wasflipped(row.sz);
        bool bad = false;
        while (true) {
            bool flipped = false;
            for (int i = 0; i < row.sz; i++) {
                if (row[i] == '-') {
                    int fliploc = i;
                    if (fliploc > row.sz-flipper) {
                        fliploc = row.sz-flipper;
                    }
                    rep(j, flipper) {
                        if (row[fliploc+j] == '-')
                            row[fliploc+j] = '+';
                        else
                            row[fliploc+j] = '-';
                    }
                    flips++;
                    if (wasflipped[fliploc])
                        bad = true;
                    wasflipped[fliploc] = true;
                    flipped = true;
                    break;
                }
            }
            if (bad)
                break;
            if (!flipped)
                break;
            if (flips > 1000)
                break;
        }

        if (bad)
            cout << "IMPOSSIBLE" << endl;
        else
            cout << flips << endl;
    }

    //////////////end////////////////
    return 0;
}

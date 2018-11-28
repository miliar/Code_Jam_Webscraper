#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
typedef unsigned long long ull;
typedef long double ld;
typedef pair<int,int> pii;
typedef vector<int> vi;
typedef stringstream ss;

#define sz(x) ((int)(x).size())
#define all(x) (x).begin(),(x).end()
#define mset(t,v) memset((t),(v),sizeof(t))
#define print(a) cout << #a << ": " << a << endl;
#define print_arr(a,n) rep(_##i, n) cout << #a << "[" << _##i << "]: " << a[_##i] << endl

#define rep(i,n) for(int i=0,_##i=(n);i<_##i;++i)
#define repr(i,n) for(int i=(n);--i>=0;)
#define rep2(i,l,r) for(int i=(l),_##i=(r);i<_##i;++i)
#define repr2(i,l,r) for(int i=(r),_##i=(l);--i>=_##i;)

#define vt(args...) vector<tuple<args>>
#define mp make_pair
#define pb push_back
#define eb emplace_back
#define em emplace

string grid[100];
int R, C;

bool good(int x, int y) {
    return x >= 0 && x < R && y >= 0 && y < C;
}

int X[500];
int Y[500];
int hasr[100];
int hasc[100];
void solve_case(int i) {
    cout << "Case #" << i << ": ";
    int ans;

    cin >> R >> C;
    rep(i, R) cin >> grid[i];
    ans = 0;
    rep(i, R){
        hasr[i] = 0;
        rep(j, C) {
            if (grid[i][j] != '.') {
                hasr[i]++;
            }
        }
    } 
    rep(j, C){
        hasc[j] = 0;
        rep(i, R) {
            if (grid[i][j] != '.') {
                hasc[j]++;
            }
        }
    }
    rep(i, R) {
        rep (j, C) {
            if (grid[i][j] != '.') {
                if (hasr[i] == 1 && hasc[j] == 1) {
                    cout << "IMPOSSIBLE\n";
                    return;
                }
                char c = grid[i][j];
                int x = i;
                int y = j;
                int xx = X[c];
                int yy = Y[c];
                x += xx;
                y += yy;
                bool ok = false;
                while (good(x, y)) {
                    if (grid[x][y] != '.') {
                        ok = true;
                        break;
                    }

                    x += xx;
                    y += yy;
                }
                if (!ok) ans++;
            }
        }
    }
    cout << ans << "\n";
}


int main(){
    X['>'] = 0;
    Y['>'] = 1;
    X['<'] = 0;
    Y['<'] = -1;
    X['^'] = -1;
    Y['^'] = 0;
    X['v'] = 1;
    Y['v'] = 0;
    int T;
    cin >> T;
    rep(i, T) solve_case(i + 1);
    return 0;
}


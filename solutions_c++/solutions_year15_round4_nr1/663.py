#include <iostream>
#include <algorithm>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <vector>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <cstring>
#include <fstream>
#include <ctime>
#include <iomanip>
#define LL long long
#define ULL unsigned long long
#define FOR(i,a,b) for(int i=a;i<=b;i++)
#define FO(i,a,b) for(int i=a;i<b;i++)
#define FORD(i,a,b) for(int i=a;i>=b;i--)
#define FOD(i,a,b) for(int i=a;i>b;i--)
#define FORV(i,a) for(typeof(a.begin()) i = a.begin(); i != a.end(); i++)
#define fi first
#define se second
#define pb push_back
#define mp make_pair
#define debug cout << "YES" << endl
#define REP(i, n) for (int i = 0; i < (int)(n); ++i)

using namespace std;

typedef pair<int, int>II;
typedef pair<int,II>PII;
template<class T> T gcd(T a, T b) {T r; while(b!=0) {r=a%b;a=b;b=r;} return a;}
template<class T> T lcm(T a, T b) { return a / gcd(a, b) * b; }
template<class T> int getbit(T s, int i) { return (s >> i) & 1; }
template<class T> T onbit(T s, int i) { return s | (T(1) << i); }
template<class T> T offbit(T s, int i) { return s & (~(T(1) << i)); }

const long double PI = 2*acos(0.0);
const long double eps = 1e-12;
const int infi = 1e9;
const LL Linfi = (LL) 1e18;
const LL MOD = 1000000007;
const int c1 = 31;
const int c2 = 37;
#define maxn 1000005

const int N = 110;
string s[N];
int t[N][N];
bool b[N][N][4];
int r, c;

void solve(){
    FOR(i,1,r) {
        FOR(j,1,c){
            if (s[i][j] == '>') t[i][j] = 0;
            else if (s[i][j] == '^') t[i][j] = 1;
            else if (s[i][j] == '<') t[i][j] = 2;
            else if (s[i][j] == 'v') t[i][j] = 3;
        }
    }

    memset(b, 0, sizeof(b));
    FOR(i,1,r){
        FOR(j,1,c)
            if (s[i][j] != '.') {
                b[i][j][2] = true;
                break;
            }
        FORD(j,c,1)
            if (s[i][j] != '.') {
                b[i][j][0] = true;
                break;
            }
    }

    FOR(j,1,c) {
        FOR(i,1,r)
            if (s[i][j] != '.') {
                b[i][j][1] = true;
                break;
            }
        FORD(i,r,1)
            if (s[i][j] != '.') {
                b[i][j][3] = true;
                break;
            }
    }

    int ans = 0;
    bool ok = true;
    for (int i = 1; i <= r && ok; ++i){
        for (int j = 1; j <= c && ok; ++j)
            if (s[i][j] != '.') {
                if (b[i][j][t[i][j]]) {
                    bool found = false;
                    for (int k = 0; k < 4; ++k)
                        if (b[i][j][k] == false) {
                            found = true;
                        }
                    if (found) {
                        ans++;
                    } else {
                        ok = false;
                    }
                }
            }
    }

    if (ok) cout << ans << endl;
    else cout << "IMPOSSIBLE" << endl;
}

int main() {
    ios::sync_with_stdio(false);
    #ifndef ONLINE_JUDGE
    freopen("test.in","r",stdin);
    freopen("test.out","w",stdout);
    #endif
    int sotest;
    cin >> sotest;
    FOR(test,1,sotest){
        cin >> r >> c;
        FOR(i,1,r) {
            cin >> s[i];
            s[i] = '0' + s[i];
        }
        cout << "Case #" << test << ": ";
        solve();
    }
}

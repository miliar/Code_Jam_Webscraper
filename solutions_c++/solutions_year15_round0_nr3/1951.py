//============================================================================
// Author    : LAM PHAN VIET - lamphanviet@gmail.com
//============================================================================
#include <bits/stdc++.h>
using namespace std;

#define fr(i,a,b) for (int i = (a), _b = (b); i <= _b; i++)
#define frr(i,a,b) for (int i = (a), _b = (b); i >= _b; i--)
#define rep(i,n) for (int i = 0, _n = (n); i < _n; i++)
#define repr(i,n) for (int i = (n) - 1; i >= 0; i--)
#define foreach(it, ar) for ( typeof(ar.begin()) it = ar.begin(); it != ar.end(); it++ )
#define fill(ar, val) memset(ar, val, sizeof(ar))

#define uint64 unsigned long long
#define int64 long long
#define all(ar) ar.begin(), ar.end()
#define pb push_back
#define mp make_pair
#define ff first
#define ss second

#define BIT(n) (1<<(n))
#define sqr(x) ((x) * (x))

typedef pair<int, int> ii;
typedef pair<int, ii> iii;
typedef vector<ii> vii;
typedef vector<int> vi;

#define PI  3.1415926535897932385
#define EPS 1e-7
#define MOD 1000000007
#define INF 1500111222
#define MAX 100111

const int mul[5][5] = {
    { 0, 0, 0, 0, 0 },
    { 0, 1, 2, 3, 4 },
    { 0, 2, -1, 4, -3 },
    { 0, 3, -4, -1, 2 },
    { 0, 4, 3, -2, -1 }
};

int len, rep, n, idx[300];
string s, os;
bool okk[MAX];

bool solve() {
    fill(okk, false);
    n = s.length();
    //cout << s << endl;
    rep(i, n) s[i] = idx[s[i]];
    int val = 1, sign = 1;
    repr(i, n) {
        val = mul[s[i]][val];
        //printf("k %d: %d\n", i, val);
        if (val < 0)
            val = -val, sign = -sign;
        if (val == 4 && sign > 0)
            okk[i] = true;
    }
    val = 1, sign = 1;
    rep(i, n) {
        val = mul[val][s[i]];
        //printf("i %d: %d\n", i, val);
        if (val < 0)
            val = -val, sign = -sign;
        if (val == 2 && sign > 0) {
            int valj = 1, signj = 1;
            for (int j = i + 1; j < n - 1; j++) {
                valj = mul[valj][s[j]];
                if (valj < 0) valj = -valj, signj = -signj;
                if (valj == 3 && signj > 0 && okk[j + 1])
                    return true;
            }
        }
    }
    return false;
}

int main() {
    #ifndef ONLINE_JUDGE
        freopen("test.inp", "r", stdin);
        freopen("test.out", "w", stdout);
    #endif
    rep(i, 300) idx[i] = i;
    idx['i'] = 2;
    idx['j'] = 3;
    idx['k'] = 4;
    int cases, caseNo = 0;
    for (scanf("%d", &cases); cases--; ) {
        scanf("%d %d", &len, &rep);
        cin >> os;
        s = "";
        rep(i, rep) s += os;
        printf("Case #%d: %s\n", ++caseNo, solve() ? "YES" : "NO");
    }
    return 0;
}
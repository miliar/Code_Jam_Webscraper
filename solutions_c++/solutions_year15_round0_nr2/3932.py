#include <bits/stdc++.h>
using namespace std;

typedef ostringstream OSS;
typedef istringstream ISS;

typedef long long LL;
typedef pair<int, int> PII;

typedef vector<int> VI;
typedef vector<VI> VVI;
typedef vector<LL> VLL;
typedef vector<VLL> VVLL;
typedef vector<string> VS;
typedef vector<VS> VVS;
typedef vector<bool> VB;
typedef vector<VB> VVB;
typedef vector<PII> VPII;

#define fst first
#define snd second
#define MP make_pair
#define PB push_back
#define EB emplace_back 
#define ALL(x) (x).begin(),(x).end()
#define RANGE(x,y,maxX,maxY) (0 <= (x) && 0 <= (y) && (x) < (maxX) && (y) < (maxY))
#define DUMP( x ) cerr << #x << " = " << ( x ) << endl

template < typename T > inline T fromString(const string &s) { T res; ISS iss(s); iss >> res; return res; };
template < typename T > inline string toString(const T &a) { OSS oss; oss << a; return oss.str(); };

const int INF = 0x3f3f3f3f;
const LL INFL = 0x3f3f3f3f3f3f3f3fLL;
const int DX[]={1,0,-1,0},DY[]={0,-1,0,1};

int dfs(VI ps, int cnt) {
    int max_i = max_element(ALL(ps)) - ps.begin();
    
    if (ps[max_i] == 0) return cnt;

    VI anss;
    
    VI ps1(ps);
    for (auto &p : ps1) {
        p = max(p - 1, 0);
    }

    anss.PB(dfs(ps1, cnt + 1));

//    if (ps[max_i] > 3) {
        for (int i = 2; i <= ps[max_i] / 2; i++) {
            VI ps2(ps);
            ps2.PB(i);
            ps2[max_i] -= i;
            anss.PB(dfs(ps2, cnt + 1));
        }
//    }

    return *min_element(ALL(anss));
}

int solve() {
    int D;
    cin >> D;
    VI P(D);
    for (auto &p : P) cin >> p;

    int ans = dfs(P, 0);
/*
    cout << D << ": ";
    for (auto p : P) cout << p << " ";
    cout << " = " << ans;
    cout << endl;
*/

    return ans;
}

int main(void) {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int ans = solve();

        printf("Case #%d: %d\n", i + 1, ans);
    }

	return 0;
}

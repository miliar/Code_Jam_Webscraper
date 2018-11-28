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

const string CHARS("01ijk");
int quat[5][5] = {
    {1, 1,  2,  3,  4},
    {1, 1,  2,  3,  4},
    {2, 2, -1,  4, -3},
    {3, 3, -4, -1,  2},
    {4, 4,  3, -2, -1}
};

int multiply(int a, int b) {
    int sign = (a < 0 ? -1 : 1) * (b < 0 ? -1 : 1);
    int num = quat[abs(a)][abs(b)];
    return sign * num;
}

int solve() {
    int X, L;
    string base_s;
    cin >> X >> L >> base_s;

    int N = X * L;
    
    VI ss(N);
    int sum = 1;
    for (int i = 0; i < N; i++) {
        ss[i] = CHARS.find(base_s[i % (int)base_s.size()]);
        sum = multiply(sum, ss[i]);
    }

    int a, b, c;
    a = 1;
    for (int l = 1; l < N - 1; l++) {
        a = multiply(a, ss[l - 1]);
        if (a != 2) continue;

        b = 1;
        for (int r = l + 1; r < N; r++) {
            b = multiply(b, ss[r - 1]);
            if (b != 3) continue;

            c = 1;
            for (int i = r; i < N; i++) {
                c = multiply(c, ss[i]);
            }

            if (c == 4) return true;
        }
    }

    return false;
}

int main(void) {
    int T;
    cin >> T;

    for (int i = 0; i < T; i++) {
        int ans = solve();

        printf("Case #%d: %s\n", i + 1, ans ? "YES" : "NO");
    }

	return 0;
}

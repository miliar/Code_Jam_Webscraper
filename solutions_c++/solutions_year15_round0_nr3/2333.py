#include <bits/stdc++.h>
using namespace std;

#define For(i,a,b) for(int i=(a);i<(int)(b);++i)
#define Ford(i,a,b) for(int i=(a);i>=(int)(b);--i)
#define Fore(i,c) for(int i=0;i<(int)(c).size();++i)
#define Iter(i,c) for(typeof((c).begin()) i=(c).begin();i!=(c).end();++i)
#define All(a) (a).begin(),(a).end()
#define Rall(a) (a).rbegin(),(a).rend()
#define Mem(a,v) memset((a),(v),sizeof(a))
#define Sz(a) ((int)(a).size())
#define gcd(a,b) __gcd((a),(b))
#define pb push_back
#define mp make_pair
#define ft first
#define sd second
#define gc getchar

typedef long long LL;
typedef unsigned long long ULL;
typedef vector<int> VI;
typedef pair<int, int> PII;

const int INF = 1001001001;
const int MOD = 1000000007;
const double EPS = 1e-8;

template<class T> inline void fromStr(const string& s,T& x){istringstream is(s);is>>x;}
template<class T> inline string toStr(const T& x){ostringstream os;os<<x;return os.str();}

template<class T>
inline void getNum(T& x) {
    x = 0; int s = 1; register int c = gc();
    while ((c < '0' || c > '9') && c != '-') c = gc();
    if (c == '-') s = -1, c = gc();
    for (; c >= '0' && c <= '9'; c = gc()) x = (x<<1) + (x<<3) + c-'0';
    x *= s;
}

int powmod(int a, int b, int m) {
    a %= m;
    int r = 1;
    while (b > 0) {
        if (b & 1) r = (r * 1LL * a) % m;
        a = (a * 1LL * a) % m;
        b >>= 1;
    }
    return r;
}

int mul[5][5] = {
    {0, 0, 0, 0, 0},
    {0, 1, 2, 3, 4},
    {0, 2, -1, 4, -3},
    {0, 3, -4, -1, 2},
    {0, 4, 3, -2, -1}
};

int multiply(int a, int b) {
    int s = 1;
    if (a < 0) s *= -1, a *= -1;
    if (b < 0) s *= -1, b *= -1;
    int ret = mul[a][b];
    return ret * s;
}

const int MAXL = 10005;
const string YES = "YES\n";
const string NO = "NO\n";

int L, val[MAXL], prodL[MAXL], prodR[MAXL];
LL X;
string s;

int intval(char c) {
    if (c == '1') return 1;
    return c - 'i' + 2;
}

LL findMinPrefix(const int pre, const int all, const int req) {
    if (pre == req) return 0;
    int allPow = all;
    For(i,1,4) {
        int val = multiply(allPow, pre);
        allPow = multiply(allPow, all);
        if (val == req) return i;
    }
    return -1;
}

LL findMinSuffix(const int suf, const int all, const int req) {
    if (suf == req) return 0;
    int allPow = all;
    For(i,1,4) {
        int val = multiply(suf, allPow);
        allPow = multiply(all, allPow);
        if (val == req) return i;
    }
    return -1;
}

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);

    int T;
    cin >> T;

    for (int testCase = 1; testCase <= T; ++testCase) {
        cout << "Case #" << testCase << ": ";

        cin >> L >> X;
        cin >> s;
        int n = L - 1;

        val[0] = intval(s[0]);
        prodL[0] = val[0];
        For(i, 1, Sz(s)) {
            val[i] = intval(s[i]);
            prodL[i] = multiply(prodL[i-1], val[i]);
        }

        prodR[n] = val[n];
        Ford(i,n-1,0) {
            prodR[i] = multiply(val[i], prodR[i+1]);
        }
        
        int all = prodL[n];

        int allPow = 1;
        int powM = X % 4;
        For(i, 0, powM) allPow = multiply(allPow, all);

        if (allPow != -1) {
            cout << NO;
            continue;
        }

        LL preI = -1;
        LL times = findMinPrefix(1, all, 2);
        if (times > 0) {
            preI = L * times;
        }
        For(i,0,L) {
            int v = prodL[i];
            LL times = findMinPrefix(v, all, 2);
            if (times < 0) continue;
            LL len = i + 1 + L * times;
            if (preI < 0 || len < preI)
                preI = len;
        }

        LL sufK = -1;
        times = findMinSuffix(1, all, 4);
        if (times > 0) {
            sufK = L * times;
        }
        For(i,0,L) {
            int v = prodR[i];
            LL times = findMinSuffix(v, all, 4);
            if (times < 0) continue;
            LL len = L - i + L * times;
            if (sufK < 0 || len < sufK)
                sufK = len;
        }


        if (preI < 0 || sufK < 0) {
            cout << NO;
            continue;
        }

        LL totalLen = L * X;
        LL reqLen = preI + sufK;
        if (reqLen >= totalLen) {
            cout << NO;
            continue;
        }

        cout << YES;
    }

    return 0;
}
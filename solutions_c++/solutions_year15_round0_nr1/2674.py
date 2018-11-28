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

string s;
int sn;

int main() {
    ios_base::sync_with_stdio(false); cin.tie(0);

    int T;
    cin >> T;

    for (int testCase = 1; testCase <= T; ++testCase) {
        cout << "Case #" << testCase << ": ";
        cin >> sn >> s;
        int n = 0, ans = 0;
        n += s[0] - '0';
        For(i, 1, Sz(s)) {
            int c = s[i] - '0';
            if (n < i) {
                ans += i - n;
                n = i;
            }
            n += c;
        }
        cout << ans << "\n";
    }

    return 0;
}
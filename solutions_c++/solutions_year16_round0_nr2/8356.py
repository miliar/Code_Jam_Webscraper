//
/*
ID: kfoozmi1
LANG: C++
TASK:
*/
#include <bits/stdc++.h>
using namespace std;

#ifdef kfoozminus
#define dbg(args...) do {cerr << #args << " : "; faltu(args); } while(0)

void faltu() {
	cerr << endl;
}

template <typename T>
void faltu(T a[], int n) {
	for(int i = 0; i < n; ++i) cerr << a[i] << ' ';
	cerr << endl;
}

template <typename First, typename ... hello>
void faltu(First arg, const hello&... rest) {
	cerr << arg << ' ';
	faltu(rest...);
}
#else
#define dbg(args...)
#endif

#define PB push_back
#define F first
#define S second
#define MKP make_pair
#define PI acos(-1)
#define INF 100000000
#define EPS 1e-9

#define B1 43
#define B2 43

#define MOD  1000000007
#define MOD1 1000000007
#define MOD2 1000000009

#define MX 100007

typedef long long ll;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

int dx[] = {0, 0, +1, -1};
int dy[] = {+1, -1, 0, 0};
int dxx[] = {+1, 0, -1, 0, +1, +1, -1, -1};
int dyy[] = {0, +1, 0, -1, +1, -1, +1, -1};

inline bool checkBit(ll n, int i) { return n & (1LL << i); }
inline ll setBit(ll n, int i) { return n | (1LL << i); }
inline ll resetBit(ll n, int i) { return n & (~ (1LL << i)); }
inline bool EQ(double a, double b) { return fabs(a-b) < EPS; }

ll bigMod(ll a, ll b)
{
	ll r = 1;
	while(b) {
		if(b & 1) (r *= a) %= MOD;
		b >>= 1;
		(a *= a) %= MOD;
	}
	return r;
}

int main()
{
#ifdef kfoozminus
	//freopen("in", "r", stdin);
	freopen("jamB", "w", stdout);
#endif

	int tc, cs, i, cnt, l;
	char s[200];

	scanf("%d", &tc);
	for(cs = 1; cs <= tc; cs ++) {

		printf("Case #%d: ", cs);

		scanf("%s", s);
		l = strlen(s);
		
		cnt = 0;
		char ch = '+';
		for(i = l - 1; i >= 0; i --) {

			if(s[i] != ch) {

				cnt ++;
				ch = s[i];
			}
		}

		printf("%d\n", cnt);
	}
        return 0;
}


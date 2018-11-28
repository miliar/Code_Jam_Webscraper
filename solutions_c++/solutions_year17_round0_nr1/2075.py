#include <cstdio>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <string>
#include <stack>
#include <queue>
#include <deque>
#include <vector>
#include <map>
#include <set>
#include <utility>
#include <algorithm>
#include <cmath>
#include <climits>
#ifdef DEBUG
    #include <ctime>
#endif
using namespace std;

// template

// abbreviations

typedef unsigned long long ull;
typedef long long ll;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ll> vl;
typedef vector<vl> vvl;
typedef vector<string> vs;
typedef pair<int, int> ii;
typedef vector<ii> vii;
typedef map<int, int> mii;
#define a first
#define b second
#define que queue
#define pque priority_queue
#define stk stack
#define pub push_back
#define pob pop_back
#define puf push_front
#define pof pop_front
#define pu push
#define po pop
#define mp make_pair
#define it iterator
#define sz(var) ((int) var.size())
#define rep(it, n) for(int it = 0; it < n; ++it)
#define dep(it, n) for(int it = n - 1; it >= 0; --it)
#define rep1(it, n) for(int it = 1; it <= n; ++it)
#define dep1(it, n) for(int it = n; it > 0; --it)
#define loop(it, from, to) for(int it = (from); it <= (to); ++it)
#define iter(it, cont) for(__typeof((cont).begin()) it = (cont).begin(); it != (cont).end(); ++it)
#define riter(it, cont) for(__typeof((cont).rbegin()) it = (cont).rbegin(); it != (cont).rend(); ++it)
#define all(cont) (cont).begin(), (cont).end()
#define rng(cont, n) cont, cont + n
#define memclr(var) memset(var, 0, sizeof(var))

const int INF = INT_MAX;
const int NINF = INT_MIN;
const ll INF_LL = LLONG_MAX;
const ll NINF_LL = LLONG_MIN;
const double PI = acos(-1.0);
const int MOD = 1e9 + 7;

inline ll pos_m(ll a, ll c = MOD) { while (a < 0) { a += c; } return a; }
inline ll add_m(ll a, ll b, ll c = MOD) { a = pos_m(a, c), b = pos_m(b, c); return (a + b) % c; }
// Russian multiplication O(log(min(a, b)))
// inline ll mul_m(ll a, ll b, ll c = MOD) { a = pos_m(a, c), b = pos_m(b, c); ll ret = 0; if (a < b) return mul_m(b, a, c); while (b) { if (b & 1) ret = add_m(ret, a, c); a = add_m(a, a, c); b >>= 1; } return ret; }
// Simple multiplication O(1), Note: works for a, b <= 10^9
inline ll mul_m(ll a, ll b, ll c = MOD) { a = pos_m(a, c), b = pos_m(b, c); return (a * b) % c; }
inline ll sub_m(ll a, ll b, ll c = MOD) { a = pos_m(a, c), b = pos_m(b, c); return pos_m((a - b) % c, c); }
inline ll pow_m(ll a, ll b, ll c = MOD) { a = pos_m(a, c); ll ret = 1; while (b) { if (b & 1) ret = mul_m(a, ret, c); a = mul_m(a, a, c); b >>= 1; } return ret; }

#ifdef DEBUG
    #define debug(fmt, args...) printf("Line %d, in %s\t: " fmt, __LINE__, __FUNCTION__, ##args)
    #define rep_rt() printf("[Run time: %.3fs]\n", ((double) clock()) / CLOCKS_PER_SEC)
#else
    #define debug(...)
#endif

// end of template

#define MAXS (int) (1e3 + 5)
#define MAXK (int) (1e3 + 5)

int get_ans(char *s, int k) {
	int len = strlen(s);
	int ans = 0;
	for (int i = 0; i < len; ++i) {
		char cur_c = s[i];
		if (cur_c == '-') {
			ans++;
			for (int j = i; j < i + k; ++j) {
				// it needs to flip pancakes which are less than K
				if (len <= j)
					return -1;

				char &c = s[j];
				if (c == '+')
					c = '-';
				else
					c = '+';
			}
		}
	}
	return ans;
}

int main() {
#ifdef DEBUG
    // freopen("A.in", "r", stdin);
    // freopen("A.out", "w", stdout);
#endif
    // freopen("A-large.in", "r", stdin);
    // freopen("A-large.out", "w", stdout);
    
    int nt;
    scanf("%d%*c", &nt);

    rep1(t, nt) {
    	char s[MAXS];
    	int k;
    	scanf("%s %d%*c", s, &k);

    	int ans = get_ans(s, k);
    	printf("Case #%d: ", t);
    	if (ans == -1) {
    		puts("IMPOSSIBLE");
    	} else {
    		printf("%d\n", ans);
    	}
    }

#ifdef DEBUG
    // rep_rt();
#endif
    return 0;
}
#include <bits/stdc++.h>
#include <assert.h>
//#include <unordered_map>
using namespace std;
 
typedef long long ll;
typedef double ld;
typedef vector < long long > vll;
typedef pair < long long, long long > pll;
typedef pair < int, int > pii;
typedef vector < int > vii;
typedef vector < vll > matrix;
 
#define rep(i,n) for(ll i = 0; i < n; i++)
#define reps(i,a,n) for(ll i = a; i < n; i++)
#define csl ios_base::sync_with_stdio(false); cin.tie(NULL)
#define l(x) (((x) << 1) | 1)
#define r(x) ((l(x)) + 1)
#define md(a,b) (((a) + (b)) >> 1LL)
#define INF ((1LL << 57LL))
#define pb push_back
#define mp make_pair
#define fst first
#define snd second
 
ll t, n, u, v, m, q, l, r, ql, qr, k, d, c;
const int N = 2505;
const int K = 95;
const ll mod = 10243;
const bool JUDGE = true;
multiset < ll > a;
ll A[N];
string ans;
int main(){
	csl;
	if (JUDGE) {
		freopen("B-large.in", "r", stdin);
		freopen("out.txt", "w", stdout);
	}
	cin >> t;
	for (int abcd = 1; abcd <= t; abcd++) {
		ll ans = INF;
		cin >> n;
		rep (i, n) cin >> A[i];
		ll ff = *max_element(A, A + n);
		ll kc = 0;
		for (int i = 1; i <= ff; ++i) {
			kc = 0;
			rep (j, n) {
				if (A[j] > i) {
					if (A[j] % i == 0) kc += (A[j] / i) - 1;
					else kc += A[j] / i;
				}
			}
			ans = min(ans, i + kc);
		}
		cout << "Case #" << abcd << ": " << ans << '\n';
	}
	return 0;
}
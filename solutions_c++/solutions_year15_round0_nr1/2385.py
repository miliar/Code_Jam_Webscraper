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
string str;
int A[N];
int main(){
	csl;
	if (JUDGE) {
		freopen("A-large.in", "r", stdin);
		freopen("out.txt", "w", stdout);
	}
	cin >> t;
	for (int abcd = 1; abcd <= t; abcd++) {
		cin >> n;
		cin >> str;
		rep (i, n + 1) A[i] = str[i] - '0';
		int add = 0;
		int ans = 0;
		int i = 0; 
		while (i <= n) {
			if (A[i] == 0) {
				i++;
				continue;
			}
			if (add >= i) {
				add += A[i];
				A[i] = 0;
				i++;
				continue;
			}
			else {
				ans += (i - add);
				add = i;
				continue;
			}
		}
		cout << "Case #" << abcd << ": " << ans << '\n';
	}
	return 0;
}
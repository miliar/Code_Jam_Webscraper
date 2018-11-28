#include <bits/stdc++.h>
using namespace std;

#define MOD 1000000007
#define INF 0x3f3f3f3f //numeric_limits<int>::max()
#define INFLL 0x3f3f3f3f3f3f3f3fLL //numeric_limits<ll>::max()
#define mp make_pair
#define mt make_tuple
#define getT(T, p) get<p>(T)
#define pb push_back
#define st first
#define nd second
#define contOnes __builtin_popcountl
#define powDI __builtin_powi
#define sz(v) int(v.size())
#define ver(x) if(debug) {cout << #x << " is " << x << endl; if(--debugCount < 0) exit(1);};
#define endLine if(debug) {cout << endl;}
//cuidado parametro duplicados
#define all(X) (X).begin(), (X).end()
#define logLow(X) (X <= 0 ? 0 : 31 - __builtin_clz(X))
#define logUpper(X) (X <= 1 ? 0 : 32 - __builtin_clz(X-1))
#define pow2(X) ((X)*(X))
#define unico(X) X.erase(unique((X).begin(), (X).end()), (X).end())
#define __ << " " <<

typedef long long ll;
typedef unsigned long long ull;
typedef pair<int,int> ii;
typedef pair<ll,ll> llll;
typedef pair<int,ii> iii;
typedef vector<int> vi;
typedef vector<vi> vvi;
typedef vector<ii> vii;
typedef vector<llll> vllll;
typedef vector<vii> vvii;
typedef vector<iii> viii;
typedef vector<ll> vll; 

const double EPS = 1e-8;
//const double PI = atan(1.0)*4;
const double PI = 2*acos(0.0);
inline int cmp(double x, double y = 0, double tol = EPS) {
	return (x <= y + tol) ? (x + tol < y) ? -1 : 0 : 1;
}
int debugCount = 20;
bool debug = true;

int func(string s, int k) {
	int n = sz(s);
	int flips = 0;
	for (int i = 0; i < n - k + 1; ++i) {
		if (s[i] == '-') {
			++flips;
			for (int j = i; j < i + k; ++j) {
				s[j] = '+' + '-' - s[j];
			}
		}
	}
	for (int i = n - k + 1; i < n; ++i) {
		if (s[i] == '-') {
			return -1;
		}
	}
	return flips;
}

int main(void){
	//ios_base::sync_with_stdio(false);
	int T;
	cin >> T;
	for (int t(0), k; t - T; ++t) {
		string s;
		cin >> s >> k;
		int f = func(s, k);
		if (f == -1) {
			cout << "Case #" << t+1 << ": IMPOSSIBLE" << endl;
		} else {
			cout << "Case #" << t+1 << ": " << f << endl;
		}
	}

	return 0;
}

#include <bits/stdc++.h>
using namespace std;
 
using ll = long long; using ld = long double;
using vi  = vector<int>; using vb  = vector<bool>; using vd  = vector<double>; using vl  = vector<ll>;
using vvi = vector<vi>;  using vvb = vector<vb>;   using vvd = vector<vd>;     using vvl = vector<vl>;
 
#define REP(i,n) for(ll i=0; i<(n); ++i)
#define FOR(i,b,n) for(ll i=(b); i<(n); ++i)
#define ALL(v) (v).begin(), (v).end()
#define TEN(x) ((ll)1e##x)
 
template<typename V, typename T> inline void fill(V& x, const T& val){ x = val; }
template<typename V, typename T> inline void fill(vector<V>& vec, const T& val){ for(auto& v: vec) fill(v, val); }
template<typename T> inline vector<T> operator+(vector<T> lhs, const vector<T> & rhs) { lhs.insert(lhs.end(), ALL(rhs)); return lhs; }
template<typename T> inline istream& operator>>(istream& is, vector<T>& vec){ for(T& x: vec) is >> x; return is; }
template<typename T> inline string join(const vector<T>& vec, string sep = " ") { stringstream ss; REP(i, vec.size()) ss << vec[i] << ( i+1 == vec.size() ? "" : sep ); return ss.str(); }
 
const ll MOD = 1777777777;
const double EPS = 1e-10;

int main() {
#ifdef INPUT_FROM_FILE
	std::ifstream cin("sample.in");
	std::ofstream cout("sample.out");
#endif
	cin.tie(0);
	ios_base::sync_with_stdio(false);
	cout << fixed << setprecision(30);
	ll T; cin >> T;
	REP(i, T) {
		string S; cin >> S;
		cout << "Case #" << i + 1 << ": ";
		deque<char> S2;
		for(char c : S) {
			if (S2.empty()) S2.push_back(c);
			else if (S2[0] <= c) S2.push_front(c);
			else S2.push_back(c);
		}
		REP(i, S2.size()) cout << S2[i];
		cout << endl;
	}
	
	return 0;
}
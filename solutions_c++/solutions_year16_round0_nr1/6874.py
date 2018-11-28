#include <bits/stdc++.h>
using namespace std;
#define FOR(i,k,n) for(int i = (k); i < (n); i++)
#define REP(i,n) FOR(i,0,n)
#define ALL(a) a.begin(), a.end()
#define MS(m,v) memset(m,v,sizeof(m))
#define D10 fixed<<setprecision(10)
typedef long long ll;
typedef long double ld;
typedef vector<int> vi;
typedef vector<string> vs;
typedef pair<int, int> pii;
const int MOD = 1000000007;
const int INF = MOD + 1;
const ld EPS = 1e-12;
template<class T> T &chmin(T &a, const T &b) { return a = min(a, b); }
template<class T> T &chmax(T &a, const T &b) { return a = max(a, b); }

/*--------------------template--------------------*/

set<int> st;

ll solve(ll t)
{
	for (int i = 1;; i++)
	{
		ll ans = t*i, s = t*i;
		while (s > 0)
		{
			st.insert(s % 10);
			s /= 10;
		}
		if (st.size() == 10) return ans;
	}
}

int main()
{
	int n; cin >> n;
	REP(i, n)
	{
		st.clear();
		int t; cin >> t;
		cout << "Case #" << i + 1 << ": ";
		if (t == 0) puts("INSOMNIA");
		else cout << solve(t) << endl;
	}
	return 0;
}
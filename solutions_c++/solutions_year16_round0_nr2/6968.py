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

int main()
{
	int n; cin >> n;
	REP(i, n)
	{
		cout << "Case #" << i + 1 << ": ";
		string s; cin >> s;
		int ans = 0, p = 0;
		char tmp = s[0];
		while (1)
		{
			while (p < s.size() && s[p] == tmp)
			{
				p++;
			}
			if (p == s.size())
			{
				if (s.back() == '-') ans++;
				break;
			}
			ans++;
			tmp = s[p];
		}
		cout << ans << endl;
	}
	return 0;
}
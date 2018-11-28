#include <bits/stdc++.h>
using namespace std;

#define REPU(i, a, b) for (int i = (a); i < (b); ++i)
#define REPD(i, a, b) for (int i = (a); i > (b); --i)
#define FOREACH(it, a) for (auto it = a.begin(); it != a.end(); ++it)
#define MEM(a, x) memset(a, x, sizeof(a))
#define ALL(a) a.begin(), a.end()
#define UNIQUE(a) a.erase(unique(ALL(a)), a.end())

typedef long long ll;
const int MOD = 1000000007;

template<class T, class U> inline T tmin(T a, U b) { return (a < b) ? a : b; }
template<class T, class U> inline T tmax(T a, U b) { return (a > b) ? a : b; }
template<class T, class U> inline void amax(T &a, U b) { if (b > a) a = b; }
template<class T, class U> inline void amin(T &a, U b) { if (b < a) a = b; }
template<class T> inline T tabs(T a) { return (a > 0) ? a : -a; }
template<class T> T gcd(T a, T b) { while (b != 0) { T c = a; a = b; b = c % b; } return a; }

const int N = 14;
string mr[N], ms[N], mp[N];

bool check(const string &st, int r, int s, int p) {
	REPU(i, 0, st.size()) {
		if (st[i] == 'R') r--;
		if (st[i] == 'S') s--;
		if (st[i] == 'P') p--;
	}
	return (r == 0 && s == 0 && p == 0);
}

int main(int argc, char *argv[]) {
	ios_base::sync_with_stdio(false);
	
	int nTest, n, r, s, p;
	string ans, tl, tr; bool ok;

	mr[0] = "R", ms[0] = "S", mp[0] = "P";
	REPU(i, 1, N) {
		string tl = mr[i - 1];
		string tr = ms[i - 1];
		mr[i] = min(tl + tr, tr + tl);
		tl = ms[i - 1];
		tr = mp[i - 1];
		ms[i] = min(tl + tr, tr + tl);
		tl = mp[i - 1];
		tr = mr[i - 1];
		mp[i] = min(tl + tr, tr + tl);
	}

	cin >> nTest;
	REPU(it, 1, nTest + 1) {
		cin >> n >> r >> p >> s;
		printf("Case #%d: ", it);
		ok = false;
		if (check(mr[n], r, s, p)) {
			ans = mr[n], ok = true;
		}
		if (check(ms[n], r, s, p)) {
			ans = ok ? min(ans, ms[n]) : ms[n];
			ok = true;
		}
		if (check(mp[n], r, s, p)) {
			ans = ok ? min(ans, mp[n]) : mp[n];
			ok = true;
		}
		if (!ok) printf("IMPOSSIBLE\n");
		else printf("%s\n", ans.c_str());
	}
	
	return 0;
}

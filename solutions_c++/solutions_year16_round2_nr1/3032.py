#include <bits/stdc++.h>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	present(c,x)		((c).find(x) != (c).end())
#define	cpresent(c,x)		(find(all(c),x) != (c).end())
#define	endl			'\n'

typedef long long		ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>		vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>		vpii;

const int MX = 25;

int main(int argc, char *argv[])
{
#ifdef	HTRINH_UNIT_TEST
	freopen(argv[1],"r",stdin);
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	ios :: sync_with_stdio(false);
	cin.tie(NULL);

	int T;
	cin >> T;
	FOR(testcase,1,T+1) {
		string s;
		cin >> s;
		int n = s.length();
		int cnt[26] = {0};
		FOR(i,0,n) cnt[s[i]-'A']++;
		vpii v;
		if (cnt['Z'-'A']) {
			// zero
			int have = min(cnt['Z'-'A'],min(cnt['E'-'A'],min(cnt['R'-'A'],cnt['O'-'A'])));
			cnt['Z'-'A'] -= have;
			cnt['E'-'A'] -= have;
			cnt['R'-'A'] -= have;
			cnt['O'-'A'] -= have;
			if (have) v.pb(pii(0,have));
		}
		if (cnt['F'-'A']) {
			if (cnt['U'-'A']) {
				// four
				int have = min(cnt['F'-'A'],min(cnt['O'-'A'],cnt['U'-'A']));
				have = min(have,cnt['R'-'A']);
				cnt['F'-'A'] -= have;
				cnt['O'-'A'] -= have;
				cnt['U'-'A'] -= have;
				cnt['R'-'A'] -= have;
				if (have) v.pb(pii(4,have));
			}
		}
		if (cnt['F'-'A']) {
			// five
			int have = min(cnt['F'-'A'],min(cnt['I'-'A'],cnt['V'-'A']));
			have = min(have,cnt['E'-'A']);
			cnt['F'-'A'] -= have;
			cnt['I'-'A'] -= have;
			cnt['V'-'A'] -= have;
			cnt['E'-'A'] -= have;
			if (have) v.pb(pii(5,have));
		}
		if (cnt['S'-'A']) {
			if (cnt['X'-'A']) {
				// six
				int have = min(cnt['S'-'A'],min(cnt['I'-'A'],cnt['X'-'A']));
				cnt['S'-'A'] -= have;
				cnt['I'-'A'] -= have;
				cnt['X'-'A'] -= have;
				if (have) v.pb(pii(6,have));
			}
		}
		if (cnt['S'-'A']) {
			if (cnt['E'-'A'] > 1) {
				// seven
				int have = min(cnt['S'-'A'],min(cnt['V'-'A'],cnt['N'-'A']));
				have = min(have,cnt['E'-'A']/2);
				cnt['S'-'A'] -= have;
				cnt['V'-'A'] -= have;
				cnt['N'-'A'] -= have;
				cnt['E'-'A'] -= 2*have;
				if (have) v.pb(pii(7,have));
			}
		}
		if (cnt['G'-'A']) {
			// eight
			int have = min(cnt['E'-'A'],min(cnt['I'-'A'],cnt['G'-'A']));
			have = min(have,cnt['H'-'A']);
			have = min(have,cnt['T'-'A']);
			cnt['E'-'A'] -= have;
			cnt['I'-'A'] -= have;
			cnt['G'-'A'] -= have;
			cnt['H'-'A'] -= have;
			cnt['T'-'A'] -= have;
			if (have) v.pb(pii(8,have));
		}
		if (cnt['T'-'A']) {
			// two
			int have = min(cnt['T'-'A'],min(cnt['W'-'A'],cnt['O'-'A']));
			cnt['T'-'A'] -= have;
			cnt['W'-'A'] -= have;
			cnt['O'-'A'] -= have;
			if (have) v.pb(pii(2,have));
		}
		if (cnt['T'-'A']) {
			// three
			int have = min(cnt['T'-'A'],min(cnt['H'-'A'],cnt['R'-'A']));
			have = min(have,cnt['E'-'A']/2);
			cnt['T'-'A'] -= have;
			cnt['H'-'A'] -= have;
			cnt['R'-'A'] -= have;
			cnt['E'-'A'] -= 2*have;
			if (have) v.pb(pii(3,have));
		}
		// one
		int have = min(cnt['O'-'A'],min(cnt['N'-'A'],cnt['E'-'A']));
		cnt['O'-'A'] -= have;
		cnt['N'-'A'] -= have;
		cnt['E'-'A'] -= have;
		if (have) v.pb(pii(1,have));
		// nine
		have = min(cnt['I'-'A'],cnt['E'-'A']);
		have = min(have,cnt['N'-'A']/2);
		cnt['E'-'A'] -= have;
		cnt['I'-'A'] -= have;
		cnt['N'-'A'] -= 2*have;
		if (have) v.pb(pii(9,have));

		cout << "Case #" << testcase << ": ";
		sort(all(v));
		FOR(i,0,v.size()) FOR(j,0,v[i].second) cout << v[i].first;
		cout << endl;
	}
	return 0;
}

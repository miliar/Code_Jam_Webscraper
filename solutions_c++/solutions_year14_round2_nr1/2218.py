#include <vector>
#include <numeric>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <algorithm>
#include <sstream>
#include <iostream>
#include <fstream>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <cctype>
#include <string>
#include <cstring>
#include <ctime>
#include <limits>
#include <iomanip>

using namespace std;

#define FOR(i,a,b)		for(int i=(a),_b=(b);i<(_b);++i)
#define FORD(i,a,b)		for(int i=(a),_b=(b);i>(_b);--i)
#define pb			push_back
#define mp			make_pair
#define	all(c)			(c).begin(),(c).end()
#define	tr(c,i)	for(typeof((c).begin()) i = (c).begin(); i != (c).end(); i++)
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
#ifndef ONLINE_JUDGE
	freopen(argv[1],"r",stdin);
#endif
#ifndef ONLINE_JUDGE
	ifstream cin(argv[1]);
#endif
#if 1
	ofstream cout(argv[2]);
#endif
	ios :: sync_with_stdio(false);
	cin.tie(NULL);

	int T,n;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> n;
		string a[n];
		FOR(i,0,n) cin >> a[i];
		vector<pair<char,int> > p[n];
		int mn = -1;
		bool ok = true;
		FOR(i,0,n) {
			int len = a[i].length();
			FOR(j,0,len) {
				int k = j+1;
				while (k < len && a[i][k] == a[i][j]) ++k;
				p[i].pb(pair<char,int>(a[i][j],k-j));
				j = k-1;
			}
			if (mn == -1) mn = p[i].size();
			else if (mn != p[i].size()) {
				ok = false;
				break;
			}
		}
		if (!ok) {
			cout << "Case #" << t << ": Fegla Won" << endl;
			continue;
		}
		int ans = -1;
		FOR(i,0,mn) {
			bool ok = true;
			char c = '*';
			int s = 0;
			FOR(j,0,n) {
				if (c == '*') c = p[j][i].first;
				else if (p[j][i].first != c) {
					ok = false;
					break;
				}
				s += p[j][i].second;
			}
			if (!ok) {
				ans = -1;
				break;
			}
			int ave = s/n;
			int res = 0;
			FOR(j,0,n) res += abs(p[j][i].second-ave);
			if (ans == -1) ans = res;
			else ans += res;
		}
		if (ans == -1) cout << "Case #" << t << ": Fegla Won" << endl;
		else cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

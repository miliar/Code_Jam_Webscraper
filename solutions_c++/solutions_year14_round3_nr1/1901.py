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

int solve(ll p, ll q)
{
	if (p == 0) return -1;
	if (q == 1) {
		if (p > 1) return -1;
		return 0;
	}
	if (p == 1) {
		int ans = 0;
		while (q > 1 && q%2 == 0) {
			++ans;
			q /= 2;
		}
		if (q == 1) return ans;
		return -1;
	}
	int ans = 0;
	while (q%2 == 0 && q > p) {
		q /= 2;
		++ans;
	}
	if (q == p) return ans;
	p /= q;
	int res = solve(p,q);
	if (res == -1) return -1;
	return ans;
}

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

	int T;
	ll p,q;
	string s;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> s;
		int k = 0;
		while (k < s.length() && s[k] != '/') ++k;
		p = q = 0;
		ll x = 1;
		FORD(i,k-1,-1) {
			p += (s[i]-'0')*x;
			x *= 10;
		}
		x = 1;
		FORD(i,s.length()-1,k) {
			q += x*(s[i]-'0');
			x *= 10;
		}
		int ans = solve(p,q);
		if (ans == -1) cout << "Case #" << t << ": impossible" << endl;
		else cout << "Case #" << t << ": " << ans << endl;
	}
	return 0;
}

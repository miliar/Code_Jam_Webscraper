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

typedef long long			ll;
typedef unsigned long long	ull;
typedef unsigned char	 	byte;
typedef vector<int>			vi;
typedef pair<int, int>		pii;
typedef pair<ll, ll>		pll;
typedef vector<pii>			vpii;

const int N = 25;

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
	int T,R,C;
	cin >> T;
	FOR(t,1,T+1) {
		cin >> R >> C;
		int a[R][C];
		FOR(i,0,R) FOR(j,0,C) cin >> a[i][j];
		int b[R][C];
		FOR(i,0,R) FOR(j,0,C) b[i][j] = 110;
		pair<int,pii> v[R*C];
		int k = 0;
		FOR(i,0,R) FOR(j,0,C) v[k++] = pair<int,pii>(a[i][j],pii(i,j));
		sort(v,v+R*C);
		bool ok = true;
		FORD(i,R*C-1,-1) {
			int r = v[i].second.first;
			int c = v[i].second.second;
			int cut = v[i].first;
			bool cutrow = true, cutcol = true;
			FOR(j,0,C) {
				if (a[r][j] > cut && a[r][j] <= 100) {
					cutrow = false;
					break;
				}
			}
			FOR(j,0,R) {
				if (a[j][c] > cut && a[j][c] <= 100) {
					cutcol = false;
					break;
				}
			}
			if (!cutrow && !cutcol) ok = false;
			if (cutrow) FOR(j,0,C) b[r][j] = cut;
			if (cutcol) FOR(j,0,R) b[j][c] = cut;
			if (!ok) break;
		}
		cout << "Case #" << t << ": ";
		if (!ok) cout << "NO\n";
		else cout << "YES\n";
	}
	return 0;
}

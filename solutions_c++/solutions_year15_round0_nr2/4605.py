#include <vector>
#include <list>
#include <map>
#include <set>
#include <deque>
#include <stack>
#include <bitset>
#include <algorithm>
#include <functional>
#include <numeric>
#include <utility>
#include <sstream>
#include <iostream>
#include <iomanip>
#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <ctime>
#include <string>
#include <cstring>
#include <queue>
using namespace std;

#define FOR(i,a,b) for(int i=(a);i<(b);i++)
#define REV(i,a,b) for(int i=(a);i>=(b);i--)
#define mp make_pair
#define pb push_back
#define oo 1e9
#define eps 1e-9
#define PI 3.14159265358979323846264338327950
#define MAX 2001
#define sz(v) (int)v.size()
#define all(c) (c).begin(),(c).end()
#define rall(c) (c).rbegin(),(c).rend()
#define show(x) cerr<<#x<<" = "<<x<<endl;
#define mem(s,v) memset(s,v,sizeof(s))
#define ppc(x) __builtin_popcount((x))
#define iter(it,s) for (__typeof(s.begin()) it = s.begin(); it != s.end(); it++)

typedef long long ll;
typedef vector<int> vi;
typedef vector<bool> vb;
typedef vector<double> vd;
typedef vector<string> vs;
typedef pair<int, int> pi;
typedef vector<pi> vpi;

int dx[] = { 0, 0, 1, -1 };
int dy[] = { 1, -1, 0, 0 };

int mnGlob, res;
map<pair<vi , int> , int> mapp;

void bt(vi v, int cnt) {
	sort(all(v));
	if(mapp[mp(v , cnt)])
		return;
	mapp[mp(v , cnt)] = 1;
	int mn = oo, mx = -oo;
	FOR(i , 0 , sz(v))
		mn = min(mn, v[i]), mx = max(mx, v[i]);
	res = min(res, cnt + mx);
	if (mx == 1)
		return;

	FOR(i , 0 , sz(v))
	{
		vi tmp = v;
		tmp.pb(-1);
		if (v[i] != 1) {
			FOR(j , 1 , 1 + v[i]/2)
			{
				tmp[i] = j;
				tmp[sz(tmp) - 1] = v[i] - j;
				bt(tmp, cnt + 1);
			}
		}
	}
}

int main() {
#ifndef ONLINE_JUDGE
	freopen("B-small-attempt3.in", "rt", stdin);
	freopen("o.txt", "wt", stdout);
#endif
	ios::sync_with_stdio(false);
	int t, cs = 1;
	cin >> t;
	while (t--) {
		int d;
		cin >> d;
		vi v(d);
		FOR(i , 0 , d)
			cin >> v[i];
		sort(all(v));
		res = oo;
		mapp.clear();
		bt(v, 0);
		cout << "Case #" << cs++ << ": " << res << endl;
	}
	return 0;
}

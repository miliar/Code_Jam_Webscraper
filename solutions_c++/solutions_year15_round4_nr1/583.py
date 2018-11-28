#include <string>
#include <iostream>
#include <algorithm>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <cstdio>
#include <cmath>
#include <iomanip>
#include <deque>
#include <ctime>
#include <cstring>

//#include <bits/stdc++.h>

using namespace std;

#define fr first
#define sd second
#define pb push_back
#define mp make_pair

#define endl '\n'

#define forr(i, n) for(ll (i) = 0LL; (i) < (n); (i)++)
#define mp3(a, b, c) mp(a, mp(b, c))

typedef long long ll;
typedef pair<ll, ll> pll;
typedef pair<ll, pll> plll;
typedef vector < vector < double > > vvd;
typedef vector < double > vd;
typedef vector < pair < double, double> > vdd;
typedef vector < vector < long long > > vvl;
typedef vector < long long > vl;
typedef vector < pll > vll;

int INT_MAX_VAL = (int)  0x3F3F3F3F;
int INT_MIN_VAL = (int) -0x3F3F3F3F;
ll LONG_MAX_VAL = (ll)   0x3F3F3F3F3F3F3F3F;
ll LONG_MIN_VAL = (ll)  -0x3F3F3F3F3F3F3F3F;

#define MAXN 500006
#define MOD 1000000007

void solve(int test)
{
	cout << "Case #" << test << ": ";
	int n, m; cin >> n >> m;
	vector<string> vs(n);
	forr(i, n) cin >> vs[i];

	int res = 0;

	forr(i, n) forr(j, m) {
		if(vs[i][j] == '.') continue;

		bool is_up = false;
		for(int x = i - 1; x >= 0; --x) if(vs[x][j] != '.') is_up = true;
		bool is_down = false;
		for(int x = i + 1; x < n; ++x) if(vs[x][j] != '.') is_down = true;
		
		bool is_left = false;
		for(int y = j - 1; y >= 0; --y) if(vs[i][y] != '.') is_left = true;

		bool is_right = false;
		for(int y = j + 1; y < m; ++y) if(vs[i][y] != '.') is_right = true;

		switch(vs[i][j]) {
			case '^': {
				if(is_up) continue;
				if(is_down || is_left || is_right) ++res;
				else res = -1;
				break;
					  }
			case 'v': {
				if(is_down) continue;
				if(is_up || is_left || is_right) ++res;
				else res = -1;
				break;
					  }
			case '<': {
				if(is_left) continue;
				if(is_down || is_right || is_up) ++res;
				else res = -1;
				break;
					  }
			case '>': {
				if(is_right) continue;
				if(is_up || is_down || is_left) ++res;
				else res = -1;
				break;
					  }
		}
		if(res == -1) {
			cout << "IMPOSSIBLE" << endl;
			return;
		}
	}			 
	cout << res << endl;
}

int main()
{
	cin.tie(0);
	ios::sync_with_stdio(false);

	int t; cin >> t;
	for(int i = 1; i <= t; ++i) solve(i);

	return 0;
}

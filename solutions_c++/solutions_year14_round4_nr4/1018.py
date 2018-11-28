
#define _USE_MATH_DEFINES

#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>
#include <list>
#include <iomanip>
#include <stack>
#include <map>
#include <set>
#include <queue>
#include <string>
#include <algorithm>
#include <cstring>
#include <cstdlib>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> pt;
#define ft first
#define sc second

int n, m;
string s[10];

bool read() {
	if (!(cin >> n >> m))
		return false;
	forn(i, n)
		cin >> s[i];
	return true;
}

vector<string> q[10];
int cnt[10000];

int difpref(vector <string> & v) {
	set <string> s;
	forn(i, v.size()) {
		string cur = "";
		forn(j, v[i].size()) {
			cur += v[i][j];
			s.insert(cur);
		}
	}
	return s.size()+1;
}

void rec(int cur) {
	if (cur == n) {
		int res = 0;
		forn(i, m) {
			if (q[i].empty())
				return;
			res += difpref(q[i]);
		}
		cnt[res]++;
		return;
	}
	
	forn(i, m) {
		q[i].push_back(s[cur]);
		rec(cur+1);
		q[i].pop_back();
	}
}

void solve() {
	memset(cnt, 0, sizeof(cnt));
	rec(0);
	int a, b;
	forn(i, 10000)
		if (cnt[i])
			a = i, b = cnt[i];
	cout << a << " " << b;
}

int main() {
#ifdef dans
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
#endif

#ifdef TASK_NAME
	freopen(TASK_NAME ".in", "r", stdin);
	freopen(TASK_NAME ".out", "w", stdout);
#endif

	int t;
	cin >> t;
	t = 1;
	while (read()) {
		cout << "Case #" << t << ": ";
		solve();
		cout << endl;
		++t;
	}
	
	return 0;
}

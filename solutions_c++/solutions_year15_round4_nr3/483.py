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
#include <cassert>
#include <cstring>
#include <ctime>

#define all(a) a.begin(),a.end()
#define pb push_back
#define mp make_pair
#define forn(i,n) for(int i = 0; i < int(n); ++i)
#define sz(a) int(a.size())

using namespace std;

typedef long long li;
typedef long double ld;

typedef pair<int,int> pt;
#define ft first
#define sc second

const int N = 5000;

#define ws Ws

int n;
int col[N], wcol[N], fst;
map <string, int> sid;
vector <int> ws[1000];

int getid(string s) {
	if (sid.count(s))
		return sid[s];
	int nid = sz(sid);
	return sid[s] = nid;
}

bool read() {
	if (scanf("%d\n", &n)!= 1 )
		return false;

	sid.clear();

	

	char c;

	memset(col, 0, sizeof col);

	forn(i, n) {
		string word;
		char c = 0;
		vector <int> words;
		while (true) {
			scanf("%c", &c);
			if (c == '\n') break;
			if (c == ' ') {
				words.pb(getid(word));
				word = "";
			} else
				word += c;
		}		
		words.pb(getid(word));

		ws[i] = words;
	}

	return true;
}

void solve() {

	int res = N;
	int cnt = 0;
	
	forn(mask, (1 << n)) {
		if (mask % 4 != 2)
			continue;

		int cur = 0;
		for (int i = 0; i < sz(sid); ++i)
			col[i] = 0;

		forn(i, n)
			forn(j, sz(ws[i]))
				col[ ws[i][j] ] |= (1 << ((mask >> i) & 1));

		for (int i = fst; i < sz(sid); ++i)
			cur += col[i] == 3;

		res = min(res, cur);
	}

	cout << res << endl;
}

int main() {
//#ifdef _DEBUG
	freopen("input.txt", "r", stdin);
freopen("output.txt", "w", stdout);
//#endif

	int T = 0;
	cin >> T;

	forn(t, T) {
		assert(read());
		cout << "Case #" << t + 1 << ": ";
		cerr << t + 1<< endl;
		solve();
	}
	
	return 0;
}

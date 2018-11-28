#include <map>
#include <set>
#include <math.h>
#include <deque>
#include <stack>
#include <queue>
#include <vector>
#include <iomanip>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <memory.h>
#include <stdio.h>

using namespace std;

#define pb push_back
#define all(v) v.begin(),v.end()
#define rep(i,s,m) for(int i=s;i<m;i++)
#define mem(a,b) memset(a,b,sizeof(a))
#define mp make_pair
#define PI = (2.0 * acos(0.0));
typedef stringstream ss;
typedef pair<int, int> pii;
typedef vector<pii> vpii;
typedef vector<string> vs;
typedef vector<int> vi;
typedef vector<vector<int> > vii;
typedef long long ll;
#define OO ((int)1e9)
#define sz 10010

int di[] = { -1, 0, 1, 0 };
int dj[] = { 0, 1, 0, -1 };

vector<vector<string> > seg;
bool isValid(vector<string> v) {
	for (int i = 0; i < v.size(); ++i) {
		string s = v[i];
		for (int j = 1; j < s.size(); ++j) {
			if (s[j] == s[j - 1]) {
				s = s.substr(0, j) + s.substr(j + 1), j--;
			}
		}
		v[i] = s;
	}
	for (int i = 0; i < v.size(); ++i) {
		if (v[i] != v[0])
			return false;
	}
	return true;
}

int calc(vector<string> v) {

	for (int i = 0; i < v.size(); ++i) {
		string s = v[i];
		int en = 1;
		int st = 0;
		while (en < s.size()) {
			if (s[en] != s[st]) {
				seg[i].push_back(s.substr(st, en - st));
				st = en;
			}
			en++;
		}
		seg[i].push_back(s.substr(st));
	}
	int allCnt = 0;
	for (int j = 0; j < seg[0].size(); ++j) {
		int mn = 1e9;
		for (int k = 0; k <= 100; ++k) {
			int cnt = 0;
			for (int i = 0; i < seg.size(); ++i) {
				cnt += abs(k - (int) seg[i][j].size());
			}
			mn = min(mn, cnt);
		}
		allCnt += mn;
	}
	return allCnt;

}

int main() {

#ifndef ONLINE_JUDGE
	freopen("input.in", "rt", stdin);
				freopen("output.txt", "wt", stdout);
#endif
	int ts, n;
	cin >> ts;
	for (int t = 1; t <= ts; ++t) {
		cin >> n;
		vector < string > v(n);
		seg.clear();
		seg.resize(n);

		for (int i = 0; i < n; ++i) {
			cin >> v[i];
		}
		if (!isValid(v))
			printf("Case #%d: Fegla Won\n", t);
		else {
			int cnt = calc(v);
			printf("Case #%d: %d\n", t, cnt);
		}
	}
	return 0;
}

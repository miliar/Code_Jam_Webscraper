#include <algorithm>
#include <cassert>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <iostream>
#include <map>
#include <queue>
#include <set>
#include <stack>
#include <string>
#include <vector>

using namespace std;

#define sz(x) (int)(x).size()

typedef long long ll;

string getSimple(const string& s) {
	string res;
	res += s[0];
	for(int i = 1;i < sz(s);i++) {
		if(s[i] != s[i - 1]) {
			res += s[i];
		}
	}
	return res;
}

vector < int > getLens(const string& s) {
	vector < int > res;
	res.push_back(1);
	for(int i = 1;i < sz(s);i++) {
		if(s[i] != s[i - 1]) {
			res.push_back(1);
		} else {
			res[sz(res) - 1]++;
		}
	}
	return res;	
}

void solveOne(int t) {
	int n;
	cin >> n;
	vector < string > v(n), simple(n);
	for(int i = 0;i < n;i++) {
		cin >> v[i];
		simple[i] = getSimple(v[i]);
	}
	cout << "Case #" << t << ": ";
	for(int i = 1;i < n;i++) {
		if(simple[i] != simple[i - 1]) {
			cout << "Fegla Won" << endl;
			return;
		}
	}
	vector < vector < int > > curLens(n);
	vector < int > totalLens(sz(simple[0]));
	for(int i = 0;i < n;i++) {
		curLens[i] = getLens(v[i]);
		assert(sz(curLens[i]) == sz(totalLens));
		for(int j = 0;j < sz(totalLens);j++) {
			totalLens[j] += curLens[i][j];
		}
	}
	for(int i = 0;i < sz(totalLens);i++) {
		totalLens[i] = (int)((double)totalLens[i] / n + 0.5);
	}
	int res = 0;
	for(int i = 0;i < n;i++) {
		for(int j = 0;j < sz(totalLens);j++) {
			res += abs(curLens[i][j] - totalLens[j]);
		}
	}
	cout << res << endl;
}

int main() {
	ios_base::sync_with_stdio(false);
	cin.tie(NULL);
	int tests;
	cin >> tests;
	for(int t = 1;t <= tests;t++) {
		solveOne(t);
	}
	return 0;
}

#include <sstream>
#include <vector>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <iostream>
#include <string>
#include <cassert>
#include <ctime>
#include <map>
#include <math.h>
#include <cstdio>
#include <set>
#include <deque>
#include <memory.h>
#include <queue>


using namespace std;

#pragma comment(linker, "/STACK:64000000")

typedef long long ll;

const int MAXK = 0;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;


char f(char c) {
	if (c == '-') return '+';
	return '-';
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";

		string s;
		cin >> s;
		int n = s.length();
		queue<string> q;
		map<string, int> mp;
		q.push(s);
		mp[s] = 0;
		while (!q.empty()) {
			string s = q.front();
			q.pop();
			for (int i = 1; i <= n; i++) {
				string t = "";
				for (int j = 0; j < n; j++) {
					if (j < i) t += f(s[i - 1 - j]);
					else t += s[j];
				}
				if (!mp.count(t)) {
					mp[t] = mp[s] + 1;
					q.push(t);
				}
			}
		}
		s = "";
		for (int i = 0; i < n; i++) s += '+';

		int ans = mp[s];
		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}
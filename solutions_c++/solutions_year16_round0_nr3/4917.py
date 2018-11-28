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

const int MAXK = 17;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	vector<int> lp(MAXN, -1);
	for (int i = 2; i < MAXN; i++) {
		if (lp[i] == -1) lp[i] = i;
		for (int j = i + i; j < MAXN; j += i) lp[j] = i;
	}
	vector<int> pr;
	for (int i = 2; i < MAXN; i++) if (lp[i] == i) pr.push_back(i);

	int tests;
	cin >> tests;
	assert(tests == 1);
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
	
		int n, J;
		cin >> n >> J;
		vector<string> a;
		vector<vector<int> > b;
		for (int i = (1 << (n - 1)) + 1; i < (1 << n); i += 2) {
			string s;
			int x = i;
			for (int j = 0; j < n; j++) {
				s += (char)(x % 2 + '0');
				x /= 2;
			}
			reverse(s.begin(), s.end());
			vector<int> cur;
			bool ok = 1;
			for (int p = 2; p <= 10; p++) {
				ll x = 0;
				for (int j = 0; j < n; j++) {
					x = p * x + (s[j] - '0');
				}
				bool found = 0;
				for (int i = 0; i < (int)pr.size(); i++) {
					if (x % pr[i] == 0 && x != pr[i]) {
						found = 1;
						cur.push_back(pr[i]);
						break;
					}
				}
				if (!found) ok = 0;
			}
			if (ok) {
				a.push_back(s);
				b.push_back(cur);
			}
			if (a.size() == J) break;
		}
		assert(a.size() == J);
		
		cout << endl;
		cerr << endl;
		for (int i = 0; i < J; i++) {
			cout << a[i] << " ";
			cerr << a[i] << " ";
			for (int j = 0; j < (int)b[i].size(); j++) {
				cout << b[i][j] << " \n"[j + 1 == (int)b[i].size()];
				cerr << b[i][j] << " \n"[j + 1 == (int)b[i].size()];
			}
		}
	}

	return 0;
}
#include <iostream>
#include <fstream>
#include <set>
#include <map>
#include <string>
#include <vector>
#include <bitset>
#include <algorithm>
#include <cstring>
#include <cstdlib>
#include <cmath>
#include <cassert>
#include <queue>


typedef long long ll;
typedef long double ld;

using namespace std;

void solve() {
	int n, l;
	cin >> n >> l;
	vector<string> g; 
	for (int i = 0; i < n; ++i) {
		string s;
		cin >> s;
		g.push_back(s);
	}
	string bad;
	cin >> bad;
	for (int i = 0; i < n; ++i) {
		if (bad == g[i]) {
			cout << "IMPOSSIBLE\n";
			return;
		}
	}
	if (l != 1) {
		for (int i = 0; i < l; ++i)
			cout << "0?";
		cout << " ";
		for (int i = 0; i < l - 1; ++i)
			cout << "1";
		cout << "\n";
	}
	else {
		cout << "0? 0\n";
	}
}

int main() {
	int tt;
	scanf("%d", &tt);
	for (int i = 0; i < tt; ++i) {
		printf("Case #%d: ", i + 1);
		solve();
	}
	return 0;
}



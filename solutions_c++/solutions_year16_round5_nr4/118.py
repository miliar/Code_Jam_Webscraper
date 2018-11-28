#include <functional>
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

const int MAXK = -1;
const int MAXN = 1 << MAXK;
const int INF = (int)1e9;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";
		
		int n, l;
		cin >> n >> l;
		vector<string> g(n);
		for (int i = 0; i < n; i++) cin >> g[i];
		string bb;
		cin >> bb;

		bool bad = 0;
		for (int i = 0; i < n; i++) if (bb == g[i]) bad = 1;

		if (bad) {
			cout << "IMPOSSIBLE" << endl;
			cerr << "IMPOSSIBLE" << endl;
			continue;
		}

		string a = "", b = "";
		a += "?";
		for (int i = 0; i < l - 1; i++) {
			a += "0?";
			b += "1";
		}
		if (b == "") b += "0";
		cout << a << " " << b << endl;
		cerr << a << " " << b << endl;
	}

	return 0;
}
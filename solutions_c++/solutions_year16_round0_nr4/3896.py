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


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++) {
		cout << "Case #" << test << ": ";
		cerr << "Case #" << test << ": ";

		int k, c, s;
		cin >> k >> c >> s;
		ll n = 1;
		for (int i = 0; i < c; i++) n *= k;
		if (k != s) {
			cout << "IMPOSSIBLE" << endl;
			//cerr << "IMPOSSIBLE" << endl;
			continue;
		}

		for (int i = 0; i < k; i++) {
			cout << 1 + i * (n / k) << " \n"[i + 1 == k];
			//cerr << 1 + i * (n / k) << " \n"[i + 1 == k];
		}
	}

	return 0;
}
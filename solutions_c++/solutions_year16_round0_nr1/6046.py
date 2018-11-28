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
		
		ll x;
		cin >> x;
		string ans = "INSOMNIA";
		vector<int> f(10, 0);
		int cnt = 0;
		for (int i = 1; i <= (int)1e5; i++) {
			ll y = x * i;
			stringstream ss;
			string s;
			ss << y;
			ss >> s;
			for (int i = 0; i < (int)s.length(); i++) {
				if (!f[s[i] - '0']) {
					f[s[i] - '0'] = 1;
					cnt++;
				}
			}
			if (cnt == 10) {
				ans = s;
				break;
			}
		}

		cout << ans << endl;
		cerr << ans << endl;
	}

	return 0;
}
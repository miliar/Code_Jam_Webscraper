#include <iostream>
#include <fstream>
#include <vector>
#include <string>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <algorithm>

using namespace std;

typedef long long LL;
typedef vector<LL > VLL;
typedef vector<string> VS;
typedef vector<int> VI;

const LL MAX_VAL = 100000000000000L;

int main() {
	int tcs;
	cin >> tcs;
	//process test cases
	for (int tc = 0; tc < tcs; ++tc) {
		VI vi;
		LL lres = 0;
		LL hres = 0;
		int na;
		cin >> na;

		for (int i = 0; i < na; ++i) {
			int val;
			cin >> val;
			vi.push_back(val);
		}

		int tmax = 0;
		for (int i = 1; i < na; ++i) {
			if (vi[i] < vi[i-1]) {
				int d = vi[i-1] - vi[i];
				lres += d;
				tmax = max(tmax, d);
			}
		}
		for (int i = 0; i < na - 1; ++i) {
			hres += min(vi[i], tmax);
		}

		cout << "Case #" << tc + 1 << ": " << lres << " " << hres << endl;
	}

	return 0;
}

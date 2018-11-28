#define _CRT_SECURE_NO_WARNINGS
#define _USE_MATH_DEFINES

#include <iostream>
#include <vector>
#include <string>
#include <sstream>
#include <algorithm>
#include <set>
#include <map>
#include <cmath>
#include <cstdio>
#include <cstdlib>
#include <iomanip>
#include <functional>
#include <cassert>

using namespace std;

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);

	int cases = 0;
	cin >> cases;

	for (int test = 1; test <= cases; test++) {
		int smax = 0;
		cin >> smax;

		string s;
		cin >> s;

		vector<int> c(smax + 1);
		for (int i = 0; i < s.size(); i++) {
			c[i] = s[i] - '0';
		}

		int cur = 0;
		int need = 0;

		for (int i = 0; i < c.size(); i++) {
			if (!c[i]) {
				continue;
			}

			if (cur < i) {
				need += i - cur;
				cur = i;
			}

			cur += c[i];
		}

		cout << "Case #" << test << ": " << need << endl;
	}
}
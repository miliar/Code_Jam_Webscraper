#include <iostream>
#include <cstdio>
#include <cmath>
#include <cstring>
#include <vector>
#include <limits>
#include <set>
#include <algorithm>
#include <iterator> 

using namespace std;

int main() {
	freopen("D-large.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	cin >> t;

	for (int test = 1; test <= t; test++) {
		int n;
		vector<double> v1;
		vector<double> v2;
		vector<double> v3;
		
		cin >> n;

		for (int i = 0; i < n; i++) {
			double temp;
			cin >> temp;
			v1.push_back(temp);
		}

		for (int i = 0; i < n; i++) {
			double temp;
			cin >> temp;
			v2.push_back(temp);
			v3.push_back(temp);
		}

		sort(v1.begin(), v1.end());
		sort(v2.begin(), v2.end());
		sort(v3.begin(), v3.end());

		int result1 = 0;
		int result2 = 0;

		for (int i = 0; i < n; i++) {
			double x = v1[i];

			bool found = false;
			for (vector<double>::iterator it = v2.begin(); it != v2.end(); it++) {
				if (*it > x) {
					found = true;
					v2.erase(it);
					break;
				}
			}

			if (!found) {
				result1++;
			}
		}

		while (v1.size() > 0) {
			if (v1[0] > v3[0]) {
				result2++;
				v1.erase(v1.begin());
				v3.erase(v3.begin());
			} else {
				v1.erase(v1.begin());
				v3.pop_back();
			}
		}

		printf("Case #%d: %d %d\n", test, result2, result1);
	}

	return 0;
}
/*
1
2
2 7
3 8
*/
#include <cstdio>
#include <cstring>
#include <iostream>
#include <algorithm>
using namespace std;

int main() {
	freopen("B-large (1).in", "r", stdin);
	freopen("output.txt", "w", stdout);
	
	int testCase;
	cin >> testCase;
	int caseNumber = 0;
	while (testCase--) {
		double c, f, x, t = 0;
		cin >> c >> f >> x;
		double res = 1e9;
		for (int farm = 0; ; ++farm) {
			double speed = 2.0 + farm * f;
			if (t + x / speed < res) {
				res = t + x / speed;
			} else {
				break;
			}
			t += c / speed;
		}
		printf("Case #%d: %.7f\n", ++caseNumber, res);
	}
} 

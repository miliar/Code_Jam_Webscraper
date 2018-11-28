#include <iostream>
#include <cstdio>
#include <algorithm>
#include <string>
#include <sstream>
using namespace std;

int t, smax, n, cn, result;
string s;

int main() {

	cin >> t;
	for (int C = 1; C <= t; C++) {
		printf("Case #%d: ", C);

		cin >> smax;
		cin >> s;
		result = 0;
		cn = 0;
		for (int i = 0; i <= smax; i++) {
			n = s[i] - '0';

			if (n && cn < i) {
				result += (i-cn);
				cn += (i-cn);
			}
			cn += n;
		}

		printf("%d\n", result);
	}

	return 0;
}
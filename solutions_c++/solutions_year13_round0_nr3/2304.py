#include <cstdio>
#include <iostream>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#include <sstream>
#include <string>

using namespace std;

vector<long long> f;

bool hui(long long x) {
	string str;
	while (x) {
		str += (char) '0' + (x % 10ll);
		x /= 10ll;
	}
	string rev = str;
	reverse(rev.begin(), rev.end());

	return rev == str;
}

int main() {
	for (long long i = 1ll; i <= 10000000ll; ++i)
		if (hui(i) && hui(i * i))
			f.push_back(i * i);

	int T; cin >> T;
	for (int i = 1; i <= T; ++i) {
		printf("Case #%d: ", i);
		long long a, b; cin >> a >> b;
		printf("%d\n", upper_bound(f.begin(), f.end(), b) - lower_bound(f.begin(), f.end(), a));
	}

	return 0;
}

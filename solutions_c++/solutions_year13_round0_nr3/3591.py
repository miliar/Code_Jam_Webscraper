#include <iostream>
#include <cstdio>
#include <cstring>
#include <string>
#include <vector>
#include <list>
#include <set>
#include <cmath>
#include <queue>
#include <map>
#include <algorithm>
#include <sstream>

using namespace std;

#define X first
#define Y second

vector <long long> a;

bool isPalindrome(long long x) {
	char a[20] = {0};
	sprintf(a, "%d", x);
	string s = a;
	for (int i = 0; i < s.size(); ++i)
		if (s[i] != s[s.size() - i - 1])
			return 0;
	return 1;
}

void genNumbers() {
	for (long long i = 1; i <= 10000000; ++i) {
		if (isPalindrome(i) && isPalindrome(i * i))
			a.push_back(i * i), cerr << i * i << endl;
	}
}

int lessEq(long long x) {
	int low = 0, up = a.size();
	while (up - low > 1) {
		int m = (up + low) / 2;
		if (a[m] <= x)
			low = m;
		else
			up = m;
	}
	return low;
}

int main() {
	genNumbers();
	int T;
	cerr << "Ready!\n";
	cin >> T;
	for (int TT = 1; TT <= T; ++TT) {
		long long x, y;
		cin >> x >> y;
		int up = lessEq(y), low = lessEq(x);
		if (a[low] == x)
			--low;
		printf("Case #%d: %d\n", TT, up - low);
	}
	return 0;
}
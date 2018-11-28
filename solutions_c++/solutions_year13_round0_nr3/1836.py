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

const LL MAX_VAL = 100000000000000L;

char buf[16];
VLL nums;

inline bool is_palindrome(LL num) {
	sprintf(buf, "%lld", num);
	int i1, i2;
	for (i1 = 0, i2 = strlen(buf) - 1; buf[i1] == buf[i2] && i1 <= i2; ++i1, --i2) ;
	return i1 > i2;
}

int main() {
	// pre-computation
	nums.resize(0x28);
	for (int i = 1, max = (int) sqrt(MAX_VAL); i <= max; ++i) {
		LL num = ((LL) i) * i;
		if (is_palindrome(i) && is_palindrome(num)) {
			nums.push_back(num);
			//cout << "P: " << num << endl;
		}
	}

	int tcs;
	cin >> tcs;
	//process test cases
	for (int tc = 0; tc < tcs; ++tc) {
		LL start, end;
		cin >> start >> end;
		int count = upper_bound(nums.begin(), nums.end(), end) - lower_bound(nums.begin(), nums.end(), start);
		cout << "Case #" << tc + 1 << ": " << count << endl;
	}

	return 0;
}


#include <iostream>
#include <sstream>
#include <vector>
#include <algorithm>
#include <iterator>

using namespace std;

typedef unsigned long long uint64;

int n;
uint64 len, p;
bool good(uint64 x) {
	uint64 place = 0;
	uint64 right = len - x - 1;
	for (int i = 0; i < n; ++i) {
		if (right)
			right = (right - 1) / 2;
		else
			place += ((uint64) 1) << (n - i - 1);
	}
	return place < p;
}

bool worse(uint64 x) {
	uint64 place = 0;
	uint64 left = x;
	for (int i = 0; i < n; ++i) {
		if (left) {
			left = (left - 1) / 2;
			place += ((uint64) 1) << (n - i - 1);		
		}
	}
	return place < p;
}


int main()
{
	ios_base::sync_with_stdio(0);
	int test_cases;
	cin >> test_cases;
	for (int test_num = 1; test_num <= test_cases; ++test_num) {
		cout << "Case #" << test_num << ": ";
		cin >> n >> p;

		len = (((uint64) 1) << n);
		uint64 l = 0, r = len, x;

		while (l < r - 1) {
			x = (l + r) / 2;
			if (worse(x))
				l = x;
			else
				r = x;
		}
		cout << l << " ";
		l = 0;
		r = len;
		while (l < r - 1) {
			x = (l + r) / 2;
			if (good(x))
				l = x;
			else
				r = x;
		}
		cout << l << endl;

	}
	return 0;
}
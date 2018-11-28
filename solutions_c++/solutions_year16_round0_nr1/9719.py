#include <iostream>
#include <cstdio>
#include <cstdlib>
#include <vector>
#include <set>
#include <map>
#include <string>
#include <cstring>
#include <queue>
#include <cmath>
#include <algorithm>
#include <climits>

using namespace std;

int n, cnt;
bool digit[10];

bool add_digit(long long d) {
	while (d > 0) {
		if (!digit[d%10]) {
			digit[d%10] = true;
			cnt++;
		}
		d /= 10;
	}
	if (cnt == 10)
		return true;
	else
		return false;
}

void run_case(int tc) {
    cin >> n;
	if (n == 0) {
		cout << "Case #" << tc << ": INSOMNIA" << endl;
		return;
	}
	memset(digit, false, sizeof(digit));
	cnt = 0;
	long long nn = n;
	for (long long i = 1; i < LLONG_MAX/n; i++) {
		if (add_digit(nn)) {
			cout << "Case #" << tc << ": " << nn << endl;
			return;
		} else {
			nn += n;
		}
	}
	cout << "Case #" << tc << ": INSOMNIA" << endl;
}

int main() {
	int num = 0;
	cin >> num;
	for (int i = 1; i <= num; ++i) {
		run_case(i);
	}
	return 0;
}
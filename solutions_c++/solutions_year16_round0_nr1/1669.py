#include <iostream>
#include <vector>
#include <algorithm>
#include <cmath>
#include <iomanip>
#include <string>
#include <tuple>
#include <queue>
#include <utility>
#include <stack>
#include <set>
#include <map>
#include <deque>
#include <limits>
#include <new>
#include <functional>
#include <unordered_map>
#include <unordered_set>

using namespace std;

bool dissect(int& mask, int input) {
	while (input != 0) {
		int temp = input % 10;
		input /= 10;
		mask |= (1 << temp);
	}
	if (mask == 1023) return true;
	else return false;
}

int main(void) {
	cin.tie(nullptr);
	cin.sync_with_stdio(false);

	int t;
	cin >> t;
	for (int i = 1; i <= t; i++) {
		int n;
		cin >> n;
		if (n == 0) {
			cout << "Case #" << i << ": INSOMNIA\n";
			continue;
		}
		int N = n, mask = 0;
		while (!dissect(mask, N)) {
			N += n;
		}
		cout << "Case #" << i << ": " << N << '\n';
	}

	return 0;
}
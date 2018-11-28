#include <sstream>
#include <string>
#include <vector>
#include <map>
#include <algorithm>
#include <iostream>
#include <utility>
#include <set>
#include <cctype>
#include <queue>
#include <stack>
#include <cstdio>
#include <cstdlib>
#include <cmath>
#include <cstring>

using namespace std;

int main() {
	int T;
	cin >> T;
	for (int t = 1; t <= T; t++) {
		long long n;
		cin >> n;

		if (n == 0) {
			cout << "Case #" << t << ": " << "INSOMNIA" << endl;
			continue;
		}

		long long ret = -1;
		bool used[10] = {false};
		for (int i = 1; ret < 0 && i < 100000; i++) {
			long long num = n * i;
			while (num > 0) {
				used[num % 10] = true;
				num /= 10;
			}
			for (int j = 0; j < 10; j++) {
				if (!used[j]) {
					break;
				} else if (j == 10 - 1) {
					ret = n * i;
				}
			}
		}
		cout << "Case #" << t << ": " << ret << endl;
	}
}


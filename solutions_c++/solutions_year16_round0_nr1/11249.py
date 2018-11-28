#include <string>
#include <vector>
#include <iostream>
#include <cstdlib>
#include <cstdio>
#include <sstream>
#include <algorithm>
#include <map>
#include <set>
#include "string.h"

using namespace std;

typedef long long LL;

int main() {
	int T; cin >> T;
	for (int i = 0; i < T; i++) {
		int N; cin >> N;

		if (N == 0) {
			cout << "Case #" << i+1 << ": " << "INSOMNIA" << endl;
		} else {
			int used[11] = {0};
			int count = 1;
			int M = N * count;

			while (true) {
				stringstream ss;
				ss << M;
				string s = ss.str();
				for (int j = 0; j < s.length(); j++) {
					used[s[j] - '0'] = 1;
				}

				int sum = 0;
				for (int j = 0; j < 11; j++) {
					if (used[j]) sum++;
				}
//				cout << "  " << sum << endl;

				if (sum == 10) {
					cout << "Case #" << i+1 << ": " << M << endl;
					break;
				}

//				cout << "    " << M << " " << N << " " << count << endl;

				count++;
				M = N * count;
			}
		}
	}

	return 0;
}
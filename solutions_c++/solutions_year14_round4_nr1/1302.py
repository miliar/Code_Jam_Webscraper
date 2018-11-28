#include <iostream>
#include <math.h>
#include <stdlib.h>
#include <iomanip>
#include <string>
#include <string.h>
#include <sstream>
#include <algorithm>
#include <time.h>
using namespace std;

int main() {
	int T;
	int N;
	int X;
	int num[10010];
	bool marked[10010];

	cin >> T;

	for (int j = 1; j <= T; j++) {
		cin >> N >> X;

		for (int i = 0; i < N; ++i) {
			cin >> num[i];
			marked[i] = false;
		}

		sort(num, num+N);

		int count = 0;
		int cur = 0;

		for (int i = N-1; i >= 0; --i) {
			if (marked[i])
				continue;

			cur = num[i];

			for (int k = i-1; k>=0; --k) {
				if (marked[k])
					continue;
				if (num[k] + cur <= X) {
					marked[k] = true;
					//cur += num[k];
					break;
				}
			}

			++count;
		}

		cout << "Case #" << j << ": " << count << endl;
	}

	return 0;
}

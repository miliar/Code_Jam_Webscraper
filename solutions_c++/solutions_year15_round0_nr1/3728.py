#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <cstdlib>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <string>

using namespace std;

int main() {
	int T;
	cin >> T;

	for (int i = 0; i < T; i++) {
		int max;
		cin >> max;

		string shyness;
		cin >> shyness;


		if (max == 0) {

			cout << "Case #" << i+1 << ": " << 0 << endl;
			continue;
		}

		vector<int> shynessint(max + 1, 0);
		shynessint[0] = shyness[0] - '0';
		for (int j = 1; j <= max; j++) {
			shynessint[j] = shyness[j] - '0';
		}

		int count = 0;
		for (int j = 1; j <= max; j++) {
			if (shynessint[j - 1] < j) {
				count += j - shynessint[j - 1];
				shynessint[j] = j + shynessint[j];
			}
			else {
				shynessint[j] = shynessint[j - 1] + shynessint[j];
			}
		}

		//string str(shynessint.begin(), shynessint.end());
		//cout << "Accu Shyness " << str << endl;

		cout << "Case #" << i+1 << ": " << count << endl;
	}

	return 0;
}
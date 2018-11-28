#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>
#include <utility>
#include <cmath>
#include <cstdio>

using namespace std;
typedef long long LL;

bool isPol(LL n) {
	LL st = 1;
	while(st <= n) {
		st *= 10;
	}
	LL dst = 1;
	bool flag = true;
	while(st != 1) {
		if ( (n / (st/10) ) % 10 == ( n / (dst) ) % 10) {
			dst *= 10;
			st /= 10;
		} else {
			return false;
		}
	}
	return flag;
}

int main() {						   
	//freopen("input.txt", "r", stdin);
	//freopen("output.txt", "w", stdout);

	vector<LL> nums;
	for (LL i = 1; i < 100000000; ++i) {
		if (isPol(i) && isPol(i*i)) {
			nums.push_back(i*i);
		}									 
	}

	int T = 0;
	cin >> T;
	for (int t = 1; t <= T; ++t) {
		LL a, b;
		cin >> a >> b;
		int cc = 0;
		for (int i = 0; i < nums.size(); ++i) {
			if (nums[i] >= a && nums[i] <= b) {
				++cc;
			}
		}
		cout << "Case #" << t << ": " << cc << endl;
	}
	/*for (LL i = 1; i < 1000000000; ++i) {
		if (isPol(i) && isPol(i*i)) {
			cout << i << " " << i*i << endl;
		}									 
	} */

	return 0;
}

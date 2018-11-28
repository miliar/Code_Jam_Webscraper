#include <cstring>
#include <iostream>
#include <set>
#include <algorithm>
#include <queue>
#include <climits>
using namespace std;

int main() {
	int t;
	cin >> t;

	for(int z = 1; z <= t; z++) {
		int d;
		cin >> d;
		vector<int> v;

		int tmp, mx = INT_MIN;
		for(int i = 0; i < d; i++) {
			cin >> tmp;
			v.push_back(tmp);
			mx = max(mx, tmp);
		}

		int ret = mx;

		for(int i = 1; i <= mx; i++) {
			int acc = i;

			for(int j = 0; j < v.size(); j++) {
				if(v[j] > i) {
					if(v[j]%i == 0) acc += (v[j]/i)-1;
					else acc += (v[j]/i);
				}
			}

			ret = min(ret, acc);
		}

		cout << "Case #" << z << ": " << ret << endl;
	}
}


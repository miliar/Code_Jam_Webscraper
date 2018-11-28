#include <iostream>
#include <vector>
#include <stdio.h>
#include <algorithm>
#include <cmath>
using namespace std;

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.txt", "w", stdout);
	int t = 0;
	cin >> t;
	for(int i=1; i<=t; i++) {
		int d;
		cin >> d;
		vector<int> v(d);
		for (int x = 0; x < d; x++) {
			cin >> v[x];
		}

		sort(v.rbegin(),v.rend());

		int m = v[0];
		int ans = v[0];

		for (int r = 1; r < m+1; ++r) {
			int mv = 0;
			for (int j = 0; j < v.size(); ++j) {
				if(v[j]<=r)
					break;
				 mv += ceil(float(v[j]) / float(r)) - 1;
			}
			if( mv + r < ans)
				ans = mv+r;
		}

		cout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}

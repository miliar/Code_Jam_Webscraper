#include <iostream>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;


int main() {
	freopen("C:/Users/dd/Downloads/A-large.in", "r", stdin);
	freopen("C:/Users/dd/Downloads/A-large.out", "w", stdout);

	int cas;
	cin >> cas;
	for (int te = 1; te <= cas; te ++) {
		vector<int> v;
		int n; 
		cin >> n;
		int first = 0, second = 0, ma = 0;
		for (int i = 0; i < n; i ++) {
			int x; cin >> x;
			v.push_back(x);
			if (i) {
				first += max(0, v[i - 1] - v[i]);
				ma = max(ma, v[i - 1] - v[i]);
			} 
		} 
		for (int i = 0; i < n - 1; i ++) {
			second += min(ma, v[i]);
		}

		//cout << ma << endl;
		printf("Case #%d: %d %d\n", te, first, second);
	}
}

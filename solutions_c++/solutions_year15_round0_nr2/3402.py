#include <cstdio>
#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int main() {
	int T;
	cin >> T;
	for(int t = 0; t < T; t ++) { 
		vector <int> a;
		int n, temp;
		cin >> n;
		for(int i = 0; i < n; i ++) {
			cin >> temp;
			a.push_back(temp);
		}
		int ans = 10000000;
		for(int lim = 1; lim <= 1000; lim ++) {
			int val = lim;
			for(int i = 0; i < n; i ++) {
				if(a[i] > lim)
					val += a[i] / lim;
				if((a[i] > lim) && (a[i] % lim == 0))
					val --;
			}
			ans = min(ans, val);
			//printf("ans: %d\n", ans);
		}
		printf("Case #%d: %d\n", t + 1, ans);
	}
	return 0;
}

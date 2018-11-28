#include <iostream>
#include <stdio.h>
#include <map>
#include <algorithm>
#include <vector>

using namespace std;


int main() {
	freopen("C:/Users/dd/Downloads/B-large.in", "r", stdin);
	freopen("C:/Users/dd/Downloads/B-large.out", "w", stdout);

	int cas;
	cin >> cas;
	for (int te = 1; te <= cas; te ++) {
		int n;
		vector<int> v;
		cin >> n;
		for (int i = 0; i < n; i ++) {
			int x;
			cin >> x;
			v.push_back(x);
		}		
		int ans = 1000000000;
		for (int h = 1; h < 1005; h ++) {
			int tmp = 0;
			for (int i = 0; i < n; ++ i) {
				tmp += (v[i] + h - 1) / h - 1; 
			}
			tmp += h;
			ans = min(ans, tmp);
		}
		printf("Case #%d: %d\n", te, ans);
	}
}

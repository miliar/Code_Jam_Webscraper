#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>
#include <vector>
#include <cstdio>
#include <fstream>
using namespace std;


int main() {
	freopen("B-large (1).in", "r", stdin);
	freopen("2output.txt","w",stdout);
	int test,t;
	cin >> t;
	for (test=1;test<=t;test++) {
		int n;
		cin >> n;
		int a[2502] = {0};
		for (int i=1;i<=2*n-1;i++) {
			for (int j = 1; j <= n; j++) {
				int k;
				cin >> k;
				a[k]++; 
			}
		}
		vector<int> ans;
		for (int i = 1; i < 2502; i++) {
			if (a[i] % 2 != 0) {
				ans.push_back(i);
			}
		}
		sort(ans.begin(),ans.end());
		cout << "Case #" << test << ": ";
		for (int i =0 ; i < n; i++){
			cout << ans[i] << " ";
		}
		cout << endl;
	}
	return 0;
}
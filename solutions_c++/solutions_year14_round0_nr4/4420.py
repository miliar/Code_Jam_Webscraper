#include <iostream>
#include <vector>
#include <cstdlib>
#include <queue>
#include <unordered_set>
#include <algorithm>
#include <map>
#include <sstream>
#include <list>
#include <algorithm>
#include <string>
#include <cstring>
#include <cstdlib>
#include <climits>
#include <cmath>
#include <set>
#include <utility>


using namespace std;

int main() {
	int ncases;
	cin >> ncases;
	for (int caseid = 1; caseid <= ncases; caseid++) {
		int n;
		cin >> n;
		vector<double> a(n), b(n);
		for (int i = 0; i < n; i++) {
			cin >> a[i];
		}
		for (int i = 0; i < n; i++) {
			cin >> b[i];
		}
		sort(a.begin(), a.end());
		sort(b.begin(), b.end());

		/*
		int ans1 = n;
		int cur1 = 0;
		
		for (int i = 0; i < n && cur1 < n; i++) {
			if (b[cur1] > a[i]) {
				ans1--;
				cur1--;
			}
		}
		*/
		vector<int> tmp(b.size()+1, 0);
		vector<vector<int>> f(a.size()+1, tmp);

		for (int i = 0; i <= n; i++) {
			for (int j = 0; j <= n; j++) {
				if (i > 0)
					f[i][j] = max(f[i][j], f[i-1][j]);
				if (j > 0)
					f[i][j] = max(f[i][j], f[i][j-1]);
				if (i > 0 && j > 0 && a[i-1]>b[j-1]) 
					f[i][j] = max(f[i][j], f[i-1][j-1]+1);
			}
		}
		int ans1 = f[n][n];
		
		int ans2 = n;
		int cur2 = 0;
		for (int i = 0; i < n; i++) {
			while (cur2 < n) {
				if (b[cur2] > a[i]) {
					ans2--;
					cur2++;
					break;
				} else {
					cur2++;
				}
			}
		}
		cout << "Case " << "#" << caseid << ": " << ans1 << " " << ans2 << endl;
	}
	return 0;
}

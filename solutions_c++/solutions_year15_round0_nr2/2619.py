#include <iostream>
#include <sstream>
#include <algorithm>
#include <unordered_map>
#include <vector>
#include <cstdio>
#include <cmath>
#include <map>
#include <set>
#include <unordered_set>


using namespace std;


int t;
vector<int> v;


int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int k = 0; k < t; k++) {
		int d;
		scanf("%d", &d);
		v.resize(d);
		for (int i = 0; i < d; i++) {
			scanf("%d", &v[i]);
		}
		sort(v.begin(), v.end());
		int ans = 0;
		while (v.back() > 2) {
			int tt = 0;
			int j = 0;
			int g = v.back();
			for (int i = (int)v.size() - 1; i >= 0; i--) {
				if (v[i] == g) {
					tt++;
					j = i - 1;
				}
			}
			int h = max((j >= 0 ? v[j]: 0), (g + 1) / 2);
			if (g - h > tt) {
				ans+= tt;
				while (!v.empty() && v.back() == g) {
					v.pop_back();
				}
				for (int i = 0; i < tt; i++) {
					v.push_back(g / 2);
					v.push_back((g + 1) / 2);
				}
				sort(v.begin(), v.end());
			} else {
				break;
			}
		}
		ans += v.back();
 		printf("Case #%d: %d\n", k + 1, ans);
	}
    return 0;
}

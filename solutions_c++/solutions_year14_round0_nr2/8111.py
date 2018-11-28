#include <iostream>
#include <vector>
#include <algorithm>
#include <map>
#include <cstdio>
#include <iomanip>

using namespace std;


int T;
double c, f, x, cur, ans, now;
int main () {
	freopen("input.txt", "r", stdin);freopen("output.txt", "w", stdout);
	cin >> T;
	cout << fixed << setprecision(10);
	for (int t = 1; t <= T; t++) {
		cin >> c >> f >> x;
	        cur = 2.;
	        ans = 1e9;
		now = 0;
		for (int i = 1; i <= x + 1; i++) {
			ans = min(ans, now + x / cur);
			now += c / cur;
			cur += f;	 					       		
	       	}
	       	cout << "Case #" << t << ": " << ans << "\n";
	}
}
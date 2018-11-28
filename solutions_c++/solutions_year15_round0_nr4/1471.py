#include <iostream>
#include <algorithm>
#include <cmath>
#include <string>

using namespace std;

int main() {
	int t;
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	cin >> t;
	for (int test = 0; test < t; test++) {
		cout << "Case #" << test + 1 << ": ";
		int x, y, n;
		cin >> n >> x >> y;
		if (x > y)
			swap(x, y);
		string ans = "GABRIEL";
		string r = "RICHARD";

		if ( (x * y) % n ) 
			ans = r;

		if (x < (n+1)/ 2)
			ans = r;

		if (x == 2 && n > 3 )
			ans = r;

		cout << ans << endl;
	}
}
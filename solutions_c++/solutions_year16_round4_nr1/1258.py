#include <iostream>
#include <string>
#include <vector>
#include <algorithm>
#include <numeric>

using namespace std;

string solve(int p, int r, int s) {
	if (p + r + s == 2) {
		string ans = "";
		if (p) {
			ans += 'P';
		}
		if (r) {
			ans += 'R';
		}
		if (s) {
			ans += 'S';
		}
		return ans;
	}
	int p1 = p / 2, p2 = p / 2, r1 = r / 2, r2 = r / 2, s1 = s / 2, s2 = s / 2;
	if (p % 2 == 0) {
		++r1;
		++s2;
	}
	if (r % 2 == 0) {
		++p1;
		++s2;
	}
	if (s % 2 == 0) {
		++r1;
		++p2;
	}
	string ans1 = solve(p1, r1, s1), ans2 = solve(p2, r2, s2);
	if (ans1 > ans2) {
		swap(ans1, ans2);
	}
	return ans1 + ans2;
}

int main() {
	int t;
	cin>>t;
	for (int tt = 1; tt <= t; ++tt) {
		int n, r, p, s;
		string ans = "IMPOSSIBLE";
		cin>>n>>r>>p>>s;
		if ((max(r, max(p, s)) - min(r, min(p, s))) == 1) {
			ans = solve(p, r, s);
		}
		cout<<"Case #"<<tt<<": "<<ans<<endl;
	}
	return 0;
}

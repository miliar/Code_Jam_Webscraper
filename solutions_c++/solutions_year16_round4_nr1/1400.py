#include <algorithm>
#include <bitset>
#include <cstdio>
#include <cstring>
#include <deque>
#include <functional>
#include <iostream>
#include <set>
#include <stack>
#include <map>
#include <queue>
#include <vector>
using namespace std;

string ss[15][2111][2111];
int ok[15][2111][2111];
int T;

string recurse(int n, int p, int r) {	
	if (ok[n][p][r] > -1) {
		return ss[n][p][r];
	}
	if (n == 0) {
		ok[n][p][r] = true;
		if (p == 1) {
			ss[n][p][r] = "P";
		}
		else if (r == 1) {
			ss[n][p][r] = "R";
		}
		else {
			ss[n][p][r] = "S";
		}
		return ss[n][p][r];
	}
	
	int s = (1 << n) - p - r;
	if (abs(p - s) > 1 || abs(r - s) > 1) {
		ok[n][p][r] = 0;
		return ss[n][p][r] = "";
	}
	
	int lp = p/2, rp = p - p/2, lr = r/2, rr = r - r/2;
	string p1 = recurse(n - 1, lp, lr);
	string p2 = recurse(n - 1, rp, rr);
	string p3 = recurse(n - 1, lp, rr);
	string p4 = recurse(n - 1, rp, lr);
	
	string s1 = (p1 > p2) ? (p2 + p1) : (p1 + p2);
	string s2 = (p3 > p4) ? (p4 + p3) : (p3 + p4);	
	ok[n][p][r] = 1;
	if (s1.size() == 1 << n) {
		ss[n][p][r] = s1;
	}
	if (s2.size() == 1 << n && (s1.size() < 1 << n || s2 < s1)) {
		ss[n][p][r] = s2;
	}
	return ss[n][p][r];
}

int main() {
	scanf("%d", &T);	
	memset(ok, -1, sizeof ok);
	for (int it = 1; it <= T; it++) {
		printf("Case #%d: ", it);
		int n, r, p, s;
		scanf("%d %d %d %d", &n, &r, &p, &s);		
		if (abs(r - p) > 1 || abs(r - s) > 1 || abs(p - s) > 1) {
			printf("IMPOSSIBLE\n");
			continue;
		}
		cout << recurse(n, p, r) << endl;
	}
	return 0;
}

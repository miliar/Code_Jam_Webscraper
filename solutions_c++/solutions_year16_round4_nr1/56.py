#include <cmath>
#include <cstdio>
#include <cctype>
#include <cstdlib>
#include <climits>
#include <cstring>
#include <vector>
#include <string>
#include <iostream>
#include <cassert>
#include <algorithm>

using namespace std;

const char A[] = "RPS";

int n, r, p, s;
string ret;

void go(int d, string vec)
{
	if (d == n) {
		int cr = 0, cp = 0, cs = 0;
		for(auto e: vec) {
			if (e == 'R') ++ cr;
			if (e == 'P') ++ cp;
			if (e == 'S') ++ cs;
		}
		if (cr == r && cp == p && cs == s) {
			for(int d = 2; d <= vec.size(); d *= 2) {
				for(int i = 0; i < vec.size(); i += d) {
					if (vec.substr(i, d / 2) > vec.substr(i + d / 2, d / 2)) {
						for(int j = 0; j < d / 2; ++ j) {
							swap(vec[i + j], vec[i + j + d / 2]);
						}
					}
				}
			}
			if (ret == "IMPOSSIBLE" || ret > vec) {
				ret = vec;
			}
		}
		return;
	}
	string nxt;
	for(auto e: vec) {
		if (e == 'R') nxt += "RS";
		if (e == 'S') nxt += "SP";
		if (e == 'P') nxt += "PR";
	}
	go(d + 1, nxt);
}

void solve()
{
	cin >> n >> r >> p >> s;
	ret = "IMPOSSIBLE";
	for(int i = 0; i < 3; ++ i) {
		string tmp;
		tmp += A[i];
		go(0, tmp);
	}
	cout << ret << endl;
}

int main()
{
	//freopen("A-small-attempt0.in", "r", stdin); freopen("A-small-attempt0.out", "w", stdout);
	//freopen("A-small-attempt1.in", "r", stdin); freopen("A-small-attempt1.out", "w", stdout);
	//freopen("A-small-attempt2.in", "r", stdin); freopen("A-small-attempt2.out", "w", stdout);
	freopen("A-large.in", "r", stdin); freopen("A-large.out", "w", stdout);
	int test_case;
	cin >> test_case;
	for(int i = 0; i < test_case; ++ i) {
		printf("Case #%d: ", i + 1);
		cerr << "Start: " << i << endl;
		solve();
	}
	return 0;
}

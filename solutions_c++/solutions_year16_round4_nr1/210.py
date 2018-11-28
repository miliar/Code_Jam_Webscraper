#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <iostream>
#include <string>

using namespace std;

int n;
int r, s, p;
int cr, cs, cp;

string dfs(int dep, char cur) {
	if (dep == 0) {
		if (cur == 'R') {
			cr++;
			return "R";
		} else if (cur == 'S') {
			cs++;
			return "S";
		} else {
			cp++;
			return "P";
		}
	}

	string a, b;

	if (cur == 'R') {
		a = dfs(dep - 1, 'R');
		b = dfs(dep - 1, 'S');
	} else if (cur == 'S') {
		a = dfs(dep - 1, 'P');
		b = dfs(dep - 1, 'S');
	} else if (cur == 'P') {
		a = dfs(dep - 1, 'P');
		b = dfs(dep - 1, 'R');
	}
	if (b < a) {
		swap(a, b);
	}
	return a + b;
}

int main() {
	int test;
	scanf("%d", &test);
	while (test--) {
		string answer = "";
		scanf("%d %d %d %d", &n, &r, &p, &s);

		cr = cs = cp = 0;
		string rr = dfs(n, 'R');
		if (cr == r && cp == p && cs == s) {
			if (answer == "" || rr < answer) {
				answer = rr;
			}
		}

		cr = cs = cp = 0;
		string ss = dfs(n, 'S');
		if (cr == r && cp == p && cs == s) {
			if (answer == "" || ss < answer) {
				answer = ss;
			}
		}

		cr = cs = cp = 0;
		string pp = dfs(n, 'P');
		if (cr == r && cp == p && cs == s) {
			if (answer == "" || pp < answer) {
				answer = pp;
			}
		}

		static int testCount = 0;
		printf("Case #%d: ", ++testCount);
		if (answer == "") {
			cout << "IMPOSSIBLE" << endl;
		} else {
			cout << answer << endl;
		}
	}
	return 0;
}

// Problem A. Rather Perplexing Showdown
#include <cstdio>
#include <cstdlib>
#include <cstring>
#include <cmath>
#include <string>
#include <algorithm>
#include <vector>
#include <queue>
#include <map>
#include <set>

using namespace std;

string calc(int n, char c)
{
	if (n == 1) {
		if (c == 'P') return "PR";
		else if (c == 'R') return "RS";
		else return "PS";
	}

	if (c == 'P') {
		string s1 = calc(n - 1, 'P');
		string s2 = calc(n - 1, 'R');
		return (s1 < s2) ? s1 + s2 : s2 + s1;
	} else if (c == 'R') {
		string s1 = calc(n - 1, 'R');
		string s2 = calc(n - 1, 'S');
		return (s1 < s2) ? s1 + s2 : s2 + s1;
	} else if (c == 'S') {
		string s1 = calc(n - 1, 'S');
		string s2 = calc(n - 1, 'P');
		return (s1 < s2) ? s1 + s2 : s2 + s1;
	}
}

int main(int argc, char *argv[])
{
	int T;
	scanf("%d", &T);
	for (int ti = 1; ti <= T; ti++) {
		int N, R, P, S;
		scanf("%d %d %d %d", &N, &R, &P, &S);

		string a[3];
		a[0] = calc(N, 'P');
		a[1] = calc(N, 'R');
		a[2] = calc(N, 'S');

		string ans = "";
		for (int i = 0; i < 3; i++) {
			int r = 0, p = 0, s = 0;
			for (int k = 0; k < a[i].size(); k++)
				if (a[i][k] == 'P') p++;
				else if (a[i][k] == 'R') r++;
				else s++;
			if (r == R && p == P && s == S) {
				ans = a[i];
				break;
			}
		}

		if (ans.size() > 0)
			printf("Case #%d: %s\n", ti, ans.c_str());
		else
			printf("Case #%d: IMPOSSIBLE\n", ti);
	}

	return 0;
}

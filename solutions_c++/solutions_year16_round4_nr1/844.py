#include <stdio.h>
#include <algorithm>
#include <string>
#include <vector>

using namespace std;

string ans;

void sorting(int n)
{
	vector<string> v[15];

	for (int i = 0; i < (1 << n); i++) v[0].push_back(ans.substr(i,1));
	for (int i = 0; i < n; i++) {
		for (int j = 0; j < v[i].size(); j += 2) {
			if (v[i][j] < v[i][j + 1]) v[i + 1].push_back(v[i][j] + v[i][j + 1]);
			else v[i + 1].push_back(v[i][j + 1] + v[i][j]);
		}
	}
	ans = v[n][0];
}

bool func(int n, int p, int r, int s)
{
	if (p < 0 || r < 0 || s < 0) return false;
	if (n == 0) {
		if (p) ans = "P";
		else if (r) ans = "R";
		else if (s) ans = "S";
		return true;
	}
	int p1 = (r-s+p)/2, p2=(-r+s+p)/2;
	if (func(n - 1, p1, p2, r - p1))
	{
		string tmp;
		for (int i = 0; i < ans.size(); i++) {
			if (ans[i] == 'P') tmp += "PR";
			else if (ans[i] == 'R') tmp += "PS";
			else tmp += "RS";
		}
		ans = tmp;
		return true;
	}

	return false;
}

void process()
{
	int n, p, r, s;
	scanf("%d %d %d %d", &n, &r, &p, &s);

	if (func(n, p, r, s)) {
		sorting(n);
		printf("%s\n", ans.c_str());
	}
	else printf("IMPOSSIBLE\n");
}

int main()
{
	freopen("A-large.in", "rt", stdin);
	freopen("output.txt", "wt", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ",i);
		process();
	}
	return 0;
}
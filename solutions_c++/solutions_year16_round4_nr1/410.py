#include <cstdio>
#include <vector>
#include <algorithm>
using namespace std;


string calculate(int n, int r, int p, int s, int S, vector<vector<string>>& memo)
{
	if(n == 0) {
		if(r > 0) return "R";
		if(p > 0) return "P";
		if(s > 0) return "S";
		return "";
	}

	if(r % 2 == 0 && p % 2 == 0 && s % 2 == 0)
		return "XXX";

	int idx = r * (S + 1) + s;

	if(memo[n - 1][idx] != "Z")
		return memo[n - 1][idx];

	string ans = "XXX";

	if(r % 2 == 0) {
		string x = calculate(n - 1, r / 2, p / 2, (s + 1) / 2, S, memo);
		string y = calculate(n - 1, r / 2, (p + 1) / 2, s / 2, S, memo);
		if(x.size() + y.size() == (1 << n))
			ans = min(x + y, y + x);
	} else if(p % 2 == 0) {
		string x = calculate(n - 1, r / 2, p / 2, (s + 1) / 2, S, memo);
		string y = calculate(n - 1, (r + 1) / 2, p / 2, s / 2, S, memo);
		if(x.size() + y.size() == (1 << n))
			ans = min(x + y, y + x);
	} else if(s % 2 == 0) {
		string x = calculate(n - 1, (r + 1) / 2, p / 2, s / 2, S, memo);
		string y = calculate(n - 1, r / 2, (p + 1) / 2, s / 2, S, memo);
		if(x.size() + y.size() == (1 << n))
			ans = min(x + y, y + x);
	}

	return memo[n - 1][idx] = ans;
}


int main()
{
	int testcase;

	scanf("%d", &testcase);

	for(int case_num = 1; case_num <= testcase; ++case_num) {

		int n, r, p, s;
		string ans = "XXX";
		vector<vector<string>> memo;

		scanf("%d%d%d%d", &n, &r, &p, &s);
		memo.resize(n);
		for(int i = 0; i < n; ++i)
			memo[i].resize((r + 1) * (s + 1), "Z");

		ans = min(ans, calculate(n, r, p, s, s, memo));

		if(ans == "XXX")
			ans = "IMPOSSIBLE";

		printf("Case #%d: %s\n", case_num, ans.c_str());
	}

	return 0;
}

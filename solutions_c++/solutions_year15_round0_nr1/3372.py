#include <bits/stdc++.h>
using namespace std;

void solve(int test)
{
	int n;
	string s;
	cin >> n >> s;

	int shyCount[n + 1];

	for (int i = 0; i<n+1; i++)
		shyCount[i] = s[i] - '0';

	int res = 0, up = 0;
	for (int i = 0; i<n+1; i++){
		if (!shyCount[i])
			continue;
		if (up >= i)
			up += shyCount[i];
		else {
			res += i - up;
			up = i + shyCount[i];
		}
	}

	printf("Case #%d: %d\n", test, res);
}

int main()
{
	int t;
	cin >> t;
	for (int test = 1; test <= t; test++)
		solve(test);
	return 0;
}
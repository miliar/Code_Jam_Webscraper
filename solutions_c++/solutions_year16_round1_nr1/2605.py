#define _CRT_SECURE_NO_WARNINGS
#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cstdint>
#include <algorithm>
#include <array>
using namespace std;

void solve(int num_test)
{
	string str;
	cin >> str;
	string ans;
	ans += str[0];
	for (int i = 1; i < str.size(); ++i)
	{
		if (str[i] >= ans[0])
			ans = str[i] + ans;
		else
			ans += str[i];
	}
	cout << "Case #" << num_test << ": " << ans << endl;
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	std::ios_base::sync_with_stdio(false);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		solve(i + 1);
	}
	return 0;
}
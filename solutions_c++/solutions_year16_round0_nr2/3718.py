#include <iostream>
#include <vector>
#include <set>
#include <string>
#include <cstdint>
using namespace std;

void solve(int test_case)
{
	string str;
	cin >> str;
	int ans = 0;
	int r = str.size() - 1;
	bool is = true;
	while (r >= 0)
	{
		if (str[r] == '-' && is)
		{
			++ans;
			is = !is;
		}
		else if (str[r] == '+' && !is)
		{
			++ans;
			is = !is;
		}
		--r;
	}
	cout << "Case #" << test_case << ": " << ans << endl;
}

int main(void)
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		solve(i+1);
	}
}
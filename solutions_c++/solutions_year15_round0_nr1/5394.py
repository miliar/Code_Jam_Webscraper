#include <iostream>
#include <algorithm>
#include <vector>
#include <string>
#include <map>
#include <set>

using namespace std;

void solve(int sm, string s)
{
	int col = s[0] - '0';
	int res = 0;
	for (int i = 1; i < s.length(); ++i)
	{
		int val = s[i] - '0';
		if (col < i && val > 0)
		{
			res += i - col;
			col += (i - col) + val;
		}
		else
		{
			col += val;
		}
	}
	cout << res << endl;
}

int main()
{
	freopen("C:\\out.txt", "w", stdout);
	int t;
	cin >> t;
	for (int i = 0; i < t; ++i)
	{
		int n;
		string s;
		cin >> n >> s;
		cout << "Case #" << i + 1 << ": ";
		solve(n, s);
	}
}
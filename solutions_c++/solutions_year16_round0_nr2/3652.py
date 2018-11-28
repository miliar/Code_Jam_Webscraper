#include <iostream>
#include <vector>
#include <string>
#include <algorithm>

using namespace std;

class Solution
{
public:
	void getSolution(vector<string> & cases)
	{
		const int n = cases.size();
		for (int i = 0; i < n; ++i)
		{
			int res = deal(cases[i]);
			cout << "Case #" << i + 1 << ": " << res << endl;
		}
	}

	int deal(string s)
	{
		int n = s.size();
		vector<vector<int> > f(n, vector<int>(2));
		f[0][0] = s[0] != '+';
		f[0][1] = s[0] != '-';
		for (int i = 1; i < n; ++i)
		{
			if (s[i] == '+')
			{
				f[i][0] = min(f[i - 1][0], f[i - 1][1] + 1);
				f[i][1] = min(f[i - 1][1] + 2, f[i - 1][0] + 1);
			}
			else
			{
				f[i][0] = min(f[i - 1][0] + 2, f[i - 1][1] + 1);
				f[i][1] = min(f[i - 1][1], f[i - 1][0] + 1);
			}
		}
		return min(f[n - 1][0], f[n - 1][1] + 1);
	}
};

int main()
{
	freopen("C:/Users/ywy/Desktop/large.in", "r", stdin);
	freopen("C:/Users/ywy/Desktop/large-out.txt", "w", stdout);
	//freopen("C:/Users/ywy/Desktop/in.in", "r", stdin);
	//freopen("C:/Users/ywy/Desktop/out.txt", "w", stdout);
	int n;
	cin >> n;
	vector<string> cases(n);
	for (int i = 0; i < n; ++i)
	{
		string str;
		cin >> str;
		cases[i] = str;
	}
	Solution ss;
	ss.getSolution(cases);
	return 0;
}
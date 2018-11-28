#include <iostream>
#include <algorithm>
#include <cmath>
#include <vector>
#include <string>
#include <numeric>
#include <limits>
#include <functional>
#include <set>
#include <map>
#include <fstream>

using namespace std;
typedef long long ll;
int const INF = numeric_limits<int>::max();

char inline reverse(const char &c)
{
	return (c == '-' ? '+' : '-');
}

string const IMP = "IMPOSSIBLE";

int main()
{
	ifstream cin("input.txt");
	ofstream cout("output.txt");
	int tests;
	cin >> tests;
	for (int test = 1; test <= tests; test++)
	{
		string s;
		int k;
		cin >> s >> k;
		int ans = 0;
		for (int i = 0; i <= s.size() - k; i++)
		{
			if (s[i] == '-')
			{
				ans++;
				for (int j = i; j <= i + k- 1; j++)
				{
					s[j] = reverse(s[j]);
				}
			}
		}
		bool flag = true;
		for (int i = 0; i < s.size(); i++)
		{
			if (s[i] == '-')
			{
				flag = false;
				break;
			}
		}
		cout << "Case #" << test << ": ";
		if (flag)
		{
			cout << ans << endl;
		}
		else
		{
			cout << IMP << endl;
		}
	}
    return 0;
}


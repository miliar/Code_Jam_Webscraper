#include <iostream>
#include <string>
#include <fstream>
using namespace std;
int main()
{
	freopen("A-small-attempt1.in", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int T = 1; T <= t; T++)
	{
		int x, res = 0, sum = 0;
		string s;
		cin >> x >> s;
		for (int i = 0; i < s.size(); i++)
		{
			sum += s[i] - '0';
			if (sum < i + 1)
				res += i + 1 - sum, sum += i + 1 - sum;
		}
		cout << "Case #" << T << ": " << res << endl;
	}
}
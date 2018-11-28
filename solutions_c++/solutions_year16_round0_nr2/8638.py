#include <iostream>
#include <string>
#include <stack>

using namespace std;

int main()
{
	ios::sync_with_stdio(false);
	cin.tie(nullptr);
	int T;
	cin >> T;
	for (int t = 1; t <= T; ++t)
	{
		int c = 0;
		string p;
		cin >> p;
		char x = '+';
		for (auto it = p.rbegin(); it != p.rend(); ++it)
		{
			if (*it != x) ++c;
			x = *it;
		}
		cout << "Case #" << t << ": " << c << "\n";
	}
	return 0;
}

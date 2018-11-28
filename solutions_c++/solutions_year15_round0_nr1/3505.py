#include <iostream>
#include <vector>

using namespace std;

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	cin >> t;
	for (int T = 0; T < t; ++T)
	{
		int smax;
		cin >> smax;
		int currsum = 0;
		int currans = 0;
		for (int i = 0; i <= smax; ++i)
		{
			char ch;
			cin >> ch;
			int x = ch - '0';
			if (currsum < i && x)
			{
				currans += (i - currsum);
				currsum += (i - currsum);
			}
			currsum += x;
		}
		cout << "Case #" << T + 1 << ":" << ' ' << currans << endl;
	}
}
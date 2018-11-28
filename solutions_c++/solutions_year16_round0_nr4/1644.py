#include <iostream>

using namespace std;

int main()
{
    int k, c, s, t;
    cin >> t;
    for (int i = 1; i <= t; i++)
	{
		cin >> k >> c >> s;
		cout << "Case #" << i << ": ";
		int impTest = c == 1 ? k : k - 1;
		int indexStart = c == 1 ? 0 : 1;
		if (s < impTest) cout << "IMPOSSIBLE";
		else
		{
			for (int j = indexStart; j < k - 1; j++)
			{
				cout << (j + 1) << " ";
			}
			cout << k;
		}
		cout << endl;
	}
}

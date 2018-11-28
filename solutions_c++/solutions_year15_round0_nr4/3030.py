#include <iostream>
#include <vector>
#include <string>
#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int main()
{
	freopen("C:/temp/in.txt", "r",stdin);
	freopen("C:/temp/out.txt", "w", stdout);
	int T;
	cin >> T;
	int x, r, c;
	for (int i = 1; i <= T;i++)
	{
		int z[1001];
		memset(z, 0, sizeof(z));
		cin >> x >> r >> c;

		int xmax = r*c;

		if (x == 1)
		{
			cout << "Case #" << i << ": GABRIEL" << endl;
		}
		else if (x == 2) 
		{
			if (xmax % 2 == 1)
			{
				cout << "Case #" << i << ": RICHARD" << endl;
			}
			else
			{
				cout << "Case #" << i << ": GABRIEL" << endl;
			}
		}
		else if (x == 3)
		{
			if ((xmax % 3 == 0) && (r >= 2 && c >= 2))
			{
				cout << "Case #" << i << ": GABRIEL" << endl;
			}
			else {
				cout << "Case #" << i << ": RICHARD" << endl;
			}
		}
		else if (x == 4)
		{
			if ((xmax % 4 == 0) && r > 2 && c > 2)
			{
				cout << "Case #" << i << ": GABRIEL" << endl;
			}
			else 
			{
				cout << "Case #" << i << ": RICHARD" << endl;
			}
		}
	}

	return 0;
}
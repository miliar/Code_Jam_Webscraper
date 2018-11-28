#include <iostream>
#include <algorithm>
using namespace std;
int T;
int a, b, x = 1, y;
int c, C[17];
int main()
{
	cin >> T;
	for (int x = 1; x <= T; ++x)
	{
		memset(C, 0, sizeof(C));
		y = 0;
		cin >> a;
		for (int i = 1; i <= 16; ++i)
		{
			cin >> c;
			if (i > 4*(a-1) && i <= 4*a)
				C[c] = 1;
		}
		cin >> b;
		for (int i = 1; i <= 16; ++i)
		{
			cin >> c;
			if (i > 4*(b-1) && i <= 4*b)
			{
				if (C[c] && !y)
				{
					y = c;
				} else if (C[c])
				{
					y = -1;
				}

			}
		}
		if (y == -1)
		{
			cout << "Case #" << x << ": Bad magician!" << endl;
		} else if (y == 0)
		{
			cout << "Case #" << x << ": Volunteer cheated!" << endl;
		} else
		{
			cout << "Case #" << x << ": " << y << endl;
		}
	}
}
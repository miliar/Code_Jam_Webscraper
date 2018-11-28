#include <iostream>
using namespace std;

int main()
{
	int t;
	cin >> t;
	for (int cc = 1; cc <= t; ++cc)
	{
		int x, r, c;
		cin >> x >> r >> c;
		if (x == 1)
		{
			cout << "Case #" << cc << ": GABRIEL" << endl;
		}
		else if (x == 2)
		{
			if (r % 2 == 0 || c % 2 == 0)
			{
				cout << "Case #" << cc << ": GABRIEL" << endl;
			}
			else
			{
				cout << "Case #" << cc << ": RICHARD" << endl;
			}
		}
		else if (x == 3)
		{
			if ((r * c) % 3 != 0 || (r * c) == 3)
			{
				cout << "Case #" << cc << ": RICHARD" << endl;
			}
			else
			{
				cout << "Case #" << cc << ": GABRIEL" << endl;
			}
		}
		else if (x == 4)
		{
			if ((r == 3 && c == 4) || (r == 4 && c == 3)
				|| (r == c && r == 4))
			{
				cout << "Case #" << cc << ": GABRIEL" << endl;
			}
			else
			{
				cout << "Case #" << cc << ": RICHARD" << endl;
			}
		}
		else
		{
			cout << "wrong!" << endl;
		}
	}
	return 0;
}
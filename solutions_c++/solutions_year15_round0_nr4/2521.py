#include <iostream>
using namespace::std;

main ()
{
	int T;
	cin >> T;

	for (int t = 0; t < T; ++t)
	{
		int x, r, c;
		cin >> x >> r >> c;

		if (r > c)
		{
			int tmp = r;
			r = c;
			c = tmp;
		}

		if (x == 1)
			cout << "Case #" << t + 1 << ": GABRIEL" << endl;
		else if (x == 2)
		{
			if ((r % 2) && (c % 2))
				cout << "Case #" << t + 1 << ": RICHARD" << endl;
			else
				cout << "Case #" << t + 1 << ": GABRIEL" << endl;
		}
		else if (x == 3)
		{
			if ((r > 1) && (c > 1) && ((r == 3) || (c == 3)))
				cout << "Case #" << t + 1 << ": GABRIEL" << endl;
			else
				cout << "Case #" << t + 1 << ": RICHARD" << endl;
		}
		else
		{
			if ((r > 2) && (c > 2) && ((r == 4) || (c == 4)))
				cout << "Case #" << t + 1 << ": GABRIEL" << endl;
			else
				cout << "Case #" << t + 1 << ": RICHARD" << endl;
		}
	}
}

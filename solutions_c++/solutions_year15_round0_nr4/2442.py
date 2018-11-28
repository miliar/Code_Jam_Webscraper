#include <iostream>
using namespace std;

int main()
{
	int T;
	cin >> T;
	for (int case_num = 1; case_num <= T; ++case_num)
	{
		int X, R, C;
		cin >> X >> R >> C;
		bool G;

		switch (X)
		{
		case 1:
			G = true;
			break;

		case 2:
			G = (((R * C) % 2) == 0);
			break;

		case 3:
			if ((R == 1) || (C == 1))
				G = false;
			else
				G = ((R == 3) || (C == 3));
			break;

		case 4:
			if (!((R == 4) || (C == 4)))
				G = false;
			else if ((R == 1) || (C == 1))
				G = false;
			else
			{
				if ((R == 2) || (C == 2))
					G = false;
				else
					G = true;
			}
			break;
		}

		cout << "Case #" << case_num << ": ";
		if (G)
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}
	return 0;
}
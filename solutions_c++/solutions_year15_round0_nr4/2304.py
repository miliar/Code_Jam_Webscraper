#include <iostream>


using namespace std;

int _t;
int x,r,c;

int main()
{
	cin >> _t;
	for (int _i = 0; _i < _t; ++_i)
	{
		cin >> x >> r >> c;
		cout << "Case #" << _i + 1 << ": ";
		if (x == 1)
		{
			cout << "GABRIEL\n";
		}
		if (x == 2)
		{
			if ((r * c) % 2 == 0)
				cout << "GABRIEL\n";
			else
				cout << "RICHARD\n";
		}
		if (x == 3)
		{
			if (r == 1 || c == 1 || (((r * c) % 3) != 0))
				cout << "RICHARD\n";
			else
				cout << "GABRIEL\n";
		}
		if (x == 4)
		{
			if (r < 3 || c < 3 || (((r * c) % 4) != 0))
				cout << "RICHARD\n";
			else
				cout << "GABRIEL\n";
		}
	}
}
#include <iostream>
using namespace std;

bool can_win(int x, int r, int c);

int main()
{
	int T, x, r, c;
	bool g_win;

	cin >> T;
	for (int i = 0; i < T; i++)
	{
		cin >> x >> r >> c;

		cout << "Case #" << i + 1 << ": ";

		if (can_win(x, r, c))
			cout << "GABRIEL" << endl;
		else
			cout << "RICHARD" << endl;
	}
}

bool can_win(int x, int r, int c)
{
	if (r*c % x != 0)
		return false;
	if (x >= 7)
		return false;
	if (x > r && x > c)
		return false;
	if ((x / 2) + 1*(x%2==1) > r || (x / 2) + 1*(x%2==1) > c)
		return false;
	if ((x / 2) + 1 * (x % 2 == 1) >= r ^ (x / 2) + 1 * (x % 2 == 1) >= c) //one possible orientation with respect to rows or cols
		if (x % 2 == 0 && x > 3)
			return false;
	return true;
}


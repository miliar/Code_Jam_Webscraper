#include <iostream>
using namespace std;

bool f(int x1, int y1, int x2, int y2)
{

}

bool judge(int X, int R, int C)
{
	if (R * C % X != 0)
		return true;
	if (R > C)
	{
		int t = R;
		R = C;
		C = t;
	}

	if (X > C)
		return true;

	if (X >= 7)
		return true;
	if (X == 1 || X == 2)
		return false;
	if (X == 3)
	{
		if (R == 1)
			return true;
		else
			return false;
	}
	if (X == 4)
	{
		if (R <= 2)
			return true;
		return false;
	}
	return true;
}

int main()
{
	int T, count = 0;
	cin >> T;
	while (T--){
		count++;
		int X, R, C;
		cin >> X >> R >> C;
		if (judge(X, R, C))
			cout << "Case #" << count << ": " << "RICHARD" << endl;
		else
			cout << "Case #" << count << ": " << "GABRIEL" << endl;
	}
	return 0;
}


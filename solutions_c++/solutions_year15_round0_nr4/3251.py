#include<iostream>

using namespace std;

int X, R, C;

void solveCase()
{
	cin >> X >> R >> C;

	if (X == 1)
	{
		cout << "GABRIEL";
		return;
	}

	if (((R * C) % X) != 0)
	{
		cout << "RICHARD";
		return;
	}

	if (X == 2)
	{
		cout << "GABRIEL";
		return;
	}

	if ((X > R) && (X > C))
	{
		cout << "RICHARD";
		return;
	}

	int tmp = (X / 2) + (X % 2);
	if ((tmp > R) || (tmp > C))
	{
		cout << "RICHARD";
		return;
	}
	
	if (X == 3)
	{
		cout << "GABRIEL";
		return;
	}

	if ((R == X && C == 2) || (C == X && R == 2))
	{
		cout << "RICHARD";
		return;
	}

	cout << "GABRIEL";
}

int main()
{
	int cases;
	cin >> cases;
	for (int c = 0; c < cases; c++)
	{
		cout << "Case #" << c + 1 << ": ";
		solveCase();
		cout << endl;
	}
}

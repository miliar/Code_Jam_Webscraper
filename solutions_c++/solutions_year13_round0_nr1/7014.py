#include <cstdio>
#include <cstdlib>
#include <iostream>

using namespace std;

const int size = 4;

char t[size+1][size+1];

void Write(char ch, int test);

void Read()
{
	for (int i = 0; i < size; ++i)
	{
		for (int j = 0; j < size; ++j)
			cin >> t[i][j];
		
	}
}

bool Win(char ch)
{
	for (int i = 0; i < size; ++i)
	{
		bool win = true;
		for (int j = 0; j < size; ++j)
			if (t[i][j] != ch && t[i][j] != 'T')
				win = false;
		if (win)
			return win;
	}
	for (int i = 0; i < size; ++i)
	{
		bool win = true;
		for (int j = 0; j < size; ++j)
			if (t[j][i] != ch && t[j][i] != 'T')
				win = false;
		if (win)
			return win;
	}

	int win;
	win = true;
	for (int i = 0; i < size; ++i)
	{
		if (t[i][i] != ch && t[i][i] != 'T')
				win = false; 
	}
	if (win)
		return win;

	win = true;
	for (int i = 0; i < size; ++i)
	{
		if (t[i][size - i - 1] != ch && t[i][size - i - 1] != 'T')
				win = false; 
	}
	if (win)
		return win;
	else
		return false;

}

bool NotFinished()
{
	for (int i = 0; i < size; ++i)
		for (int j = 0; j < size; ++j)
			if (t[i][j] == '.')
				return true;
	return false;
}
void Solve(int test)
{
	bool wx = Win('X');
	bool wo = Win('O');
	if (wx)
		if (wo)
			Write('D', test);
		else
			Write('X', test);
	else
		if (wo)
			Write('O', test);
		else
			if (NotFinished())
				Write('N', test);
			else
				Write('D', test);

}

void Write(char ch, int test)
{
	cout << "Case #" << test + 1<< ": ";
	if (ch == 'X')
	{
		cout << "X won";

	}
	if (ch == 'O')
	{
		cout << "O won";

	}
	if (ch == 'D')
	{
		cout << "Draw";

	}
	if (ch == 'N')
	{
		cout << "Game has not completed";

	}
	cout << endl;
}

int main()
{
	freopen("ain", "r", stdin);
	freopen("aout", "w", stdout);
	int T;
	cin >> T; 
	for (int test = 0; test < T; ++test)
	{
		Read();
		Solve(test);
	}
}

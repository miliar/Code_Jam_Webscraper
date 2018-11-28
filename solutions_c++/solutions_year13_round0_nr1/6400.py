#include <iostream>
#include <string>
using namespace std;

void print(char data[][4])
{
	int i, j;
	for (i = 0; i < 4; ++i)
	{
		for (j = 0; j < 4; ++j)
			cout << data[i][j];
		cout << endl;
	}
}

/*
 * -2: "Game has not completed"
 * -1: "Draw"
 * +1: "X won"
 * +2: "O won"
 */

int analyze_row(char data[][4])
{
	int i, j, val = -2;
	bool finish = true;

	for (i = 0; i < 4; ++i)
	{
		int X_COUNT = 0, O_COUNT = 0;
		for (j = 0; j < 4; ++j)
		{
			if (data[i][j] == '.')
			{
				finish = false;
			}
			else
			{
				if (data[i][j] == 'X' || data[i][j] == 'T') ++X_COUNT;
				if (data[i][j] == 'O' || data[i][j] == 'T') ++O_COUNT;
			}
		}
		if (X_COUNT == 4) return 1;
		if (O_COUNT == 4) return 2;
	}

	if (finish) val = -1;
	return val;
}

int analyze_column(char data[][4])
{
	int i, j, val = -2;
	bool finish = true;

	for (i = 0; i < 4; ++i)
	{
		int X_COUNT = 0, O_COUNT = 0;
		for (j = 0; j < 4; ++j)
		{
			if (data[j][i] == '.')
			{
				finish = false;
			}
			else
			{
				if (data[j][i] == 'X' || data[j][i] == 'T') ++X_COUNT;
				if (data[j][i] == 'O' || data[j][i] == 'T') ++O_COUNT;
			}
		}
		if (X_COUNT == 4) return 1;
		if (O_COUNT == 4) return 2;
	}

	if (finish) val = -1;
	return val;
}

int analyze_diagonal(char data[][4])
{
	int i, X_COUNT = 0, O_COUNT = 0, val = -2;
	bool finish = true;

	for (i = 0; i < 4; ++i)
	{
		if (data[i][i] == '.')
		{
			finish = false;
		}
		else
		{
			if (data[i][i] == 'X' || data[i][i] == 'T') ++X_COUNT;
			if (data[i][i] == 'O' || data[i][i] == 'T') ++O_COUNT;
		}
		if (X_COUNT == 4) return 1;
		if (O_COUNT == 4) return 2;
	}

	X_COUNT = 0, O_COUNT = 0;

	for (i = 0; i < 4; ++i)
	{
		if (data[i][3 - i] == '.')
		{
			finish = false;
		}
		else
		{
			if (data[i][3 - i] == 'X' || data[i][3 - i] == 'T') ++X_COUNT;
			if (data[i][3 - i] == 'O' || data[i][3 - i] == 'T') ++O_COUNT;
		}
		if (X_COUNT == 4) return 1;
		if (O_COUNT == 4) return 2;
	}

	if (finish) val = -1;
	return val;
}

void analyze(int id)
{
	char data[4][4];
	int i, j;
	for (i = 0; i < 4; ++i)
		for (j = 0; j < 4; ++j)
			cin >> data[i][j];

	//print(data);

	int v1 = analyze_row(data);
	int v2 = analyze_column(data);
	int v3 = analyze_diagonal(data);

	string s;

	if (v1 == 2 || v2 == 2 || v3 == 2)
		s = "O won";
	else if (v1 == 1 || v2 == 1 || v3 == 1)
		s = "X won";
	else if (v1 == -1 && v2 == -1 && v3 == -1)
		s = "Draw";
	else
		s = "Game has not completed";

	cout << "Case #" << id << ": " << s << endl;
}

int main(int argc, char* argv[])
{
	int i, test = 0;
	cin >> test;
	for (i = 0; i < test; ++i)
		analyze(i + 1);
	return 0;
}
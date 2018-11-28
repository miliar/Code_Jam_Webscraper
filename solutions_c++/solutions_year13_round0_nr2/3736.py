#include <iostream>
#include <string>

using namespace std;

class Lawn
{
private:
	int ** myLawn;
	int row;
	int col;
	bool checkRow(int r);
	bool checkCol(int c, int val);

public:
	void getLawn();
	bool check();

};

void Lawn::getLawn()
{
	cin >> row >> col;
	myLawn = new int* [row];
	for (int i = 0; i < row; i++)
		myLawn[i] = new int[col];
	for (int i = 0; i < row; i++)
		for (int k = 0; k < col; k++)
		{
			cin >> myLawn[i][k];
		}

}

bool Lawn::check()
{
	for (int i = 0; i < row; i++)
		if (!checkRow(i))
			return false;

	return true;
	
}

bool Lawn::checkRow(int r)
{
	int max = myLawn[r][0];
	for (int i = 1; i < col; i++)
		if (myLawn[r][i] > max)
			max = myLawn[r][i];
	for (int i =0; i < col; i++)
	{
		if (myLawn[r][i] < max)
			if (! checkCol (i, myLawn[r][i]))
				return false;
	}
	return true;
}

bool Lawn::checkCol(int c, int val)
{
	for (int i = 0; i < row; i++)
		if (myLawn[i][c] > val)
			return false;
	return true;
}

int main()
{
	int numOfCases;
	Lawn* cases;

	cin >> numOfCases;
	cases = new Lawn[numOfCases];

	for (int i = 0; i < numOfCases; i++)
	{
		cases[i].getLawn();
	}

	for (int i = 0; i < numOfCases; i++)
	{
		cout << "Case #" << i+1 << ": ";
		if (cases[i].check())
			cout << "YES";
		else
			cout << "NO";
		cout << endl;
	}
}



#include<fstream>
using namespace std;
int findMatch(int*, int*, int*);
int main()
{
	int counter, firstRow, secondRow, firstOrder[4][4], secondOrder[4][4];
	int fTemp[4], sTemp[4];
	
	ifstream in;
	ofstream out;
	in.open("A-small-attempt0.in");
	out.open("output.out");
	in >> counter;
	for (int i = 1; i <= counter; i++)
	{
		in >> firstRow;
		for (int x = 0; x < 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				in >> firstOrder[x][y];
			}

		}
		for (int m = 0; m < 4; m++)
		{
			fTemp[m] = firstOrder[firstRow-1][m];
		}
		in >> secondRow;
		for (int x = 0; x < 4; x++)
		{
			for (int y = 0; y < 4; y++)
			{
				in >> secondOrder[x][y];
			}
		}
		for (int m = 0; m < 4; m++)
		{
			sTemp[m] = secondOrder[secondRow-1][m];
		}
		int number = 0;
		int result = findMatch(fTemp, sTemp, &number);
		switch (result)
		{
		case 0:
		{out << "Case #" << i << ": Volunteer cheated!" << endl;
		break; }
		case 1:
		{out << "Case #" << i << ": " << number << endl;
		break; }

		default:out << "Case #" << i << ": Bad magician!" << endl;

		}
	}
	return 0;
}
int findMatch(int *first, int *second, int *number)
{
	int counter = 0;
	for (int i = 0; i < 4; i++)
	{
		for (int j = 0; j < 4; j++)
		{
			if (first[i] == second[j])
			{
				counter++;
				*number = first[i];
			}
		}
	}
	return counter;
}
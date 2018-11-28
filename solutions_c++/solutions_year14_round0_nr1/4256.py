#include<iostream>
#include<fstream>
using namespace std;

int main()
{
	int count = 0,temp,_1st,_2nd,i,j,k;
	int row1[4], row2[4];
	ifstream fin("A-small-attempt0.in");
	ofstream fout("output.txt");
	fin >> count;
	
	for (i = 0; i < count; i++)
	{
		fin >> _1st;
		for (j = 0; j < 4; j++)
		{
			for (k = 0; k < 4; k++)
			{
				if (j+1 == _1st)
					fin >> row1[k];
				else
					fin >> temp;
			}
		}
		
		fin >> _2nd;
		for (j = 0; j < 4; j++)
		{
			for (k = 0; k < 4; k++)
			{
				if (j+1 == _2nd)
					fin >> row2[k];
				else
					fin >> temp;
			}
		}

		int matches = 0;
		int value = 0;
		for (j = 0; j < 4; j++)
		{
			for (k = 0; k < 4; k++)
			{
				if (row1[j] == row2[k])
				{
					++matches;
					value = row1[j];
				}
			}
		}

		fout << "Case #" << i+1<<": ";
		if (matches == 1)
			fout << value;
		else
		{
			if (matches > 1)
				fout << "Bad magician!";
			else
				fout << "Volunteer cheated!";
		}
		fout << endl;
	}
	return 0;
}
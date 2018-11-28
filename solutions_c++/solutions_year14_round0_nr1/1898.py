#include<iostream>
#include<stdio.h>
#include<fstream>
using namespace std;

int main()
{
	int test,a,b,row,col,first[10][10],second[10][10],count,var,index;
	fstream fp("B-small-practice.in",ios::in);
	fstream op("B-small-practice.out", ios::out);

	index = 0;
	row = 4;
	col = 4;

	fp >> test;
	while (test--)
	{

		fp >> a;
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				fp >> first[i][j];

			}

		}

		fp >> b;
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				fp >> second[i][j];

			}

		}

		count = 0;
		var = 0;
		for (int i = 0; i < row; i++)
		{
			for (int j = 0; j < col; j++)
			{
				if (first[a-1][i] == second[b-1][j])
				{
					count++;
					var = first[a-1][i];
				}
			}

		}

		index++;
		op << "Case #"<<index<<": ";
		if (count>1)
			op << "Bad magician!" << endl;
		else if (!count)
			op << "Volunteer cheated!" << endl;
		else
			op << var << endl;


	}

}
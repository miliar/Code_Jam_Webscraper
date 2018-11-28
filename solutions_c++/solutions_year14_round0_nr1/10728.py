#include<iostream>
#include<fstream>
using namespace std;
void main()
{
	ifstream in("A-small-attempt1.in");
	ofstream out("output.txt");
	int A[4][4];
	int B[4][4];
	int row1,row2;
	int test;
	in >> test;
	for (int t = 0; t < test; t++)
	{
		out << "Case #" << t+1 << ": ";
		in >> row1;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> A[i][j];
			}
		}
		in >> row2;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				in >> B[i][j];
			}
		}
		int check = 0;
		int number;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				if (A[row1 - 1][i] == B[row2 - 1][j])
				{
					number = A[row1 - 1][i];
					check++;
				}
			}
		}
		if (check == 0)
		{
			out << "Volunteer cheated!" << endl;
		}
		else if (check == 1)
		{
			out << number << endl;
		}
		else
		{
			out << "Bad magician!" << endl;
		}
	}
}
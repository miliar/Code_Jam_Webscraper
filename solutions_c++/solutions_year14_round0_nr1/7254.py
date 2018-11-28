#include<iostream>
#include<fstream>
#include<iomanip>
#include<algorithm>
#include<string>

using namespace std;

void main()
{

	int first[4][4];
	int second[4][4];
	int loop;
	ifstream  infile;
	infile.open("A-small-attempt0.in");
	ofstream outfile;
	outfile.open("out.txt");
	int firstrow, secondrow;
	int value;

	infile >> loop;
	for (int h = 0; h < loop; h++)
	{


		infile >> firstrow;

		int count = 0;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				infile >> first[i][j];
			}
		}

		infile >> secondrow;
		for (int i = 0; i < 4; i++)
		{
			for (int j = 0; j < 4; j++)
			{
				infile >> second[i][j];
			}
		}

		firstrow = firstrow - 1;
		secondrow = secondrow - 1;

		for (int i = 0; i < 4; i++){
			for (int j = 0; j < 4; j++)
			{
				if (first[firstrow][i] == second[secondrow][j])
				{
					count++;
					value = first[firstrow][i];
				}
			}
		}


		if (count == 0)
			outfile << "Case #" << h+1 << ": Volunteer cheated!" << endl;
		else if (count == 1)
			outfile << "Case #" << h+1 << ": " << value << endl;
		else
			outfile << "Case #" << h+1 << ": Bad magician!" << endl;
	}


		system("pause");











}
#include <iostream>
#include <fstream>
using namespace std;

int main()
{
	ifstream ifile;
	ofstream ofile;
	ifile.open("A-small-attempt0.in");
	if (ifile.fail())
	{
		exit(1);
	}
	ofile.open("magic_output.in");
	if (ofile.fail())
	{
		exit(1);
	}
	int test_case;
	ifile >> test_case;
	int ans1 = 0, ans2 = 0, a1[4], a2[4],temp[4], count = 0, number = 0;
	for (int i = 1; i <= test_case; i++)
	{
		ifile >> ans1;
		for (int j = 1; j <= 4; j++)
		{
			if (j == ans1)
			{
				ifile >> a1[0] >> a1[1] >> a1[2] >> a1[3];
			}
			else
			{
				ifile >> temp[0] >> temp[1] >> temp[2] >> temp[3];
			}
		}
		ifile >> ans2;
		for (int j = 1; j <= 4; j++)
		{
			if (j == ans2)
			{
				ifile >> a2[0] >> a2[1] >> a2[2] >> a2[3];
			}
			else
			{
				ifile >> temp[0] >> temp[1] >> temp[2] >> temp[3];
			}
		}
		count = 0;
		for (int j = 0; j < 4; j++)
		{
			for (int k = 0; k < 4; k++)
			{
				if (a1[j] == a2[k])
				{
					count++;
					number = a1[j];
				}
			}
		}
		ofile << "Case #" << i << ": ";
		if (count == 1)
			ofile << number << endl;
		else if (count > 1)
			ofile << "Bad magician!" << endl;
		else
			ofile << "Volunteer cheated!" << endl;
	}
	ifile.close();
	ofile.close();
	return 0;
}
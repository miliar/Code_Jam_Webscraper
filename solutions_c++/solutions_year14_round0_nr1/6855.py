#include<iostream>
#include<fstream>
#include<iomanip>
using namespace std;

int main(int argc, char* argv[])
{

	ifstream inp;
	ofstream outp;
	inp.open("A-small-attempt0.in");
	outp.open("output.txt");
	int i, j, k, l, N;
	int row[4];
	int choice1, choice2, junk, var;
	int range, matches = 0, matched;
	inp >> N;
	for (i = 1; i <= N; i++)
	{
		inp >> choice1;
		range = 4 * (choice1 - 1) + 1;
		for (j = 1; j <= 16; j++)
		{
			if ( j == range)
			{
				for (k = 0; j < range + 4; j++, k++)
				{
					inp >> row[k];
				}
				j--;
			}
			else
			{
				inp >> junk;
			}
		}

		inp >> choice2;
		range = 4 * (choice2 - 1) + 1;
		for (j = 1; j <= 16; j++)
		{
			if ( j == range)
			{
				for (k = 0; j < range + 4; j++, k++)
				{
					inp >> var;
					for (l = 0; l < 4; l++)
					{
						if (row[l] == var)
						{
							matches++;
							matched = var;
						}
					}
				}
				j--;
			}
			else
			{
				inp >> junk;
			}
		}
		
		outp << "Case #" << i << ": ";
		if (matches == 0)
			outp << "Volunteer cheated!"  << endl;
		else if (matches == 1)
			outp << matched << endl;
		else
			outp << "Bad magician!"  << endl;
		matches = 0;
	}
	outp.close();
	inp.close();
	return 0;
}

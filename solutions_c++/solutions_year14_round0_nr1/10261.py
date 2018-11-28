#include <iostream>
#include <fstream>

using namespace std;

int main()
{
	ifstream infile;
	infile.open("A-small-attempt3.in");
	ofstream ofile;
	ofile.open("output.out");
	int count = 1;
	int T;
	int flag = 0; 
	int card = 0;
	infile >> T;
	while (infile.good() && count <= T)
	{
		int fr[4][4],sr[4][4];
		int p1,p2;
		infile >> p1;
		for (int r = 0; r < 4; r++)
		{
			for (int c = 0; c < 4; c++)
			{
				infile >> fr[r][c];
			}
		}
		infile >> p2;
		for (int r = 0; r < 4; r++)
		{
			for (int c = 0; c < 4; c++)
			{
				infile >> sr[r][c];
			}
		}
		for (int c = 0; c < 4; c++)
		{
			for (int x = 0; x < 4; x++)
			{
				if (fr[p1 - 1][c] == sr[p2 - 1][x])
				{
					flag++;
					card = fr[p1 - 1][c];
				}
			}
		}
		if (flag == 1)
		{
			ofile << "Case #" << count << ": " << card << endl;
		}
		else if (flag == 0 )
		{
			ofile << "Case #" << count << ": " << "Volunteer cheated!" << endl;
		}
		else
		{
			ofile << "Case #" << count << ": " << "Bad magician!" << endl;
		}
		flag = 0;
		card = 0;
		count++;
	}
	ofile.close();
	infile.close();
	cout << endl;

}

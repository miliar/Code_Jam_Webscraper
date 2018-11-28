#include<fstream>
using namespace::std;
int main()
{
	ifstream infile;
	infile.open("A-small-attempt0.in");

	ofstream outfile;
	outfile.open("out.out");

	int t;
	infile >> t;

	for(int l = 1; l <= t; l++)
	{
		int ans1, ans2;
		int pos1[16], pos2[16];
		for(int i = 0; i < 16; i++)
		{
			pos1[i] = 0;
			pos2[i] = 0;
		}
		
		infile >> ans1;

		for(int i = 1; i <= 4; i++)
		{
			for(int j = 1; j <= 4; j++)
			{
				int d;
				infile >> d;
				pos1[d-1] = i;
			}
		}

		infile >> ans2;

		for(int i = 1; i <= 4; i++)
		{
			for(int j = 1; j <= 4; j++)
			{
				int d;
				infile >> d;
				pos2[d-1] = i;
			}
		}

		int found[16];
		for(int i = 0; i < 16; i++)
		{
			found[i] = 0;
		}

		for(int i = 0; i < 16; i++)
		{
			if((pos1[i] == ans1) && (pos2[i] == ans2))
				found[i] = 1;
		}

		outfile << "Case #" << l << ": ";

		int c = 0;
		for(int i = 0; i < 16; i++)
		{
			if(found[i] == 1)
				c++;
		}

		if(c == 1)
		{
			for(int i = 0; i < 16; i++)
			{
				if(found[i] == 1)
					outfile << i+1 << endl;
			}
		}
		if(c == 0)
			outfile << "Volunteer cheated!" << endl;
		if(c > 1)
			outfile << "Bad magician!" << endl;
	}
	return 0;
}
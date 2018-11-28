/*
 *	Tested with GCC 4.8.2 on Linux x86_64
 */

#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
using namespace std;

int main()
{
	int T;
	int ans;
	int row[2][4]; // row[0][] is the first selected row from the first permutation, row[1][] the 2nd

	ifstream in("A-small-attempt2.in");
	string line;

	if(in.is_open())
	{	
		getline(in, line);
		stringstream(line) >> T;

		for(int t=1; t <= T; t++)
		{
			for(int n=0; n<2; n++)
			{
				getline(in, line);
				stringstream(line) >> ans;

				for(int r = 1; r <= 4; r++)
				{
					getline(in, line);
					if(ans == r)
						stringstream(line) >> row[n][0] >> row[n][1] >> row[n][2] >> row[n][3];
				}
			}
			// count the number of matches between the first and the second selected row
			int nmatch = 0, match=0;
			for(int i=0; i<4; i++)
				for(int j=0; j<4; j++)
					if(row[0][i] == row[1][j])
					{
						nmatch++;
						match=row[0][i];
					}

			// display results
			cout << "Case #" << t << ": ";
			if(nmatch < 1)
				cout << "Volunteer cheated!" << endl;
			else if(nmatch > 1)
				cout << "Bad magician!" << endl;
			else
				cout << match << endl;
		}
		in.close();
	}
	return 0;
}

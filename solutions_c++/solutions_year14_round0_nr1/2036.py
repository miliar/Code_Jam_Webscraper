#include <iostream>
#include <fstream>
#include <string>
using namespace std;

const char * const BAD = "Bad magician!";
const char * const CHEAT = "Volunteer cheated!";

enum eResult {eUnknown, eFOUND, eBAD, eCHEAT} ;

void main()
{
	ifstream in("input.in");
	ofstream out("output.out");
	
	int T = 0;
	in>>T;

	for (int _case = 1; _case <= T;  _case++)
	{
		int remainRow = 0;
		string temp;

		int row1 = 0;
		in >> row1;
		remainRow = 4 - row1;

		int line1[4];
		
		while (row1 > 0)
		{
			getline(in, temp);
			row1--;
		}
		in >> line1[0]; in >> line1[1]; in >> line1[2]; in >> line1[3];
		getline(in, temp);
		while (remainRow > 0)
		{
			getline(in,temp);
			remainRow--;
		}

		int row2 = 0;
		in >> row2;

		remainRow = 4 - row2;
		int line2[4];
		
		while (row2 > 0)
		{
			getline(in,temp);
			row2--;
		}
		in >> line2[0]; in >> line2[1]; in >> line2[2]; in >> line2[3];
		getline(in, temp);
		while (remainRow > 0)
		{
			getline(in,temp);
			remainRow--;
		}

		eResult result = eUnknown;
		int card = 0;
		for (int i = 0; i < 4; i++)
		{
			int c = line1[i];
			for (int j = 0; j < 4; j ++)
			{
				if( line2[j] == c)
				{
					result = (result >= eFOUND) ? eBAD : eFOUND;
					card = c;
				}
			}

			if (i==3 && result == eUnknown)
			{
				result = eCHEAT;
			}
		}

		//output
		switch (result)
		{
			case eFOUND:
			{
				out << "Case #" << _case <<": " << card <<endl;
				break;
			}
			case eBAD:
			{
				out << "Case #" << _case <<": "<< BAD <<endl;
				break;
			}
			case eCHEAT:
			{
				out << "Case #" << _case <<": "<< CHEAT <<endl;
				break;
			}
		}
	}

	in.close();
	out.close();
}
#include<iostream>
#include<fstream>

using namespace std;

int writeSummary(int row1, int arg1[], int row2, int arg2[]);

int main ()
{
	ifstream myfileIn;
	myfileIn.open ("C:/stack/oldstuff/Computer Languages/Google/sample.txt");
	if(!myfileIn.good())
	{
		return 0;
	}
	int cases = 0;
	myfileIn >> cases;
	
	ofstream myfileOut;
	myfileOut.open ("C:/stack/oldstuff/Computer Languages/Google/out.txt");
	for(int i = 0; i < cases; i++)
	{
		int row1;
		int arangment1[16];
		int row2;
		int arangment2[16];
		myfileIn >> row1;
		for(int j = 0; j < 16; j++)
		{
			myfileIn >> arangment1[j];
		}
		myfileIn >> row2;
		for(int j = 0; j < 16; j++)
		{
			myfileIn >> arangment2[j];
		}
		int ans;
		ans = writeSummary(row1, arangment1, row2, arangment2);
		cout << "Case #" << (i+1) << ": ";
		myfileOut << "Case #" << (i+1) << ": ";
		if(ans == 0)
		{
			cout << "Bad magician!";
			myfileOut << "Bad magician!";
		}
		else if(ans == -1)
		{
			cout << "Volunteer cheated!";
			myfileOut << "Volunteer cheated!";
		}
		else
		{
			cout << ans;
			myfileOut << ans;
		}
		cout << endl;
		myfileOut << endl;
	}

	return 0;
}

int writeSummary(int row1, int arg1[], int row2, int arg2[])
{
	int sol = 0;
	for(int i = 0; i < 4; i++)
	{
		for(int j = 0; j < 4; j++)
		{
			if(arg1[((row1-1)*4)+i] == arg2[((row2-1)*4)+j])
			{
				if(sol == 0)
				{
					sol = arg1[((row1-1)*4)+i];
				}
				else
				{
					return 0;
				}
			}
		}
	}
	if(sol)
	{
		return sol;
	}
	else
	{
		return -1;
	}
}
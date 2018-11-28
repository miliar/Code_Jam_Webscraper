#include<iostream>
#include<fstream>
#include<string>
using namespace std;

int main()
{
	ifstream fin("A-large.in");
	ofstream fout("output.txt");

	int T, Smax, *arr, i, j, TotalShynessLevel, FriendsNeeded, temp;
	string Stringarray;
	fin >> T;
	for (i = 0; i < T; i++)
	{
		fin >> Smax;
		arr = new int[Smax + 1];
		fin >> Stringarray;

		TotalShynessLevel = 0;
		FriendsNeeded = 0;
		for (j = 0; j < Smax + 1; j++)
		{
			arr[j] = Stringarray[j] - 48;
			if (arr[j] != 0)
			{
				if (TotalShynessLevel < j)
				{
					temp = j - TotalShynessLevel;
					TotalShynessLevel += temp;
					FriendsNeeded += temp;
				}
				TotalShynessLevel += arr[j];
			}
		}

		fout << "Case #" << i + 1 << ": " << FriendsNeeded << endl;
	}
	return 0;
}
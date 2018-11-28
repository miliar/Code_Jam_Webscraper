//Code Jam 2015 Qualifier
//Standing Ovation

#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main(void)
{
	int t, smax, standing, friends;

	ifstream fin;
	ofstream fout;

	fin.open("A-large.in");
	fout.open("output.txt");

	fin >> t;

	for (int i = 1; i <= t; i++)
	{
		friends = 0;
		fin >> smax;		//read smax
		int * s = new int[smax + 1];		//dynamically allocate array of size smax + 1, to include 0
		string shystring;

		fin >> shystring;

		for (int j = 0; j <= smax; j++)		//for each index of array s
		{
			s[j] = shystring.at(j) - '0';					//read corresponding value
		}

		standing = s[0];				//initial number of people standing

		for (int j = 1; j <= smax; j++)
		{
			if (j > standing)			//if people standing are less than needed for shyness i
			{
				friends += (j - standing);		//add number of friends needed for shyness index i
				standing += (s[j] + j - standing);
			}
			else			//enough people are standing for shyness index i
				standing += s[j];
		}

		fout << "Case #" << i << ": " << friends << endl;
	}

	return 0;
}
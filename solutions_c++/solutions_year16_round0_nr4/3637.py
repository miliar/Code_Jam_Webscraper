#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main()
{
	int cases, curCase, k, startLen, complexity, students;
	string answer;
	ifstream fin;
	ofstream fout;
	fin.open("input.txt");
	fout.open("output.txt");

	fin>>cases;
	curCase = 1;
	while(curCase <= cases)
	{
		answer = "";
		fin>>startLen>>complexity>>students;

		if (startLen == 1) // Only one tile to check
		{
			answer = " 1";
		}
		else if (students < startLen - 1) // Must always be able to check at least K - 1 tiles
			answer = " IMPOSSIBLE";
		else if (complexity == 1)	// Must check all tiles
		{
			if (students < startLen)
				answer = " IMPOSSIBLE";
			else
			{
				for (k = 1; k <= startLen; k++)
				{
					answer += " " + to_string(k);
				}
			}
		}
		else // Check starting K tiles, since C > 1 you can now skip the first tile
		{
			for (k = 2; k <= startLen; k++)
				{
					answer += " " + to_string(k);
				}
		}

		fout<<"Case #"<<curCase<<":"<<answer<<endl;
		curCase++;
	}
	return 0;
}
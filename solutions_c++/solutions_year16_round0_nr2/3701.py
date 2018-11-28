#include<string>
#include<iostream>
#include<fstream>
#include<math.h>
#include<stdlib.h>
using namespace std;

int main(void)
{
	ifstream file;
	file.open("B-large.in");
	ofstream output;
	output.open("result.out");

	int caseNo;
	file >> caseNo;

	for (int t = 1; t <= caseNo; t++)
	{
		char s[101];
		file >> s;

		int flips = 0;
		char last;

		if (s[1] == '\0')
		{
			if (s[0] == '+') flips = 0;
			else if (s[0] == '-') flips = 1;
		}
		else
		{
			for (int tt = 1; s[tt] != '\0'; tt++)
			{
				if (s[tt - 1] != s[tt]) flips++;
				last = s[tt];
			}
			if (last == '-') flips++;
		}
		output << "Case #" << t << ": ";
		output << flips << endl;
	}
}
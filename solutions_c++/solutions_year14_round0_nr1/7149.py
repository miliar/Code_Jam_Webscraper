#include<iostream>
#include<fstream>
using namespace std;

ifstream fin("A-small-attempt0.in");
ofstream fout("A-small-attempt0.out");

int fr[18], T, x, i, j, c, card,a;

int main()
{
	fin >> T;
	int tmp = T;
	while (T--)
	{
		fin >> x;
		c = 0;
		for (i = 1; i <= 4;++i)
		for (j = 1; j <= 4; ++j)
		{
			fin >> a;
			if (i == x)
				fr[a]++;
		}
		fin >> x;
		for (i = 1; i <= 4; ++i)
		for (j = 1; j <= 4; ++j)
		{
			fin >> a;
			if (i == x)
				fr[a]++;
		}
		for (i = 1; i <= 16; ++i)
		{
			if (fr[i] == 2)
			{
				c++;
				card = i;
			}
			fr[i] = 0;
		}
		fout << "Case #" << tmp-T << ": ";
		if (c == 1)
			fout << card << '\n';
		if (c > 1)
			fout << "Bad magician!\n";
		if (c == 0)
			fout << "Volunteer cheated!\n";

	}
	return 0;
}
#include <iostream>
#include <fstream>
#include <string>
using namespace std;

ofstream fout("out.txt");
ifstream fin("A-small-attempt1.in");
int main()
{
	int t;
	fin >> t;
	int a;
	for (a = 1; a <= t; a++)
	{
		int num1[4], num2[4];
		int nu1, nu2, h, h1, h2, h3, h4, ans;
		fin >> nu1;
		for (h = 0; h <= 3; h++)
		{
			if (h == nu1 - 1)
				fin >> num1[0] >> num1[1] >> num1[2] >> num1[3];
			else
				fin >> h1 >> h2 >> h3 >> h4;
		}
		//fout << num1[0] << endl;
		fin >> nu2;
		for (h = 0; h <= 3; h++)
		{
			if (h == nu2 - 1)
				fin >> num2[0] >> num2[1] >> num2[2] >> num2[3];
			else
				fin >> h1 >> h2 >> h3 >> h4;
		}
		h = 0;
		for (h1 = 0; h1 <= 3; h1++)
		for (h2 = 0; h2 <= 3; h2++)
		{
			if (num1[h1] == num2[h2])
			{
				ans = num1[h1];
				h++;
			}
		}
		if (h == 0)
			fout << "Case #" << a << ": Volunteer cheated!" << endl;
		else if (h == 1)
			fout << "Case #" << a << ": " << ans << endl;
		else
			fout << "Case #" << a << ": Bad magician!" << endl;
	}
    return 0;
}
#include <iostream>
#include <fstream>
#include <cstring>
using namespace std;
bool mark1[20], mark2[20];
int main()
{
	ifstream fin("A.in");
	ofstream fout("aans.out");
	int t;
	fin >> t;
	for (int test = 1; test <= t; test++)
	{
		memset(mark1, false, sizeof(mark1));
		memset(mark2, false, sizeof(mark2));
		int ans1, ans2;
		fin >> ans1;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int val;
				fin >> val;
				if (i == ans1 - 1)
					mark1[val] = true;
			}
		fin >> ans2;
		for (int i = 0; i < 4; i++)
			for (int j = 0; j < 4; j++)
			{
				int val;
				fin >> val;
				if (i == ans2 - 1)
					mark2[val] = true;
			}
		int t = 0, ans = -1;
		for (int i = 1; i <= 16; i++)
			if (mark1[i] && mark2[i])
			{
				t++;
				ans = i;
			}
		fout << "Case #" << test << ": ";
		if (t == 0)
			fout << "Volunteer cheated!" << endl;
		if (t == 1)
			fout << ans << endl;
		if (t >= 2)
			fout << "Bad magician!" << endl;
	}
	return 0;
}

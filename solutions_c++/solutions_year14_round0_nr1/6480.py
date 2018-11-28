#include <fstream>
using namespace std;
int T, ans[2], lin[2][17], rez;

int main()
{
	int t, i, j, x;
	ifstream fin("A.in");
	ofstream fout("A.out");
	fin >> T;
	for(t = 1; t <= T; ++t)
	{
		fin >> ans[0];
		for(i = 1; i <= 4; ++i)
		{
			for(j = 1; j <= 4; ++j)
			{
				fin >> x;
				lin[0][x] = i;
			}
		}
		fin >> ans[1];
		for(i = 1; i <= 4; ++i)
		{
			for(j = 1; j <= 4; ++j)
			{
				fin >> x;
				lin[1][x] = i;
			}
		}
		rez = 0;
		for(i = 1; i <= 16; ++i)
		{
			if(lin[0][i] == ans[0] && lin[1][i] == ans[1])
			{
				if(rez == 0)
					rez = i;
				else
				{
					if(rez > 0)
						rez = -1;
				}
			}
		}
		fout << "Case #" << t << ": ";
		if(rez > 0)
			fout << rez << "\n";
		else
		{
			if(rez == 0)
				fout << "Volunteer cheated!\n";
			else
				fout << "Bad magician!\n";
		}
	}
	fin.close();
	fout.close();
	return 0;
}

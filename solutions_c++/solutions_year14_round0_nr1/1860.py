#include <fstream>

using namespace std;

int main(void)
{
	ofstream fout("Output.out");
	ifstream fin("Input.in");
	int Ncase, Ncurrent, ansA, ansB, a[4][4], b[4][4], ans, i, j;

	fin >> Ncase;
	for(Ncurrent = 1; Ncurrent <= Ncase; Ncurrent++)
	{
		ans = 0;
		fin >> ansA;
		ansA--;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				fin >> a[i][j];
		fin >> ansB;
		ansB--;
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				fin >> b[i][j];
		for (i = 0; i < 4; i++)
			for (j = 0; j < 4; j++)
				if (a[ansA][i] == b[ansB][j])
				{
					if (ans == 0)
						ans = a[ansA][i];
					else
					{
						fout << "Case #" << Ncurrent << ": Bad magician!" << endl;
						goto FINISH;
					}
				}
		if (ans == 0)
			fout << "Case #" << Ncurrent << ": Volunteer cheated!" << endl;
		else
			fout << "Case #" << Ncurrent << ": " << ans << endl;
		FINISH:;
	}
	return 0;
}



#include <iostream>
#include <fstream>
using namespace std;
ofstream fout("D:\\out.txt");
void judgeGame(int a[4][4],int b[4][4],int i,int j)
{
	int cnt = 0;
	int num;
	for (int p = 0; p < 4; p++){
		for (int q = 0; q < 4; q++){
			if (a[i][p] == b[j][q])
			{
				cnt++;
				num = a[i][p];
			}
		}
	}
	if (cnt == 0)
		fout << "Volunteer cheated!" << endl;
	else if (cnt == 1)
		fout << num << endl;
	else if (cnt>1)
		fout << "Bad magician!" << endl;
}
int main()
{
	ifstream fin("D:\\A-small-attempt0.in");
	int T;
	fin >> T;
	for (int tests = 0; tests < T; tests++)
	{
		int i, j, first[4][4], second[4][4];
		fin >> i;
		for (int m = 0; m < 4; m++){
			for (int n = 0; n < 4; n++){
				fin >> first[m][n];
			}
		}

		fin >> j;

		for (int m = 0; m < 4; m++){
			for (int n = 0; n < 4; n++){
				fin >> second[m][n];
			}
		}

		fout << "Case #" << tests + 1 << ": ";
		judgeGame(first, second, i - 1, j - 1);
	}
}


#include <iostream>
#include <fstream>
using namespace std;
ofstream fout("result.txt");
int main()
{
	int n;
	cin >> n;
	for (int i = 1;i <= n;i++)
	{
		char s[2001];
		int d[10],x[27];
		for (int j = 0;j < 10;j++) d[j] = 0;
		for (int j = 0;j < 27;j++) x[j] = 0;
		cin >> s;
		for (int j = 0;j < strlen(s) ;j++)
		{
			if (s[j] == 'Z') d[0]++;
			else if (s[j] == 'W') d[2]++;
			else if (s[j] == 'X') d[6]++;
			else if (s[j] == 'G') d[8]++;
			else if (s[j] == 'U') d[4]++;
			x[int(s[j]) - 64]++;
		}
		x['E' - 64] -= d[0];
		x['R' - 64] -= d[0];
		x['O' - 64] -= d[0];
		x['T' - 64] -= d[2];
		x['O' - 64] -= d[2];
		x['O' - 64] -= d[4];
		x['U' - 64] -= d[4];
		x['R' - 64] -= d[4];
		x['S' - 64] -= d[6];
		x['I' - 64] -= d[6];
		x['E' - 64] -= d[8] * 2;
		x['I' - 64] -= d[8];
		x['H' - 64] -= d[8];
		x['T' - 64] -= d[8];
		d[3] = x['T' - 64];
		x['H' - 64] -= d[3];
		x['E' - 64] -= d[3] * 2;
		x['R' - 64] -= d[3];
		d[7] = x['S' - 64];
		x['E' - 64] -= d[7] * 2;
		x['V' - 64] -= d[7];
		x['N' - 64] -= d[7];
		d[5] = x['V' - 64];
		x['F' - 64] -= d[5];
		x['I' - 64] -= d[5];
		x['E' - 64] -= d[5];
		d[9] = x['I' - 64];
		x['N' - 64] -= d[9] * 2;
		x['E' - 64] -= d[9];
		d[1] = x['O' - 64];
		fout << "Case #" << i << ": ";
		for (int j = 0;j <= 9;j++)
		{
			for (int k = 1;k <= d[j];k++)
			{
				fout << j;
			}
		}
		fout << endl;
	}
	return 0;
}
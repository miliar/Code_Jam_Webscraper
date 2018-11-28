#include <iostream>
#include <fstream>
#include <string>
#define N 2000000
using namespace std;

int pa[N];
int cntp = 10;

char num[N][10];
int cntn = 10;
int cnt[10] = {1, 10};

int main()
{
	ifstream infile("C-small-attempt1.in");
	ofstream outfile("C-s.out", ios::out);
	int T;
	infile >> T;
	int i, j, k, m;
	for (i = 0;i < 10;i++)
	{
		pa[i] = i;
		num[i][0] = i + '0';
		num[i][1] = '\0';
	}

	int start = -1;
	for (i = 2;i <= 8;i++)
	{
		for (j = 0;j < i;j++)
		{
			num[cntn][j] = '0';
		}
		num[cntn++][i] = '\0';
		cnt[i] ++;

		for (j = '1';j <= '9';j++)
		{

			for (k = 0;k < cnt[i-2];k++)
			{
				num[cntn][0] = j;
				num[cntn][i-1] = j;
				num[cntn][i] = '\0';
				for (m = 1;m < i-1;m++)
					num[cntn][m] = num[start+k][m-1];

				pa[cntp++] = atoi(num[cntn]);
				cntn++;
				cnt[i]++;

			}
		}
		start += cnt[i-2];
	}
	int testcase;
	for (testcase = 1;testcase <= T;testcase++)
	{
		double a, b;
		infile >> a >> b;
		int x = ceil(sqrt(a));
		int y = floor(sqrt(b));
		i = 0;
		int result = 0;
		while (true)
		{
			if (i == 4)
				i = 10;
			if (pa[i] >= x && pa[i] <= y)
				result++;
			if (pa[i] > y)
				break;
			i++;
		}
		outfile << "Case #" << testcase << ": ";
		outfile << result;
		outfile << endl;
	}
	return 0;
}
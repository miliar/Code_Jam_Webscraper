#include <fstream>
#include <memory.h>

using namespace std;

const int MAX = 1024;

int pPlates[MAX];

int main()
{
	ifstream fin("B.in");
	ofstream fout("B.out");
	int T, D, nTmp, ans;
	fin >> T;
	for(int i = 1; i <= T; i++)
	{
		ans = 2147483647;
		memset(pPlates, 0, sizeof(pPlates));
		fin >> D;
		for(int j = 1; j <= D; j++)
		{
			fin >> nTmp;
			pPlates[nTmp]++;
		}
		for(int j = 1000; j >= 1; j--)
		{
			int nTmp = 0;
			for(int k = MAX - 1; k > j; k--)
			{
				if(pPlates[k])
				{
					nTmp += pPlates[k] * (k / j + (k % j != 0) - 1);
				}
			}
			nTmp += j;
			ans = min(ans, nTmp);
		}
		fout << "Case #" << i << ": " << ans << endl;
	}
	return 0;
}

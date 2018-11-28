#include <fstream>

using namespace std;

const int MAX = 1024;

int pData[MAX];

int main()
{
	ifstream fin("A.in");
	ofstream fout("A.out");
	int T, N, x, y, nRate;
	fin >> T;
	for(int i = 1; i <= T; i++)
	{
		fin >> N; x = y = 0;
		nRate = 0;
		for(int j = 1; j <= N; j++)
		{
			fin >> pData[j];
		}
		for(int j = 1; j < N; j++)
		{
			if(pData[j] > pData[j + 1])
			{
				x += pData[j] - pData[j + 1];
				nRate = max(nRate, pData[j] - pData[j + 1]);
			}
		}
		for(int j = 1; j < N; j++)
		{
			y += min(nRate, pData[j]);
			pData[j] -= nRate;
			pData[j + 1] = max(pData[j], pData[j + 1]);
		}
		fout << "Case #" << i << ": " << x << " " << y << endl;
	}
	return 0;
}


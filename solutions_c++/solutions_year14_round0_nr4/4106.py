#include <iostream>
#include <algorithm>
#include <string>
#include <vector>
#include <stack>
#include <queue>
#include <deque>
#include <unordered_set>
#include <map>
#include <fstream>
#include <cstring>

using namespace std;

#define MAXN 1001

int T, N;
double W[2][MAXN];
int nCount(int i, int j);

int main()
{
	string filename = "D-large";
	ifstream fin(filename + ".in");
	FILE *fout = fopen((filename + ".out").c_str(), "w");

	fin >> T;
	for(int t = 1; t <= T; t++)
	{
		fin >> N;
		for(int i = 0; i < 2; i++)
		{
			for(int j = 0; j < N; j++)
			{
				fin >> W[i][j];
			}
		}
		sort(W[0], W[0] + N, greater<double>());
		sort(W[1], W[1] + N, greater<double>());

		int dC = 0, fL = N - 1, sL = N - 1;
		while(fL >= 0)
		{			
			if(W[0][fL] > W[1][sL])
			{
				dC++;
				sL--;
			}
			fL--;
		}

		int nC = 0, fP = 0, sP = 0;
		while(fP < N)
		{
			if(W[0][fP] > W[1][sP])
			{
				nC++;
			}
			else
			{
				sP++;
			}
			fP++;
		}

		fprintf(fout, "Case #%d: %d %d\n", t, dC, nC);
	}

	fin.close();
	fclose(fout);
 	return 0;
}
#include <windows.h>
#include <stdio.h>
#include <math.h>
#include <vector>
#include <map>
#include <list>
#include <set>
#include <iostream>
#include <fstream>
#include <algorithm>

using namespace::std;

int main(int argc, char* argv[])
{
	ifstream cin(argv[1]);

	int nCount, numCase = 1;
	cin >> nCount;

	while (numCase <= nCount)
	{
		int N, M;
		cin >> N >> M;

		vector<int> buf;
		buf.resize(N * M);

		vector<int> hVert;
		hVert.resize(N, 0);

		vector<int> hHorz;
		hHorz.resize(M, 0);

		for (int j = 0; j < N; j++)
		{
			for (int i = 0; i < M; i++)
			{
				int n;
				cin >> n;
				buf[j * M + i] = n;

				if (n > hVert[j])
					hVert[j] = n;

				if (n > hHorz[i])
					hHorz[i] = n;
			}
		}

		bool b = true;
		for (int j = 0; j < N && b; j++)
		{
			for (int i = 0; i < M && b; i++)
			{
				int x = buf[j * M + i];
				if (x < hVert[j] && x < hHorz[i])
					b = false;
			}
		}

		cout << "Case #" << numCase << ": ";
		cout << (b ? "YES" : "NO");
		cout << "\n";

		numCase++;
	}
	return 0;
}

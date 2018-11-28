#include <cstdio>
#include <vector>
#include <deque>
#include <queue>
#include <map>
#include <algorithm>
#include <functional>
#include <iostream>
#include <fstream>
#include <string>
#include <cmath>
#include <string.h>

using namespace std;

int findMax(int* p, int n, int& index)
{
	int max = 0;
	for (int i = 0; i < n; i++)
	{
		if (max < p[i])
		{
			max = p[i];
			index = i;
		}
	}
	return (max);
}

int findMaxR(int* p, int n, int& index)
{
	int max = 0;
	for (int i = n - 1; i > -1; i--)
	{
		if (max < p[i])
		{
			max = p[i];
			index = i;
		}
	}
	return (max);
}

int main(int argc, const char **argv)
{
    if (argc != 2)
    {
        fprintf(stderr, "Error:%d\n", __LINE__);
        return -1;
    }

    ifstream fin(argv[1]);
    ofstream fout("out.txt");

    int T;
    fin >> T;
	for (int j = 0; j < T; j++)
	{
		int N;
		fin >> N;

		int P[26];
		for (int i = 0; i < N; i++)
		{
			fin >> P[i];
		}

		string S = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";

		int index = 0;
		int max = findMax(P, N, index);

		fout << "Case #" << j + 1 << ":";
		while (max != 0)
		{
			fout << " " << S[index];
			P[index]--;
			int index2 = -1;
			int max2 = -1;
			max = findMax(P, N, index);
			max2 = findMaxR(P, N, index2);
			if (max == 0)
			{
				break;
			}
			if (index2 == index)
			{
				fout << S[index];
				P[index]--;
				max = findMax(P, N, index);
			}
		}
		fout << endl;
	}
    return (0);
}

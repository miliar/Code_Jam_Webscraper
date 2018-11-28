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
    for (long long j = 0; j < T; j++)
    {
		string S;
		fin >> S;
        int K;
        fin >> K;

		int n = 0;
		bool allHappy = true;

		for (int i = 0; i + K <= S.length(); i++)
		{
			if (S[i] == '-')
			{
				for (int k = 0; k < K; k++)
				{
					if (S[i + k] == '-')
					{
						S[i + k] = '+';
					}
					else
					{
						S[i + k] = '-';
					}
				}
				n++;
			}
		}

		for (int i = 0; i < S.length(); i++)
		{
			if (S[i] == '-')
			{
				allHappy = false;
				break;
			}
		}

		if (allHappy == false)
		{
			fout << "Case #" << j + 1 << ": " << "IMPOSSIBLE" << endl;
		}
		else
		{
			fout << "Case #" << j + 1 << ": " << n << endl;
		}
    }
	
    return (0);
}

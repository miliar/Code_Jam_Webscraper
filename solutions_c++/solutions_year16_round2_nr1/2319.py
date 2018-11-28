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
	for (int j = 0; j < T; j++)
	{
		string S;
		fin >> S;

		int d[10] = {0};
		int s[26] = {0};

		for (int i = 0; i < S.length(); i++)
		{
			s[S[i] - 'A']++;
		}

		for (int i = 0; i < s[25]; i++)
		{
			s[4]--;
			s[17]--;
			s[14]--;
		}
		d[0] = s[25];
		for (int i = 0; i < s[22]; i++)
		{
			s[19]--;
			s[14]--;
		}
		d[2] = s[22];
		for (int i = 0; i < s[20]; i++)
		{
			s[5]--;
			s[14]--;
			s[17]--;
		}
		d[4] = s[20];
		for (int i = 0; i < s[23]; i++)
		{
			s[18]--;
			s[8]--;
		}
		d[6] = s[23];
		for (int i = 0; i < s[6]; i++)
		{
			s[4]--;
			s[8]--;
			s[7]--;
			s[19]--;
		}
		d[8] = s[6];

		for (int i = 0; i < s[14]; i++)
		{
			s[13]--;
			s[4]--;
		}
		d[1] = s[14];
		for (int i = 0; i < s[19]; i++)
		{
			s[7]--;
			s[17]--;
			s[4]--;
			s[4]--;
		}
		d[3] = s[19];
		for (int i = 0; i < s[5]; i++)
		{
			s[8]--;
			s[21]--;
			s[4]--;
		}
		d[5] = s[5];
		for (int i = 0; i < s[18]; i++)
		{
			s[4]--;
			s[21]--;
			s[4]--;
			s[13]--;
		}
		d[7] = s[18];

		d[9] = s[8];

		fout << "Case #" << j + 1 << ": ";
		for (int i = 0; i < 10; i++)
		{
			for (int k = 0; k < d[i]; k++)
			{
				fout << i;
			}
		}
		fout << endl;
	}
    return (0);
}


#include <stdio.h>
#include <stdlib.h>
#include <sstream>
#include <iostream>
#include <fstream>

using namespace std;

int getStepsNum(int* num, int N)
{
	int max_chars = 0;
	int min_chars = 101;
	for (int i = 0; i < N; i++)
	{
		if (max_chars < num[i])
			max_chars = num[i];
		if (min_chars > num[i])
			min_chars = num[i];
	}

	int min_diff = 1000;
	int optimal_number = 1000;
	for (int j = min_chars; j <= max_chars; j++)
	{
		int diff = 0;
		for (int i = 0; i < N; i++)
		{
			diff += abs(num[i] - j);
		}
		if (diff < min_diff)
		{
			min_diff = diff;
			optimal_number = j;
		}
	}

	int moves = 0;
	for (int i = 0; i < N; i++)
	{
		if (optimal_number != num[i])
		{
			moves += abs(num[i] - optimal_number);
		}
	}
	return moves;
}

int main()
{
	FILE *in;
	if (fopen_s(&in, "A-small-attempt3.in", "r+") != 0)
		printf("The in file was not opened\n");

	fstream out("A-small-attempt3.out", ios::out);
	if (out.bad())
		printf("The out file was not opened\n");

	int T;
	fscanf_s(in, "%d", &T);

	const int maxN = 100;
	const int maxLen = 101;
	char strings[maxN * maxLen];
	char* pS[maxN];
	int  num[maxN];

	for (int tc = 1; tc <= T; tc++)
	{
		int N;
		fscanf_s(in, "%d\n", &N);
		memset(strings, 0, maxN * maxLen);

		for (int i = 0; i < N; i++)
		{
			fscanf_s(in, "%s", (strings + maxLen*i), maxLen);
			pS[i] = strings + maxLen*i;
		}

		int steps = 0;
		bool possible = true;

		for (int j = 0; j < maxLen; j++)
		{
			char c = *pS[0];
			if (c == 0)
			{
				for (int i = 0; i < N; i++)
				{
					if (*pS[i] != 0)
					{
						possible = false;
						break;
					}
				}
				break;
			}

			for (int i = 0; i < N; i++)
			{
				if (*pS[i] != c)
				{
					possible = false;
					break;
				}

				char* p = pS[i];
				num[i] = 0;
				while (*p == c)
				{
					pS[i]++;
					num[i]++;
					p = pS[i];
				}
			}
			steps += getStepsNum(num, N);

			if (!possible)
				break;
				
			//for (int i = 0; i < N; i++)				printf("i: %d, chars = %d\n", i, num[i]);
		}
		
		//for (int i = 0; i < N; i++)			printf("%s\n", strings + maxLen*i);

		if (!possible)
		{
			cout << "Case #" << tc << ": Fegla Won" << endl;
			out << "Case #" << tc << ": Fegla Won" << endl;
		}
		else
		{
			cout << "Case #" << tc << ": " << steps << endl;
			out << "Case #" << tc << ": " << steps << endl;
		}
	}

	out.close();
	getchar();
}
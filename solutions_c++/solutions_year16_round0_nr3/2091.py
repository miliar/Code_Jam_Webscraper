#include <iostream>
#include <fstream>
#include <string>
#include <set>
#include <cmath>
#define LL long long
#define MAXN 40
using namespace std;

const int jugMax = 10;
int bit[MAXN];
int res[10];

int min(int x, int y)
{
	return x < y ? x : y;
}

bool plusBit( int N )
{
	int i;
	for ( i = 1; i < N; i++)
	{
		if (bit[i] == 1)
		{
			bit[i] = 0;
		}
		else
		{
			bit[i] = 1;
			break;
		}
	}

	if (bit[N - 1] == 0) return false;

	return true;
}

int jugBit(int N, int jug)
{
	int tmp[MAXN] = {0};
	int ret = 1;

	while (ret < jug)
	{
		bool bValid = true;

		for (int i = 0; i < N; i++)
		{
			tmp[i] = bit[i];
		}

		for (int i = 0; i < N; i++)
		{
			if (tmp[i] && i+ret < N )
			{
				if (tmp[i + ret] == 0 )
				{
					bValid = false;
					break;
				}
				else
				{
					tmp[i] = tmp[i + ret] = 0;
					continue;
				}
			}
		}

		for (int i = 0; i < N; i++)
		{
			if (tmp[i])
			{
				bValid = false;
				break;
			}
		}

		if (bValid) break;
		else ret++;
	}

	return ret;
}

int main()
{
	fstream fin("in.txt");
	fstream fout("out.txt");

	int T;
	fin >> T;
	for (int t = 1; t <= T; t++ )
	{
		int N, J;
		fin >> N >> J;
		memset(bit, 0, sizeof(bit));
		bit[0] = bit[N - 1] = 1;

		int cnt = 0;
		fout << "Case #" << t << ":" << endl;

		int jug = min(jugMax, N);

		while (cnt < J)
		{
			plusBit(N);
			int x = jugBit(N, jug);
			if (x == jug) continue;
			else
			{
				for (int i = N - 1; i >= 0; i--)
				{
					fout << bit[i];
				}
				for (int i = 2; i <= 10; i++)
				{
					fout << " " << (LL)pow((LL)i, x) + 1;
				}
				fout << endl;
				cnt++;
			}
		}
		
	}
	return 0;
}
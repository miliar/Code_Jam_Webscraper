#include <cstdio>
#include <cstdlib>
#include <iostream>
#include <string>
#include <fstream>
#include <vector>
//#define DEBUG

using namespace std;

int m[1024];
int main(int argc, char* argv[])
{
	FILE* pf_in = fopen(argv[1], "r");
	FILE* pf_out = fopen(argv[2], "w");

	int T;
	fscanf(pf_in, "%d", &T);
	for(int i = 1; i <= T; i++)
	{
		int N;
		fscanf(pf_in, "%d", &N);
		int c2_rate = 0;
		for(int j = 0; j < N; j++)
		{
			fscanf(pf_in, "%d", &m[j]);

			if(j > 0)
			{
				int rate = m[j - 1] - m[j];
				if(rate > c2_rate)
				{
					c2_rate = rate;
				}
			}
		}

		int c1 = 0, c2 = 0;
		for(int j = 0; j < N - 1; j++)
		{
			if(m[j] - m[j + 1] > 0)
			{
				c1 += m[j] - m[j + 1];
			}

			if(m[j] >= c2_rate)
			{
				c2 += c2_rate;
			}
			else
				if(m[j] < c2_rate)
				{
					c2 += m[j];
				}
		}
		fprintf(pf_out, "Case #%d: %d %d\n", i, c1, c2);
#ifdef DEBUG
#endif
#ifdef DEBUG
#endif

#ifdef DEBUG
#endif
	}
	return 0;
}


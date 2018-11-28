#define _CRT_SECURE_NO_WARNINGS

#include <cstdio>
#include <cstdlib>
#include <algorithm>
#include <vector>

using namespace std;

inline int ctoi(char c) { return ((c) - '0'); }

const int maxn = 1000 + 10;


int process_input(char *in, int smax)
{
	int cs; // cumulative sum
	cs = ctoi(in[0]);

	int res = 0;
	int req = 0;

	// processing 
	for (int i = 1; i <= smax; i++)
	{
		if (in[i] != '0' && cs < i)
		{
			req = (i - cs);
			res += req;
			cs += req;
		}

		cs = cs + ctoi(in[i]);
	}

	return res;
}

int doit()
{
	int smax;
	char in[maxn];

	// input
	scanf("%d", &smax);
	scanf("%s", in);

	return process_input(in, smax);
}

int main()
{
#ifdef localhost
	freopen("data/A-large.in", "r", stdin);
	freopen("data/output_large.txt", "w", stdout);
#endif

	int res, t, kase = 0;
	scanf("%d", &t);
	while (t--)
	{
		res = doit();
		printf("Case #%d: %d\n", ++kase, res);
	}

	return 0;
}
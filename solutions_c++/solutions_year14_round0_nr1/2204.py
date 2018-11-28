#include <stdio.h>
#include <stdarg.h>
#include <cstring>
#include <algorithm>
#include <vector>
#include <cmath>
#define clr(a) memset(a, 0, sizeof(a))

typedef std::pair<int, int> pii;
typedef long long ll;

void dbg(const char * fmt, ...)
{
	#if 1
		va_list args;
		va_start(args, fmt);
		vfprintf(stdout, fmt, args);
		va_end(args);
		fflush(stdout);
	#endif
}

int ar[4][4];

void solve(int test_case)
{
	printf("Case #%d: ", test_case);
	int mask = (1<<16) - 1;
	for(int t = 0; t < 2; t++)
	{
		int k;
		scanf("%d", &k); k--;
		for(int i = 0; i < 4; i++)
			for(int j = 0; j < 4; j++)
			{
				scanf("%d", &ar[i][j]);
				ar[i][j]--;
			}
		int tmp = 0;
		for(int i = 0; i < 4; i++)
			tmp = tmp | (1 << ar[k][i]);
		mask = mask & tmp;				
	}
	if (mask == 0)
		printf("Volunteer cheated!\n");
	else if (mask & (mask - 1))
		printf("Bad magician!\n");
	else
	{
		for(int i = 0; i < 16; i++)
			if (mask & (1<<i))
				printf("%d\n", i+1);
	}
}

int main()
{
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++)
		solve(i + 1);


	return 0;
}

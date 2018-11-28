#include<stdio.h>
#include<iostream>
#include<math.h>

#define max(a, b) ((a) > (b)?(a):(b))
#define min(a, b) ((a) < (b)?(a):(b))

#define SZ 105

using namespace std;

long long memo[SZ][2];
char str[SZ];

int main()
{
	//freopen("test.in", "rt", stdin);
	freopen("B-large.in", "rt", stdin);
	freopen("b-large.out", "wt", stdout);
	int inp, i, kase, j;
	long long k, c, s;
	scanf("%d", &inp);
	for (kase = 1; kase <= inp; kase++)
	{
		scanf("%s", str);
		memset(memo, -1, sizeof(memo));
		if (str[0] == '-')
		{
			memo[0][0] = 1;
			memo[0][1] = 0;
		}
		else
		{
			memo[0][0] = 0;
			memo[0][1] = 1;
		}

		int len = strlen(str);
		for (i = 01; i < len; i++)
		{
			if (str[i] == '-')
			{
				memo[i][0] = memo[i - 1][1] + 1;
				memo[i][1] = memo[i - 1][1];
			}
			else
			{
				memo[i][0] = memo[i - 1][0];
				memo[i][1] = memo[i - 1][0] + 1;
			}
		}
		
		printf("Case #%d: %lld\n", kase, memo[len - 1][0]);
		
	}
	return 0;
}

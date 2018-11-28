#include<stdio.h>
#include<iostream>
#include<math.h>

#define max(a, b) ((a) > (b)?(a):(b))
#define min(a, b) ((a) < (b)?(a):(b))

#define SZ 105

using namespace std;

long long memo[SZ][2];
bool flag[11];
char str[SZ];

int main()
{
	//freopen("test.in", "rt", stdin);
	freopen("A-large.in", "rt", stdin);
	freopen("a-large.out", "wt", stdout);
	int inp, i, kase, j;
	long long k, c, s;
	scanf("%d", &inp);
	for (kase = 1; kase <= inp; kase++)
	{
		scanf("%lld", &k);
		memset(flag, false, sizeof(flag));
		int fcnt = 0;
		
		printf("Case #%d: ", kase);

		if (k == 0)
		{
			printf("INSOMNIA\n");
			continue;
		}
		c = k;
		while (true)
		{
			long long tmp = c;
			while (tmp > 0)
			{
				int d = tmp % 10;
				if (flag[d] == false)
				{
					flag[d] = true;
					fcnt++;
				}
				tmp /= 10;
			}
			if (fcnt == 10)
			{
				break;
			}
			c += k;
		}
		printf("%lld\n", c);
		
	}
	return 0;
}

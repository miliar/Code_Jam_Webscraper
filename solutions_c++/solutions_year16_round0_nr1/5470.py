#pragma warning(disable : 4996)
#include <stdio.h>
#include <iostream>
#include <set>

using namespace std;

void process(int t)
{
	printf("Case #%d: ", t + 1);
	long long N;
	scanf("%lld", &N);
	if (N == 0)
		printf("INSOMNIA");
	else
	{
		long long M = 0;
		set<int> s;
		int res = 0;
		while (s.size() < 10)
		{
			
			M += N;
			res = M;
			long long a = M;
			while (a > 0)
			{
				s.insert(a % 10);
				a /= 10;
			}
		}
		printf("%d", res);
	}
	printf("\n");
}

int main()
{
	freopen("d:\\acm\\CodeJam\\2016\\CodeJamQual\\A\\A.in", "r", stdin);
	freopen("d:\\acm\\CodeJam\\2016\\CodeJamQual\\A\\A.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		process(t);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}
#include <cstdio>
#include <iostream>
#include <cmath>
using namespace std;
int gcd(int a, int b)
{
	while (b != 0)
	{
		a = a % b;
		swap(a, b);
	}
	return a;
}

bool check(int a)
{ 
	int temp = 1;
	for(;;)
	{
		if ( a < temp)
			return false;
		else if ( a == temp)
			return true;
		else temp <<= 1; 
	}
}

int main()
{
	freopen("output.out","w",stdout);
	int t;
		scanf("%d",&t);
	for (int tcase = 1; tcase <= t; tcase++)
	{
		int p,q;
		scanf("%d/%d", &p, &q);
		int temp = gcd(p, q);
		p /= temp;
		q /= temp;
		printf("Case #%d: ", tcase);
		if (!check(q))
		{
			printf("impossible\n");
			continue;
		}
		else
		{
			double k = (double)q/p;
			int ans = ceil(log2(k));
			printf("%d\n", ans);
		}
	}
	fclose(stdout);
	return 0;
}
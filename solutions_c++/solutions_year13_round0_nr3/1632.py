#include <cstdio>
using namespace std;

/*bool isPal(long long x)
{
	int mas[20] = {0}, k = 0;
	bool res = true;
	while (x > 0)
	{
		mas[k] = x % 10;
		x = x / 10;
		k++;
	}
	for (int j = 0; j < k / 2; j++)
		if (mas[j] != mas[k - j - 1])
			res = false;

	return res;
} */
long long mas[] = {1, 4, 9, 121, 484, 10201, 12321, 14641, 40804, 44944, 1002001, 1234321, 4008004, 100020001, 102030201, 104060401, 121242121, 123454321, 125686521, 400080004, 404090404, 10000200001, 10221412201, 12102420121, 12345654321, 40000800004, 1000002000001, 1002003002001, 1004006004001, 1020304030201, 1022325232201, 1024348434201, 1210024200121, 1212225222121, 1214428244121, 1232346432321, 1234567654321, 4000008000004, 4004009004004, 100000020000001, 100220141022001, 102012040210201, 102234363432201, 121000242000121, 121242363242121, 123212464212321, 123456787654321};
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
/*	printf("mas[] = {");
	int c = 0;
	for (int i = 1; i <= 20000000; i++)
	{
		long long p = i;
		if (isPal(p) && isPal(p*p))
		{
			printf("%lld, ", p*p);
			c++; 
		}
	}
	printf("\n");
	printf("%d", c); */

	int num;
	scanf("%d", &num);
	for (int i = 1; i <= num; i++)
	{
		long long l, r;
		int res = 0;
		scanf("%lld %lld", &l, &r);
		for (int j = 0; j < 47; j++)
			if (mas[j] >= l && mas[j] <= r)
				res++;
		printf("Case #%d: %d\n", i, res);
	}

	return 0;
}
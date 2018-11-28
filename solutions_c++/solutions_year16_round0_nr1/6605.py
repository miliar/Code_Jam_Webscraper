#include <cstdio>
int T, N;
unsigned long long calc(unsigned long long n)
{
	unsigned long long sum = n;
	int check = 0;
	while (true)
	{
		unsigned long long tmp = sum;
		while (tmp)
		{
			int jari = tmp % 10;
			tmp /= 10;
		//	printf("jari %d %d\n", jari, 1 << jari);
			check |= (1 << jari);
		//	printf("%d\n", check);
		}
		if (check == 0x3FF)
			return sum;
		//printf("%d\n", sum);
		sum += n;
	}
}
int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large-output", "w", stdout);
	scanf("%d", &T);
	for (int t = 1; t <= T; t++)
	{
		unsigned long long n;
		scanf("%llu", &n);
		if (n == 0){
			printf("Case #%d: INSOMNIA",t);
		}
		else{
			printf("Case #%d: %llu",t, calc(n));
		}
		if (t != T)
			putchar('\n');
	}
}
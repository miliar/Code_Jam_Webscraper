#include<stdio.h>
int main()
{
	long long t, i;
	char str[256];
	long long n,j;
	freopen("inputB.txt", "r", stdin);
	freopen("outputB.txt", "w", stdout);
	scanf("%lld", &t);
	for (i = 0; i < t; i++)
	{
		scanf("%s", &str);
		n = 0;
		for (j = 1; str[j] == '+' || str[j] == '-'; j++)
		{
			if (str[j - 1] != str[j])
				n++;
		}
		if (str[j - 1] == '-')
			n++;
		printf("case #%lld: %lld\n", i + 1, n);
	}
	return 0;
}
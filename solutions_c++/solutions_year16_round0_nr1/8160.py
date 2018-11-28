#include <iostream>
#include <cstdio>

using namespace std;

int main()
{
	int test_case, n, check_bit;
//	printf("1 << 2 = %d", (1 << 2));

	scanf("%d", &test_case);
	for (int test = 1; test <= test_case; test++)
	{
		scanf("%d", &n);
		check_bit = 0;
		for (int i = 1; i <= 100; i++)
		{
			int res = i * n;
			while (1)
			{
				check_bit = (check_bit | (1 << (res % 10)));
				res /= 10;
				if (res == 0)
					break;
			}
			if (check_bit == 1023)
			{
				printf("Case #%d: %d\n", test, i * n);
				break;
			}
		}
		if (check_bit != 1023)
			printf("Case #%d: INSOMNIA\n", test);
	}

	return 0;
}

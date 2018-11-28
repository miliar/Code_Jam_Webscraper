#include <cstdio>
#include <iostream>

using namespace std;

int arr[10];

int check(int ar[])
{
	int i;
	for (i = 0; i < 10; i++)
	{
		if (ar[i] == 0) return 0;
	}
	return 1;
}

int main(void)
{
	freopen("inputA.txt", "r", stdin);
	freopen("outputA.txt", "w", stdout);
	int i, j;
	int t;
	int n;

	int result;
	int comp = 0;

	scanf("%d", &t);
	for (i = 0; i < t;i++)
	{
		memset(arr, 0, sizeof(arr));
		j = 2;
		scanf("%d", &n);
		result = n;
		while (1)
		{
			if (n == 0) break;
			while (1)
			{
				arr[result%10] = 1;
				result = result / 10;
				if (result == 0)
					break;
			}
			if (check(arr) == 1) break;
			result = n * j;
			comp = result;
			j++;
		}
		if (n == 0)
			printf("Case #%d: INSOMNIA\n", i + 1);
		else
			printf("Case #%d: %d\n", i + 1, comp);
	}
}
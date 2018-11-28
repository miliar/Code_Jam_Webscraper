#include <cstdio>

using namespace std;

int T, A, B;

int D[] = {1,4,9,121,484,10201,12321,14641,40804,44944};

bool palindrom(int num)
{
	int n = num, rev = 0, dig;
	while (num > 0)
	{
		dig = num % 10;
		rev = rev * 10 + dig;
		num = num / 10;
	}
	return n == rev;
}

int main()
{
	scanf("%d", &T);

	int i, res;

	for(int t = 1; t <= T; t++)
	{
		res = 0;
		scanf("%d %d", &A, &B);

		/*for(int x = A; x <= B; x++)
		{
			if(palindrom(x) && palindrom(x*x))
			{
				printf("%d,", x*x);
				i++;
			}
		}
		printf("\n%d\n\n", i);*/

		for(i = 0; i < 10; i++)
		{
			if(D[i] >= A) res++;
			if(D[i] > B) res--;
		}

		printf("Case #%d: %d\n", t, res);
	}

	return 0;
}

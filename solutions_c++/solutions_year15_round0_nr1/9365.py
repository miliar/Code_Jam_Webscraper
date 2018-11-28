#include <cstdio>
#include <cstdlib>

void solve(int testCase)
{
	int S, res = 0;
	scanf("%d ", &S);
	int standing = getchar() - '0';

	for(int shyness = 1; shyness <= S; ++shyness)
	{
		int p = getchar() - '0';
		//printf("%d %d |", standing, p);
		if(p == 0) continue;
		if(shyness > standing)
		{
			res += (shyness - standing);
			standing += p + (shyness - standing);
		}
		else
			standing += p;

	}
	printf("Case #%d: %d\n", testCase, res);
}

int main(void)
{
	int n;
	scanf("%d", &n);
	for(int i = 1; i <= n; ++i) solve(i);
	return EXIT_SUCCESS;
}

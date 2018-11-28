#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;

int num_case, N, J, num[35], ans[11];

bool check(int key)
{
	long long now = 0;
	/*for (int i = 1; i <= N; i++)
		printf("%d", num[i]);
	printf(" ");*/
	for (int i = 1; i <= N; i++)
		now = now * key + num[i];
	//printf("%d ", now);
	for (int i = 2; i <= (int)sqrt(now + 0.5); i++)
		if (now % i == 0)
		{
			//printf("OK\n");
			ans[key] = i;
			return 1;
		}
	//printf("NO!\n");
	return 0;
}

void calc()
{
	for (int i = 2; i <= 10; i++)
		if (!check(i))
			return;
	for (int i = 1; i <= N; i++)
		printf("%d", num[i]);
	printf(" ");
	for (int i = 2; i < 10; i++)
		printf("%d ", ans[i]);
	printf("%d\n", ans[10]);
	J--;
}

void search(int dep)
{
	if (dep == N && J)
	{
		calc();
		return;
	}
	num[dep] = 0;
	search(dep + 1);
	if (!J) return;
	num[dep] = 1;
	search(dep + 1);
}

int main()
{
	freopen("3.in", "r", stdin);
	freopen("3.out", "w", stdout);
	scanf("%d", &num_case);
	scanf("%d %d", &N, &J);
	printf("Case #1:\n");
	num[1] = num[N] = 1;
	search(2);
	return 0;
}

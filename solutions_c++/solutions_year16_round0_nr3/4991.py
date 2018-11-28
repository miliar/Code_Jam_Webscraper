#include <cstdio>
int A;
int C;
const int Lim = 50;
const int N = 16;
int path[N];
long long B[11];
long long P[N][11];
bool IsPrime(long long x)
{
	for(long long i = 2;;i++)
	{
		if (i * i > x) break;
		if (x % i == 0) return false;
	}
	return true;
}
bool check()
{
	for(int i = 2; i <= 10; i++)
	{
		if(IsPrime(B[i])) return false;
	}
	return true;
}
void Get()
{
	C++;
	for(int i = N - 1; i >= 0; i--) printf("%d", path[i]);
	printf(" ");
	for(int i = 2; i <= 10; i++)
	{
		for(int j = 2;; j++)
		{
			if(B[i] % j == 0)
			{
				printf("%d ", j);
				break;
			}
		}
	}
	printf("\n");
}
void dfs(int x)
{
	if(C == Lim) return;
	if(x == N)
	{
		if(check())
		{
			Get();
		}
		return;
	}
	path[x] = 0;
	if (x != 0 && x != (N - 1))
	{
		dfs(x + 1);
	}
	path[x] = 1;
	for(int i = 2; i <= 10; i++) B[i] += P[x][i];
	dfs(x + 1);
	for(int i = 2; i <= 10; i++) B[i] -= P[x][i];
	path[x] = 0;
}
int main()
{
	freopen("output2.txt", "w", stdout);
	for(int j = 2; j <= 10; j++) P[0][j] = 1;
	for(int i = 1; i < N; i++)
	{
		for(int j = 2; j <= 10; j++) P[i][j] = P[i-1][j] * (long long) j;
	}
	printf("Case #1:\n");
	dfs(0);
}
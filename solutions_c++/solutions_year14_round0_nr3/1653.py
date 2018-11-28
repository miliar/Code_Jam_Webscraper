#include <stdio.h>
#include <vector>
int R, C, sol[50], found;
void PrintSolution()
{
	if(found)
		return;
	found = 1;
	for(int i = 0; i < R; i++)
	{
		for(int j = 0; j < sol[i]; j++)
			putchar('*');
		for(int j = sol[i]; j < C; j++)
			putchar(i == R - 1 && j == C - 1 ? 'c' : '.');
		putchar('\n');
	}
}
void MM(int M, int dep, int lastRow)
{
	if(M == 0)
	{
		PrintSolution();
		return;
	}
	if(dep == R - 2)
	{
		if(M % 2 == 0 && M / 2 <= lastRow && M / 2 != C - 1)
		{
			sol[dep] = sol[dep + 1] = M / 2;
			PrintSolution();
		}
		return;
	}
	for(int i = lastRow; i > 0; i--)
	{
		if(i == C - 1 || i > M)
			continue;
		sol[dep] = i;
		MM(M - i, dep + 1, i);
		sol[dep] = 0;
	}

}
int main()
{
	int T;
	int M;
	scanf("%d", &T);
	for(int caseNum = 1; caseNum <= T; caseNum++)
	{
		scanf("%d%d%d", &R, &C, &M);
		printf("Case #%d:\n", caseNum);
		for(int i = 0; i < R; i++)
			sol[i] = 0;
		found = 0;
		if(M == R * C - 1)
		{
			for(int i = 0; i < R - 1; i++)
				sol[i] = C;
			sol[R - 1] = C - 1;
			PrintSolution();
		}
		else
			MM(M, 0, C);
		if(!found)
			puts("Impossible");
	}
}
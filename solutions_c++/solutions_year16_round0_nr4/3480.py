#include<stdio.h>
#include<algorithm>
#include<string.h>
using namespace std;
int K, C, S;
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int T = 1; T <= t; T++)
	{
		scanf("%d%d%d", &K, &C, &S);
		printf("Case #%d: ", T);
		for (int i = 1; i <= S; i++)
		{
			printf("%d ", i);
		}
		puts("");
	}
}
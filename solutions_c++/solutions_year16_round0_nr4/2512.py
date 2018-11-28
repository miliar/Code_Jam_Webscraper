#include <algorithm>
#include <iostream>
#include <cstring>
#include <cstdlib>
#include <cstdio>
#include <cmath>
using namespace std;

int num_case, K, C, S;

int main()
{
	freopen("4.in", "r", stdin);
	freopen("4.out", "w", stdout);
	scanf("%d", &num_case);
	for (int icase = 1; icase <= num_case; icase++)
	{
		scanf("%d %d %d", &K, &C, &S);
		printf("Case #%d: ", icase);
		for (int i = 1; i < S; i++) printf("%d ", i);
		printf("%d\n", S);
	}
	return 0;
}

#include <bits/stdc++.h>

using namespace std;

typedef unsigned long long ull;

int main()
{
	int T;
	scanf("%d", &T);

	for(int tc=1; tc <= T; tc++)
	{
		int K,C,S;
		ull n;

		printf("Case #%d: ", tc);
		scanf("%d %d %d", &K, &C, &S);
		for(int i=1; i <= K; i++) // simple case, K = S
			printf("%d ", i);
		printf("\n");
	}

	return EXIT_SUCCESS;
}
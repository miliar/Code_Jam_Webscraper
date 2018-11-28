#include <iostream>
#include <stdio.h>

using namespace std;

int P[26];

int cmp(int* a, int* b)
{
	return P[*b] - P[*a];
}

typedef int(__cdecl* _PtFuncCompare)(void const*, void const*);

int main()
{
	int T;
	cin >> T;

	for (int t = 1; t <= T; t++)
	{
		int p[26];
		int N;
		cin >> N;
		int n = 0;
		for (int i = 0; i < N; i++)
		{
			cin >> P[i];
			n += P[i];
			p[i] = i;
		}

		printf("Case #%d: ", t);

		while (n > 0)
		{
			qsort(p, N, sizeof(int), (_PtFuncCompare)cmp);
			printf("%c", 'A' + p[0]);
			P[p[0]]--;
			n--;

			if (n == 2)
			{
				printf(" ");
				continue;
			}

			if (P[p[0]] < P[p[1]])
				swap(p[0], p[1]);

			printf("%c", 'A' + p[0]);
			P[p[0]]--;
			n--;

			printf(" ");
		}





		printf("\n");
	}

	return 0;
}

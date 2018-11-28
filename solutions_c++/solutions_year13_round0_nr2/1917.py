#include <iostream>
#include <cstdio>
#include <cstring>

using namespace std;

#define NM 105

int a[NM][NM], maxc[NM], maxr[NM];

int main()
{
	freopen ("tests.in", "r", stdin);
	freopen ("tests.out", "w", stdout);

	int T;
	scanf ("%d", &T);

	for (int t = 1; t <= T; ++t)
	{
		int N, M;

		scanf ("%d %d", &N, &M);
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				scanf ("%d", &a[i][j]);

		for (int i = 0; i < N; ++i)
		{
			maxr[i] = 0;
			for (int j = 0; j < M; ++j) maxr[i] = max(maxr[i], a[i][j]);
		}

		for (int j = 0; j < M; ++j)
		{
			maxc[j] = 0;
			for (int i = 0; i < N; ++i) maxc[j] = max(maxc[j], a[i][j]);			
		}

		int correct = 1;
		
		for (int i = 0; i < N; ++i)
			for (int j = 0; j < M; ++j)
				if (a[i][j] < maxr[i] && a[i][j] < maxc[j]) correct = 0;


		if (correct) printf ("Case #%d: YES\n", t);
		else printf ("Case #%d: NO\n", t);
	}

	return 0;
}

#include <stdio.h>
#include <iostream>
#include <vector>
#include <algorithm>


using namespace std;

int main()
{
	freopen("B.in", "r", stdin);
	freopen("B.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 0; t < T; t++)
	{
		int N;
		scanf("%d", &N);
		int mas[10];
		for (int i = 0; i < N; i++)
			scanf("%d", &mas[i]);
		int mm[10];
		for (int i = 0; i < N; i++)
			mm[i] = mas[i];
		sort(mm, mm+N);
		int k = 0;
		int res= 1000000000;
		do
		{
			k++;
			bool ok = true;
			int mx = mm[0];
			int mxIndex = 0;
			for (int i = 1;  i < N; i++)
				if (mm[i] > mx)
				{
					mx = mm[i];
					mxIndex = i;
				}
			for (int i = 0; i < mxIndex; i++)
				if (mm[i+1] < mm[i])
					ok = false;
			for (int i =  N - 1; i > mxIndex; i--)
				if (mm[i-1] < mm[i])
					ok = false;
			if (ok)
			{
				int r = 0;
				int indexes[10];
				for (int i = 0; i < N; i++)
				{
					for (int j = 0; j < N; j++)
						if (mm[j] == mas[i])
						{
							indexes[i] = j;
							break;
						}
				}
				for (int i = 0; i < N; i++)
					for (int j = 0; j < i; j++)
						if (indexes[j] > indexes[i])
							r++;
				if (r < res)
					res = r;
			}
		}while (next_permutation(mm, mm+N));
		printf("Case #%d: %d\n", t+1, res);
	}

	return 0;
}
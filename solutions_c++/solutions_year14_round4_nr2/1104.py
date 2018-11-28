#include <cstdio>
#include <cstring>
#include <algorithm>
#include <set>

using namespace std;

int N;
int A[1005], AA[1005];

void Work()
{
	scanf("%d", &N);
	for (int i = 0; i < N; i ++)
		scanf("%d", &A[i]);
	
	int Ans = 10000000;
	for (int m = 0; m < (1 << N); m ++)
	{
		for (int i = 0; i < N; i ++)
			if (m & (1 << i))
				AA[i] = 2100000000 - A[i];
			else
				AA[i] = A[i];
		int C = 0;
		for (int i = 0; i < N; i ++)
			for (int j = i + 1; j < N; j ++)
				if (AA[i] > AA[j])
					C ++;
		if (C < Ans)
			Ans = C;
	}
	printf("%d\n", Ans);
	fflush(stdout);
}

int main()
{
	freopen("B-small.in", "r", stdin);
	freopen("B-small.out", "w", stdout);
    int Cases;
    scanf("%d", &Cases);
    for (int Case = 1; Case <= Cases; Case ++)
    {
		printf("Case #%d: ", Case);
		Work();
    }
    return 0;
}
#include <stdio.h>
#include <vector>
long long int ans;
using namespace std;

void main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T,A,B,K;
	scanf("%d", &T);
	for (int ii = 0; ii < T; ii++)
	{
		scanf("%d%d%d", &A, &B, &K);
		ans = 0;
		if (A <= K && B <= K) ans = A*B;
		else{
			for (int i = 0; i < A; i++)
			{
				for (int j = 0; j < B; j++)
				{
					if ((i&j) < K) ans++;
				}
			}
		}
		printf("Case #%d: %d\n", ii + 1, ans);
	}
}
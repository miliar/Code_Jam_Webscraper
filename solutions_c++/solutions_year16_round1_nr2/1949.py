#include <iostream>
#include <cstdio>
#include<cstdlib>
#include<cstring>
#include<string>
#include<vector>
#include<algorithm>

using namespace std;
typedef long long ll;

int A[2501];
int main()
{
	freopen("in.txt", "r", stdin);
	freopen("out.txt", "w", stdout);
	int T,N,tmp;

	scanf("%d", &T);
	for (int tc = 1; tc <= T; ++tc)
	{
		for (int i = 0; i < 2501; ++i)
			A[i] = 0;
		scanf("%d", &N);
		for (int i = 0; i < (2 * N - 1); ++i)
		{
			for (int j = 0; j < N; ++j){
				scanf("%d", &tmp);
				A[tmp]++;
			}
		}
		
		printf("Case #%d: ", tc);
		for (int i = 0; i <= 2501; ++i)
		{
			if (A[i] & 1)
				printf("%d ", i);
		}
		printf("\n");
	}

	return 0;
}
#include<cstdio>
#include<ctime>
#include<cstdlib>
#include<cstring>
#include<climits>
#include<cctype>
#include<algorithm>
#include<vector>
#include<map>
int T, ans;
int A, B, K;
int main()
{
	scanf("%d", &T);
	for(int t = 1; t <= T; ++t)
	{
		ans =0;
		scanf("%d %d %d", &A, &B, &K);
		for(int i = 0; i < A; ++i)
		{
			for(int j = 0; j < B; ++j)
			{
				if((i & j) < K)
					ans++;
			}
		}
		printf("Case #%d: %d\n", t, ans);
	}
	return 0;
}
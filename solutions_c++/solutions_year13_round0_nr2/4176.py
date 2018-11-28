using namespace std;
#include<cstdio>
#include<cstring>
int A[107][107];
int up[107][107], down[107][107], left[107][107], right[107][107];
int main()
{
	freopen("file.in", "r", stdin);
	freopen("file.out", "w", stdout);
	int T, N, M, i, j;
	int test = 1;
	scanf("%d", &T);
	while(T--)
	{
		scanf("%d%d", &N, &M);
		memset(up, 0, sizeof(up));
		memset(down, 0, sizeof(up));
		memset(left, 0, sizeof(left));
		memset(right, 0, sizeof(right));
		for(i = 1; i <= N; ++i)
			for(j = 1; j <= M; ++j)
				scanf("%d", &A[i][j]);
		for(i = 1; i <= N; ++i)
		{
			for(j =1; j <= M; ++j)
			{
				if(A[i][j] > left[i][j-1])
					left[i][j] = A[i][j];
				else left[i][j] = left[i][j-1];
				if(A[i][j] > up[i-1][j])
					up[i][j] = A[i][j];
				else up[i][j] = up[i-1][j];
			}
		}
		for(i = N; i >= 1; --i)
			for(j = M; j >= 1; --j)
			{
				if(A[i][j] > right[i][j+1])
					right[i][j] = A[i][j];
				else right[i][j] = right[i][j+1];
				if(A[i][j] > down[i+1][j])
					down[i][j] = A[i][j];
				else down[i][j] = down[i+1][j];
			}
		int OK = true;
		for(i = 1; i <= N && OK == true; ++i)
			for(j = 1; j <= M && OK == true; ++j)
			{
				if( (A[i][j] < up[i][j] || A[i][j] < down[i][j]) && (A[i][j] < left[i][j] || A[i][j] < right[i][j]) )
					OK = false;
			}
		if(OK == true)
			printf("Case #%d: YES\n", test);
		else printf("Case #%d: NO\n", test);
		++test;
	}
	return 0;
}
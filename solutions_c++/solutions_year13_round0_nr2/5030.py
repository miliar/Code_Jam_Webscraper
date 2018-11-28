#include <stdio.h>

int T,N,M;

int table [101][101];
int up[101][101];
int down[101][101];
int left[101][101];
int right[101][101];

int main(int argc, char *argv())
{
	int i,j;
	bool flag = true;
	int value;
	scanf("%d", &T);
	for (int t=0;t<T;++t)
	{
		printf("Case #%d: ", t+1);
		scanf("%d %d", &N, &M);
		for (i=0;i<N;++i)
		{
			for (j=0;j<M;++j)
			{
				scanf("%d", &table[i][j]);
				up[i][j] = down[i][j] = left[i][j] = right[i][j] = table[i][j];
			}
		}
		for (i=1;i<N;++i)
			for (j=0;j<M;++j)
				if (up[i][j]<up[i-1][j])
					up[i][j] = up[i-1][j];
		for (i=N-2;i>=0;--i)
			for (j=0;j<M;++j)
				if (down[i][j]<down[i+1][j])
					down[i][j] = down[i+1][j];
		for (j=1;j<M;++j)
			for (i=0;i<N;++i)
				if (left[i][j]<left[i][j-1])
					left[i][j] = left[i][j-1];
		for (j=M-2;j>=0;--j)
			for (i=0;i<N;++i)
				if (right[i][j]<right[i][j+1])
					right[i][j] = right[i][j+1];
		flag = true;
		for (i=0;i<N;i++)
		{
			for (j=0;j<M;j++)
			{
				value = table[i][j];
				if ( (value<up[i][j] || value<down[i][j]) && (value<left[i][j] || value<right[i][j]))
				{
					flag = false;
					i=N;
					j=M;
				}
			}
		}
		if (flag)
			printf("YES\n");
		else
			printf("NO\n");
	}
	return 0;
}
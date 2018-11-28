#include <cstdio>

int field[100][100];
int pattern[100][100];

void init(int f[][100])
{
	for (int i = 0; i < 100; i++)
		for (int j = 0; j < 100; j++)
			f[i][j] = 100;
}

void mow(int N, int M)
{
	for (int i = 0; i < N; i++)
	{
		// find the highest point
		int height = -1;
		for (int j = 0; j < M; j++)
		{
			if (height < pattern[i][j])
				height = pattern[i][j];
		}
		// mow
		for (int j = 0; j < M; j++)
		{
			if (field[i][j] > height)
				field[i][j] = height;
		}
	}
	for (int i = 0; i < M; i++)
	{
		// find the highest point
		int height = -1;
		for (int j = 0; j < N; j++)
		{
			if (height < pattern[j][i])
				height = pattern[j][i];
		}
		// mow
		for (int j = 0; j < N; j++)
		{
			if (field[j][i] > height)
				field[j][i] = height;
		}
	}
}

bool check(int N, int M)
{
	for (int i = 0; i < N; i++)
		for (int j = 0; j < M; j++)
			if (field[i][j] != pattern[i][j])
				return false;
	return true;
}

int main(int argc, char *argv[])
{
	int T;
	int N;
	int M;
	scanf("%d", &T);
	for (int c = 1; c <= T; c++)
	{
		init(pattern);
		scanf("%d %d", &N, &M);
		for (int i = 0; i < N; i++)
			for (int j = 0; j < M; j++)
				scanf("%d", &(pattern[i][j]));
		init(field);
		mow(N, M);
		printf("Case #%d: %s\n", c, check(N, M) ? "YES" : "NO");
	}
	return 0;
}
#include <cstdio>
#include <cstring>
#include <queue>
using namespace std;
int D[1 << 11];
char A[20];
int N;
int End;
int flip(int x, int lim)
{
	int y = 0;
	for(int i = 0; i < N; i++)
	{
		bool bit = false;
		if (i <= lim) bit = ((x & (1 << (lim - i))) == 0);
		else bit = ((x & (1 << i)) > 0);
		if (bit) y += (1 << i);
	}
	return y;
}
int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int T;
	scanf("%d", &T);
	for(int t = 1; t <= T; t++)
	{
		scanf("%s", A);
		N = strlen(A);
		memset(D, 12, sizeof(D));
		D[(1 << N) - 1] = 0;
		End = 0;
		for(int i = 0; i < N; i++) End += (A[i] == '+' ? 1 : 0) * (1 << i);
		queue<int> que;
		que.push((1 << N) - 1);
		while(!que.empty())
		{
			int x = que.front();
			que.pop();
			if (x == End) break;
			for(int i = 0; i < N; i++)
			{
				int y = flip(x, i);
				if(D[y] > D[x] + 1)
				{
					D[y] = D[x] + 1;
					que.push(y);
				}
			}
		}
		printf("Case #%d: %d\n", t, D[End]);
	}
}
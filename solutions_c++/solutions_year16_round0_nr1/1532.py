#include <cstdio>
#include <cstring>
using namespace std;
int main(void)
{
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);
	int T, N, t = 1;
	bool seen[10];
	scanf("%d", &T);
	while (T--)
	{
		memset(seen, false, sizeof(bool) * 10);
		int N_;
		scanf("%d", &N);
		if (!N)
		{
			printf("Case #%d: INSOMNIA\n",t++);
			continue;
		}
		N_ = N;
		for (int i = 1;; N = N_*++i)
		{
			do
			{
				seen[N % 10] = true;
				N /= 10;
			} while (N != 0);
			bool all_seen = true;
			for (int i = 0; i < 10; i++)
				if (!seen[i])
				{
					all_seen = false;
					break;
				}
			if (all_seen)
			{
				printf("Case #%d: %d\n", t++, N_*i);
				break;
			}
		}
	}
}
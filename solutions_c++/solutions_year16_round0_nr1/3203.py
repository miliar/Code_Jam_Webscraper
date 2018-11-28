#include <cstdio>
#include <cstring>

#define ll long long

using namespace std;

const int M = 1000000;

void extract(ll n, int &cnt, bool *flag)
{
	while (n > 0)
	{
		int t = n % 10;
		n /= 10;
		if (!flag[t])
		{
			cnt++;
			flag[t] = 1;
		}
	}
}

int main()
{
	freopen("A-large.in", "r", stdin);
	freopen("A.out", "w", stdout);
	int T; 
	scanf("%d", &T);
	for (int _ = 1; _ <= T; _++)
	{
		int n; 
		scanf("%d", &n);
		printf("Case #%d: ", _);
		if (n == 0) {
			printf("INSOMNIA\n");
			continue;
		}
		bool flag[10];
		memset(flag, 0, sizeof(flag));
		int cnt = 0;
		for (int i = 1; i <= M; i++)
		{
			ll t = n * 1ll * i;
			extract(t, cnt, flag);
			if (cnt == 10)
			{
				printf("%I64d\n", t);
				break;
			}
		}
		if (cnt < 10)
		{
			printf("INSOMNIA\n");
		}
	}
    return 0;
}


#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

int n;
bool p[10];

void ins(int x)
{
	for (; x; x /= 10) p[x % 10] = 1;
}

bool check()
{
	for (int i = 0; i < 10; ++ i) if (!p[i]) return 0;
	return 1;
}

int main()
{
	//freopen("1.in", "r", stdin);
	//freopen("1.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++ t)
	{
		scanf("%d", &n);
		printf("Case #%d: ", t);
		if (!n) puts("INSOMNIA");
		else 
		{
			memset(p, 0, sizeof(p));
			int j;
			for (j = n; ; j += n) 
			{
				ins(j);
				if (check()) break;
			}
			printf("%d\n", j);
		}
	}
}
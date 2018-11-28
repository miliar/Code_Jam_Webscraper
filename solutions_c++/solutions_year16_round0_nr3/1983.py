#include <cstdio>
#include <cstdlib>
#include <ctime>
#include <cstring>
#include <cmath>
#include <algorithm>
#include <set>
#include <map>
#include <vector>

#define mp make_pair
#define pb push_back

using namespace std;

typedef long long ll;

const int inf = 0x3f3f3f3f;

int pri[11] = {2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31};
int a[101], b[101];
int n, k;

bool check()
{
	for (int i = 2; i <= 10; i ++)
	{
		b[i] = -1;
		for (int j = 0; j < 11; j ++)
		{
			int base = i, mod = pri[j];
			int sum = 0;
			for (int r = 1; r <= n; r ++)
				sum = (sum * base + a[r]) % mod;
			if (sum == 0)  { b[i] = mod; break; } 
		}
		if (b[i] == -1) return false;
	}
	return true;
}

int cnt = 0, tp = 0;
void dfs(int x)
{
	if (x == n + 1)
	{
		if (check())
		{
			++ cnt;
			for (int i = 1; i <= n; i ++)
				printf("%d", a[i]);
			for (int i = 2; i <= 10; i ++)
				printf(" %d", b[i]);
			printf("\n");
		}
		return ;
	}
	a[x] = 1;
	dfs(x + 1);
	if (cnt == k) return ;
	if (x != 1 && x != n)
	{
		a[x] = 0;
		dfs(x + 1);
		if (cnt == k) return ;
	}
}

void Work()
{
	scanf("%d %d", &n, &k);
	++ tp;
	printf("Case #%d:\n", tp);
	dfs(1);
}

int main( )
{
	int T;
	scanf("%d", &T);
	while (T --) Work();
	return 0;
}

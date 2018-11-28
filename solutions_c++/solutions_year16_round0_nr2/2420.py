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

int f[10001][2];
char str[1001];

int tp = 0;
// 0: - 1:+
void Work()
{
	scanf("%s", str + 1);
	++ tp;
	int n = (int )strlen(str + 1);
	for (int i = 1; i <= n; i ++)
	{
		f[i][0] = f[i][1] = inf;
		for (int j = i; j >= 1 && str[j] == '+'; j --)
		{
			f[i][0] = min(f[i][0], f[j - 1][1] + 1);
			f[i][1] = min(f[i][1], f[j - 1][1]);
		}
		for (int j = i; j >= 1 && str[j] == '-'; j --)
		{
			f[i][0] = min(f[i][0], f[j - 1][0]);
			f[i][1] = min(f[i][1], f[j - 1][0] + 1);
		}
	}
	printf("Case #%d: %d\n", tp, f[n][1]);
}

int main( )
{
	int T;
	scanf("%d", &T);
	while (T --)
		Work();
	return 0;
}

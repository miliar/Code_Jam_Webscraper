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

int tp = 0;
bool a[1001];
int n;

void Work()
{
	int ans = -1;
	++ tp;
	scanf("%d", &n);
	for (int i = 0; i < 10; i ++) a[i] = false;
	for (int i = 1; i <= 100; i ++)
	{
		int tmp = n * i;
		if (tmp == 0) a[tmp] = true;
		else
		{
			while (tmp) a[tmp % 10] = true, tmp /= 10;
		}
		int cnt = 0;
		for (int j = 0; j < 10; j ++)
			if (a[j]) ++ cnt;
		if (cnt == 10) { ans = n * i; break; }
	}
	printf("Case #%d: ", tp);
	if (ans == -1) printf("INSOMNIA\n");
	else printf("%d\n", ans);
}
	
	
int main( )
{
	int T;
	scanf("%d", &T);
	while (T --) Work();
	return 0;
}

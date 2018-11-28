#include <cstdio>
#include <cstring>

using namespace std;

bool ispal(int d)
{
	char tmp[30];
	sprintf(tmp, "%d", d);
	for(int i = 0, j = strlen(tmp) - 1; i < j; ++i, --j)
		if(tmp[i] != tmp[j])
			return false;
	return true;
}

void solve(int t)
{
	int a, b, ans = 0;
	scanf("%d%d", &a, &b);
	for(int i = 1; i * i <= b; ++i)
		ans += ispal(i) && ispal(i * i) && i * i >= a;
	printf("Case #%d: %d\n", t, ans);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for(int k = 1; k <= t; ++k)
		solve(k);
	return 0;
}
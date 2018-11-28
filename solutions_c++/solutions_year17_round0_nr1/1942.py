#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>
using namespace std;
int cake[1010];
char str[1010];

void solve(int casen)
{
	int k;
	memset(str, 0, sizeof(str));
	memset(cake, 0, sizeof(cake));
	scanf("%s %d", str, &k);
	int len = strlen(str);
	for (int i = 0; i < len; i++)
	{
		if (str[i] == '+') cake[i] = 1;
		else if (str[i] == '-')cake[i] = -1;
		else puts("ERROR");
	}
	int cnt = 0;
	for (int i = 0; i <= len - k; i++)
	{
		if (cake[i] == 1) continue;
		cnt++;
		for (int j = i; j < i + k; j++) cake[j] = -cake[j];
	}
	for (int i = 0; i < len; i++)
	{
		if (cake[i] == -1)
		{
			printf("Case #%d: IMPOSSIBLE\n", casen);
			return;
		}
	}
	printf("Case #%d: %d\n", casen, cnt);
}

int main()
{
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t; scanf("%d", &t);
	for (int i = 1; i <= t; i++) solve(i);
}
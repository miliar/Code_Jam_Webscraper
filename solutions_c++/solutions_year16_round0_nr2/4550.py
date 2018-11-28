#include <cstdio>
#include <algorithm>
#include <cstring>
using namespace std;

const int N = 200;
char s[N];

int main()
{
	//freopen("2.in", "r", stdin);
	//freopen("2.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++ t)
	{
		scanf(" %s", &s);
		int n = strlen(s);
		printf("Case #%d: ", t);
		int cnt = 1;
		for (int i = 1; i < n; ++ i) if (s[i] != s[i - 1]) ++ cnt;
		//if ((cnt & 1) && s[0] == '+' || !(cnt & 1) && s[0] == '-') -- cnt;
		if (s[n - 1] == '+') -- cnt;
		printf("%d\n", cnt);
	}
}
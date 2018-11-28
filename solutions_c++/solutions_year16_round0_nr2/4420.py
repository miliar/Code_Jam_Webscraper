#include <cstring>
#include <cstdio>
#include <algorithm>
using namespace std;

char s1[5100],ch;
int Cas,T,len,ans;

int main()
{
	//freopen("B.in", "r", stdin);
	//freopen("B.out", "w", stdout);

	scanf("%d", &T);

	for (int Cas = 1; Cas <= T; Cas ++)
	{
		printf("Case #%d: ", Cas);
		scanf("%s", s1);
		len = strlen(s1);
		ans = 0; ch = s1[0];
		for (int i = 1; i < len; i ++) if (ch != s1[i])
			ch = s1[i], ans ++;
		if (ch == '-') ans ++;
		printf("%d\n", ans);
	}

	return 0;
}

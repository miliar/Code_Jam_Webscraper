#include <cstdio>
#include <cstring>
#include <algorithm>
#define NN 1008

using namespace std;


int main()
{
	int t;
	freopen("A-large.in", "r", stdin);
	freopen("a-large.out", "w", stdout);
	scanf("%d", &t);
	for (int cas=1; cas<=t; cas++)
	{
		int n, i;
		char s[NN];
		scanf("%d%s", &n, s);
		int all = 0;
		int res = 0;
		for (i=0; s[i]; i++)
		{
			if (s[i]-'0' > 0) {
				if (all < i) {
					res += i-all;
					all = i;
				}
			}
			all += s[i]-'0';
		}
		printf("Case #%d: %d\n", cas, res);
	}
	return 0;
}


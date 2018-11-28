#include <cstring>
#include <algorithm>

using namespace std;

char s[1000];
int main()
{
	int ncase, i, j, tt = 0;
	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);
	scanf("%d", &ncase);
	while (ncase--)
	{
		scanf("%s", s);
		int len = strlen(s);
		s[len] = '+';
		s[len + 1] = '\0';
		int tot = 0;
		for (i = 0; i<len + 1;)
		{
			int j = i + 1;
			for (; j<len + 1; j++)
			if (s[i] != s[j])
				break;
			if (j == len + 1)
				break;
			i = j;
			tot++;
		}
		printf("Case #%d: %d\n", ++tt, tot);
	}
	return 0;
}

	

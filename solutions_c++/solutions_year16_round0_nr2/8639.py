#include <cstdio>
int main()
{
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; t++) {
		char s[101], last;
		int total = 0;
		scanf("%s", s);
		for (int i = 0; s[i]; i++) {
			last = s[i];
			if (i == 0 || s[i] != s[i - 1])
				total++;
		}
		
		if (last == '+')
			total--;
		printf("Case #%d: %d\n", t, total);
		
	}
	return 0;
}

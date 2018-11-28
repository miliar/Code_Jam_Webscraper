#include <cstdio>
#include <cstring>

#define LEN 200

int T, smax, num, standup;
char a[LEN];

int main()
{
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		memset(a, 0, LEN);
		num = 0, standup = 0;
		scanf("%d%s", &smax, a);
		for (int j = 0; j <= smax; j++) {
			if (a[j] > '0') {
				if (j <= standup)
					standup += a[j] - '0';
				else {
					num += (j - standup);
					standup += num;
					standup += a[j] - '0';
				}
			}
			
		}
		printf("Case #%d: %d\n",i+1, num );
		//printf("%d %s\n", smax, a);
	}
	return 0;
}
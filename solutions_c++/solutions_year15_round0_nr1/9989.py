#include <cstdio>
#include <cstring>

int
main()
{
	int T;
	scanf("%d", &T);
	char si[1024];
	int smax;
	for (int i=0; i<T; ++i) {
		bzero(si, sizeof(si));
		int sum = 0;
		int res = 0;
		scanf("%d %s", &smax, si);
		int j = 0;
		while (sum < smax) {
			while (si[j] == '0' && j < strlen(si)) ++j;
			if (sum < j) {
				res += (j - sum);
				sum += res;
			} else {
				sum += (si[j++] - '0');
			}
		}
		printf("Case #%d: %d\n", i+1, res);
	}
	return 0;
}
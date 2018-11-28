#include <stdio.h>
#define NMAX 1010

using namespace std;

int main()
{
	freopen("inputStandingOvation.in", "r", stdin);
	freopen("outputStandingOvation.out", "w", stdout);

	int T, Smax, S[NMAX], current, extra;
	char c;

	scanf("%d", &T);

	for (int count = 1; count <= T; ++count) {
		printf("Case #%d: ", count);

		current = 0, extra = 0;

		scanf("%d", &Smax);
		
		scanf("%c", &c);

		for (int i = 0; i <= Smax; ++i) {
			scanf("%c", &c);
			S[i] = int(c) - int('0');
			if (current < i) {
				extra += i - current;
				current = i;
			}
			current += S[i];
		}

		printf("%d\n", extra);
	}
}
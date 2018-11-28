/*
Then, after the flip, 
the stack is i, i-1, ..., 2, 1, i+1, i+2, ..., N.
Pancakes 1, 2, ..., i now have the opposite side up,
whereas pancakes i+1, i+2, ..., 
N have the same side up that they had up before.
*/

#include <stdio.h>
#include <string.h>

char str[103];

int main() {

	freopen("B-large.in", "r", stdin);
	freopen("B-large.out", "w", stdout);

	int t;
	scanf("%d", &t);

	int tc = 0;

	while (t--) {

		scanf("%s", str);

		int s = strlen(str);

		int c = 0;

		for (int i = s - 1; i >= 0; i--) {
			if (str[i] == '-') {
				c++;
				for (int j = i; j >= 0; j--) {
					if (str[j] == '+')str[j] = '-';
					else
						str[j] = '+';
				}
			}
		}

		printf("Case #%d: %d\n", ++tc, c);

	}

}
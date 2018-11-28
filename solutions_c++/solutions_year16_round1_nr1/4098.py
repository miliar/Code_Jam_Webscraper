#include <bits/stdc++.h>

int main() {
	short k;
	short c;
	
	scanf("%hi", &k);
	c = k;
	
	while (k--) {
		char S[1001] = "";
		char last[1001] = "";

		scanf("%s", S);

		for (short i = 0; i < strlen(S); i++) {
			char a[1001] = "";
			char b[1001] = "";

			strcpy(a, last);
			a[strlen(a)] = S[i];
			b[0] = S[i];
			strcat(b, last);

			if (strcmp(a, b) > 0)
				strcpy(last, a);
			else
				strcpy(last, b);
		}

		printf("Case #%hi: %s\n", c-k, last);
	}
	
	return 0;
}

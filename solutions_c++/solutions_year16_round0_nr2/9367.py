#include <bits/stdc++.h>

int main() {
	short k;
	short c;
	
	scanf("%hi", &k);
	c = k;
	
	while (k--) {
		char s[101];
		short flips = 0;
		bool end = false;

		scanf("%s", s);

		while (!end) {
			char top = s[0];

			end = true;
			for (short i = 0; i < strlen(s) && end; i++)
				if (s[i] == '-')
					end = false;
			if (end)
				break;

			if (top == '+')
				top = '-';
			else
				top = '+';

			for (short i = 0; i < strlen(s) && top != s[i]; i++)
				s[i] = top;

			flips++;
		}
		
		printf("Case #%hi: %hi\n", c-k, flips);
	}
	
	return 0;
}

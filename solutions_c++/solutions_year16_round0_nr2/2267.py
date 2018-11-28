#include <iostream>
#include <cstdio>

int main() {
	int T;
	char str[101];
	scanf("%d", &T);
	for (int i = 0; i < T; i++) {
		scanf("%s", str);
		int l = strlen(str);
		int count = 0;
		
		while (l > 0 && str[l - 1] == '+') l--;

		for (int j = 0; j < l;) {
			count++;
			if(str[j] == '+') {
				while (j < l && str[j] == '+') j++;
			} else {
				while (j < l && str[j] == '-') j++;
			}
		}
		printf("Case #%d: %d\n", i + 1, count);
	}
}
#include <cstdio>
#include <cstring>

int main() {
	int T;
	char str[110];
	int cnt;
	
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		scanf("%s", str);
		
		char c = 0;
		cnt = 0;
		
		for (int j = 0; str[j] != 0; j++) {
			if (str[j] != c) {
				cnt++;
				c = str[j];
			}
		}
		
		if (c == '+') {
			cnt--;
		}
		
		printf("Case #%d: %d\n", i, cnt);
	}
	
	return 0;
}
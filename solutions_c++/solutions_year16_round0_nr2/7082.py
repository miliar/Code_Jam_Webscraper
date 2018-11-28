#include <cstdio>
#include <cstring>

#define TEST_PRINT_INPUT 0

int main() {
	int t;
	int ret = scanf("%d", &t);
	char *get;
#if TEST_PRINT_INPUT
	printf("T   = %d\n", t);
#endif
	
	for (int i = 0; i < t; i++) {
		int count = 0;
		bool plus = false;
		get = new char[128];
		ret = scanf("%s", get);
#if TEST_PRINT_INPUT
		printf("GET  = %s\n", get);
#endif		
		int len = strlen(get);
		for (int j = 0; j < len; j++) {
			if (j == 0) {
				plus = get[j] == '+';
				if (len == 1) {
					count = plus ? count : count + 1;
				}
			} else if (j == len - 1) {
				if (get[j] == '+') {
					if (!plus) {
						count++;
					}
				} else {
					if (!plus) {
						count++;
					} else {
						count+=2;
					}
				}
			}else {
				if (get[j] == '+') {
					if (!plus) {
						count++;
						plus = true;
					} 
				} else {
					if (plus) {
						count++;
						plus = false;
					}
				}
			}
		}	
		printf("Case #%d: %d\n", (i + 1), count);
		delete[] get;
	}
	return 1;
}
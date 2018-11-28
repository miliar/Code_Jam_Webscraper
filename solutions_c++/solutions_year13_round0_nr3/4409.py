#include <stdio.h>
#include <string.h>
#include <math.h>
#include <float.h>

#define MAX_STR		200

int main(int argc, char *argv[]) {
	int max_tc, tc = 1;
	long long count;
	char strA[MAX_STR], strB[MAX_STR];
	long long A, B;

	scanf("%d", &max_tc);
	while(max_tc--) {
		// init
		count = 0;
		A = 1;
		B = 1;
		scanf("%s %s", strA, strB);

		if (strlen(strB) >= LDBL_DIG) {
			goto print_case;
		}

		sscanf(strA, "%lld", &A);
		sscanf(strB, "%lld", &B);

		long double sqrtA, sqrtB;
		sqrtA = sqrt((long double)A);
		sqrtB = sqrt((long double)B);

		char tmp_str[MAX_STR];
		bool result = true;
		for(long long i = (long long)sqrtA; i*i <= B; i++) {
			if(i*i < A)
				continue;

			// check if i and i*i are palindrome.
			sprintf(tmp_str, "%lld", i);
			int len = strlen(tmp_str);
			result = true;
			if (len > 1) {
				for(int j = 0; j <= len/2; j++) {
					if(tmp_str[j] != tmp_str[len-1-j]) {
						result = false;
						break;
					}
				}
			}

			if (result) {
				sprintf(tmp_str, "%lld", i*i);
				len = strlen(tmp_str);
				if (len > 1) {
					for(int j = 0; j <= len/2+1; j++) {
						if(tmp_str[j] != tmp_str[len-1-j]) {
							result = false;
							break;
						}
					}
				}
			}

			if (result) {
				//printf("%lld %lld\n", i, i*i);
				count++;
			}
		}

print_case:
		printf("Case #%d: %lld\n", tc++, count);
	}

	return 0;
}

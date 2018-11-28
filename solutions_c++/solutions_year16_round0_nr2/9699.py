#include <stdio.h>
#include <string.h>

int str[101];
char input[101];

int main () {

	int T;

	scanf("%d", &T);

	for(int i = 1; i <= T; i++) {

		scanf("%s", &input);

		int last = strlen(input);

		for(int j = 0; j < last; j++) {
			if(input[j] == '+')
				str[j] = 1;
			else
				str[j] = 0;
		}

		--last;

		int count = 0;
		while(last > -1) {

			if(str[last] == 1) --last;
			else {
				if(str[0] == 0) {
					int finish = last/2;
					for(int j = 0, k = last; j <= finish; j++, k--) {
						int t = str[j];
						int t1 = str[k];
						str[j] = t1^1;
						str[k] = t^1;
					}
					count++;
				}
				else {
					for(int j = 0; str[j] == 1; j++) {
						str[j] = str[j]^1;
					}

					count++;
				}
			}
		}


		printf("Case #%d: %d\n", i, count);
	}
	
	return 0;
}
#include <stdio.h>
#include <string.h>


int main()
{
	int T;
	scanf("%d", &T);

	for (int w = 0; w < T; w++) {
		char in[101];
		scanf("%s", in);

		bool mode = true;
		int res = 0;
		for(int i = strlen(in) - 1; i >= 0; i--) {
			if (mode && in[i] == '+')
				continue;
			else if (!mode && in[i] == '-')
				continue;
			else if (mode && in[i] == '-') {
				mode = false;
				res++;
			}
			else {
				mode = true;
				res++;
			}
		}

		printf("Case #%d: %d\n", w+1, res);
	}

	return 0;
}
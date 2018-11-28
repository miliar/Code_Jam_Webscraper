#include <stdio.h>
int main(void){
	int t, a, b, c, count;
	scanf("%d", &t);
	for (int i = 0; i < t; i++){
		count = 0;
		scanf("%d%d%d", &a, &b, &c);
		for (int j = 0; j < a; j++)
			for (int k = 0; k < b; k++)
				if ((j & k) < c)
					count++;
		printf("Case #%d: %d\n", i + 1, count);
	}
	return 0;
}

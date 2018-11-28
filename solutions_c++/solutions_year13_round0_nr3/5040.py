#include<cstdio>

int main() 
{
	int x[] = {1, 4, 9, 121, 484};
        int t, a, b, i, j, count;
	scanf("%d", &t);

	for(i = 1; i <= t; i++) {
		scanf("%d %d", &a, &b);

		count = 0;
		for(j = 0; j < 5; j++) {
			if(x[j] >= a && x[j] <= b) {
				count ++;
			}
		}

		printf("Case #%d: %d\n", i, count);
	}

	return 0;
}

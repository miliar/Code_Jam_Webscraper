#include<stdio.h>

void testCase() {
	int a,b,k;
	int sum = 0;
	scanf("%d%d%d", &a, &b, &k);
	for(int i=0; i<a; i++) {
		for(int j=0; j<b; j++) {
			if((i&j) < k) sum++;
		}
	}
	printf("%d\n", sum);
}

int main()
{
	int testCases;
	scanf("%d", &testCases);

	for(int i=0; i<testCases; i++) {
		printf("Case #%d: ", i+1);
		fprintf(stderr, "Case #%d: ", i+1);
		testCase();
	}
	return 0;
}
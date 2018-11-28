#include <stdio.h>
#include <math.h>

int isFair(int input);

int main()
{
	int testCase;
	scanf("%d", &testCase);
	for (int t=1;t<=testCase;t++) {
		int A, B, count;
		count = 0;
		scanf("%d %d", &A, &B);
		for (int input=A;input<=B;input++) {
			double square = sqrt(input);
			if (square == (int)square) {
				if (isFair(input) && isFair((int)square)) {
					//printf("%d\n", input);
					count++;
				}
			}
		}
		printf("Case #%d: %d\n", t, count);
	}
	return 0;
}

int isFair(int input)
{
	int string[100];
	int count=0;
	while(input>=10) {
		string[count++] = input%10;
		input /= 10;
	}
	string[count] = input;
	for (int i=0;i<=count/2;i++) {
		if (string[i]!=string[count-i]) {
			return 0;
		}
	}
	return 1;
}

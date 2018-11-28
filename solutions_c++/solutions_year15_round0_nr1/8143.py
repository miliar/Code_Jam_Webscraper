#include <iostream>
#include <stdio.h>
#include <stdlib.h>

using namespace std;

int main()
{
	FILE* fp = fopen("resa.txt", "w");
	if (fp == 0)
		return -1;
	int T;
	scanf("%d", &T);
	for (int i = 1; i <= T; i++) {
		char s[1001];
		int sm = 0;
		scanf("%d %s", &sm, s);
		int f = 0;
		int sum = 0;
		for (int j = 0; s[j]; j++) {
			sum += s[j] - '0';
			sum -= 1;
			if (sum < 0 && -sum > f)
				f = -sum;
		}
		fprintf(fp, "Case #%d: %d\n", i, f);
		printf("Case #%d: %d\n", i, f);
	}
	fclose(fp);
	//system("pause");
    return 0;
}

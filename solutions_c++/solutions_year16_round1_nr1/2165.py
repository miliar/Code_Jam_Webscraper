#include <iostream>
#include <stdio.h>
#include <string.h>
using namespace std;

int main() {
	int t;
	scanf("%d\n", &t);
	
	for (int i = 1; i <= t; i++) {
		printf("Case #%d: ", i);
		char inStr[1001];
		scanf("%s\n", inStr);
		int n = strlen(inStr);
		char outStr[1001];
		outStr[0] = inStr[0];
		outStr[n] = inStr[n];
		for (int j = 1; j < n; j++) {
			if (inStr[j] >= outStr[0]) {
				for (int k = j; k >= 1; k--) {
					outStr[k] = outStr[k-1];
				}
				outStr[0] = inStr[j];
			} else {
				outStr[j] = inStr[j];
			}
		}
		printf("%s\n", outStr);
	}
	
	return 0;
}
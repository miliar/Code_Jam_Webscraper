#include <stdio.h>
#include <stdlib.h>
using namespace std;

int main() {
	int testn, temp;
	long long int counted, result;
	scanf("%d",&testn);
	for (int i = 0; i < testn; ++i) {
		scanf("%d", &temp);
		char *input = (char*)calloc(temp+1, sizeof(char));
		scanf("%s", input);
		counted = result = 0;
		for (int k = 0; k <= temp; k++) {
			if (k > counted) {
				result += k - counted;
				counted += k - counted;
			}
			counted += ((int)input[k]-48);
		}
		printf("Case #%d: %lld\n", i+1, result);
		//free(input);
		//input = NULL;
	}
	return 0;
}

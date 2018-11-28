#include <stdio.h>
#include <string.h>

void run_test(int test){
	int levels[100];
	memset(levels, 0, 100*sizeof(int));
	int max_shyness = 0;
	scanf("%d ", &max_shyness);
	for(int n = 0; n <= max_shyness; ++n)
		levels[n] = getchar() - '0';
	int friends = 0, standing = 0;
	for(int n = 0; n <= max_shyness; ++n){
		if(standing+friends < n)
			friends += n - (standing+friends);
		standing += levels[n];
	}
	printf("Case #%d: %d\n", test, friends);
}

int main(){
	int tests;
	scanf("%d", &tests);
	for(int n = 0; n < tests; ++n)
		run_test(n+1);
}

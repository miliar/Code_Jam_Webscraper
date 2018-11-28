#include <stdio.h>

int K, C, S;


int main(void){

	int testcase;
	scanf("%d", &testcase);

	for(int t_itr=1; t_itr<=testcase; t_itr++){
		printf("Case #%d: ", t_itr);
		scanf("%d %d %d", &K, &C, &S);
		
		for(int i=1; i<=K; i++){
			printf("%d ", i);
		}
		printf("\n");

	}

	return 0;
}
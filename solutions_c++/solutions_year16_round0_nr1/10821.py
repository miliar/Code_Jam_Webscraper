#include <stdio.h>
#include <iostream>

using namespace std;

int main(void){
	freopen("A-large.in", "rt", stdin);
	freopen("A-large.out", "wt", stdout);
	
	int T, N, bitmap, counter, iteration;
	scanf("%d\n", &T);
	for(int i=0; i<T; i++){
		printf("Case #%d: ", i+1);
		scanf("%d\n", &N);
		bitmap = 0;
		counter = 0;
		if( N != 0){
			while( bitmap != 1023){	
				counter = counter + 1;
				iteration = counter * N;
				do{
					int digit = iteration %10;
					bitmap |= 1 << digit;
					iteration /= 10;
				} while(iteration>0);
			}
			printf("%d\n", counter * N);
		}else{
			printf("%s\n", "INSOMNIA");
		}
	}
	return 0;
}

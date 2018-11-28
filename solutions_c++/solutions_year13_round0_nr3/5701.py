#include <stdio.h>
#include <stdlib.h>
#include <string.h>


bool p(long long in){
	int i;
	char array[100];
	sprintf(array, "%lld", in);
	int len = strlen(array);
	int mid = len / 2;
	int is_p = 0;


	for(i=0; i<mid; i++){
		if(array[i]!=array[len-1-i]){
			return false; //// taught by SmartStringAlpha!
		}
	}

	return true;
}


int main(void){

	int num; 
	long long start, end, n; //for overflowing!!! (int: 2*10^9 length)
	int i, j;
	int p_array[2000];
	int p_num;
	int COUNT;

	scanf("%d", &num);
	p_num = 0;

	//find all fair-and-square
	for(n=1; n<=10000000; n++){
		//palindromes
		if(p(n))	
			if(p(n*n)){
				p_array[p_num] = n*n;
				p_num += 1;

				//printf("%lld\n", n*n);
			}
	}
	

	for(i=0; i<num; i++){
		COUNT = 0;
		scanf("%lld", &start);
		scanf("%lld", &end);
		for(j=0; j<p_num; j++){
			if( (p_array[j] <= end) && (p_array[j] >= start))
				COUNT +=1;
		}

		printf("Case #%d: %d\n", i+1, COUNT);

	}

	return 0;

}

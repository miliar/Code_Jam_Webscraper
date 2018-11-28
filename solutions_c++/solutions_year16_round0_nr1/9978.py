#include <stdio.h>
#include <stdlib.h>
#include <vector>

using namespace std;


void getDigits(int number, vector<bool> &numbers, int &count){
	
	while(number>0){
		int n = number%10;
		
		if(!numbers[n]){
			numbers[n] = true;
			count++;
		}
	
		number/=10;
	}
}

int main(int argc, char **argv){

	int T;
	scanf("%d", &T);
	
	for(int t=1; t<=T; t++){
	
		int N;
		int count = 0;
		vector<bool> numbers(10, false);
		
		scanf("%d", &N);
		
		if(N == 0)
			printf("Case #%d: INSOMNIA\n", t);		
		else{
			int i=0;
			while(count<10){
				i++;
				getDigits(i*N, numbers, count);
			}
			printf("Case #%d: %d\n", t, i*N);
		}	
	}

	return 0;
}

#include <stdio.h>
#include <string.h>
#include <math.h>


bool isPalindrome(long long  num){
	char txt[1024];
	sprintf(txt, "%lld", num);
	int length = strlen(txt);
	for(int i = 0, j = (length - 1); i <= j; i++, j--){
		if(txt[i] != txt[j]){
			return false;
		}
	}
	return true;
}

void main(){
	int T;
	scanf("%d", &T);
	for(int cases = 1; cases <= T; cases++){
		long long A = 0;
		long long B = 0;
		scanf("%lld %lld", &A, &B);

		int count = 0;
		double _A = (double)A;
		double _B = (double)B;
		for(long long i = ceil(sqrt(_A)); i <= floor(sqrt(_B)); i++){
			char txt[1024];
			sprintf(txt, "%lld", i);
			if(isPalindrome(i)){
				if(isPalindrome(i*i)){
					count++;
				}
			}
		}
		printf("Case #%d: %lld\n", cases, count);
	}
}
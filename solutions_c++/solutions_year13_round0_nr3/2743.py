#include <iostream>
#include <cstdio>
#include <vector>
#include <cmath>

using namespace std;

int countDigits(int value){
	if(value == 0)return 1;
	else return log10(value)+1;
}

int getDigit(int val, int i){ //i is offset from end of number
	val /= pow(10, i);
	val %= 10;
	return val;
}

bool isPalindrome(const int value){
	const int digits = countDigits(value);
	int forwards = 0;
	int backwards = digits-1;
	while (forwards<backwards){
		if(getDigit(value, forwards) != getDigit(value, backwards)){
			return false;
		}
		forwards++;
		backwards--;
	}
	return true;
}

bool isSquare(int value){
	float trash;
	return modf(sqrt(value), &trash) == 0;
}

int getNumberOfFairAndSquare(int lowerLimit, int upperLimit){
	const int lowerBaseLimit = ceil(sqrt(lowerLimit));
	int sum = 0;
	for(int i = lowerBaseLimit; i*i<=upperLimit; i++){
		if(isPalindrome(i)){
			if(isPalindrome(i*i)){
				sum++;
			}
		}
	}
	return sum;
}

int main(){
	int T;
	scanf("%d", &T);
	for(int t=0; t<T; t++){
		int a, b;
		scanf("%d %d", &a, &b);
		
		printf("Case #%d: %d\n", t+1, getNumberOfFairAndSquare(a, b));
	}
}

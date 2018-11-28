#include <iostream>
#include <cstdio>
#include <climits>
#include <vector>
using namespace std;

vector<bool> digits(10);

void countDigits(long long X){
	do{
		digits[X%10] = true;
		X/=10;
	}while(X);
}

bool foundAllDigits(){
	for(int i =0 ; i < 10; ++i){
		if(!digits[i])
			return false;
	}
	return true;
}

int main(){
	int T;
	cin >> T;
	for(int i = 0; i < T ; ++i){
		int n;
		cin >> n;
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", i+1);
			continue;
		}
		fill(digits.begin(), digits.end(), false);
		for(unsigned long long k = n; k <= 5000 * k; k += n){
			countDigits(k);
			if(foundAllDigits()){
				printf("Case #%d: %lld\n",(i+1), k);
				break;
			}
		}
	}

}


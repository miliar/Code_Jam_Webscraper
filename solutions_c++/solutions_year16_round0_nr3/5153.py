#include <iostream>
#include <string>
#include <cstring>
#include <sstream>
#include <vector>
#include <stdio.h>
#include <stdlib.h>

using namespace std;
#define max (10000000L)
bool prime[max];
int**divs;
vector<long> primes(max, 0);
int pSize = 0;

int count;
int numOfAns;
int* temp;
int* ansNum;
int currSize;


void find_N_CoinJam(int level);
long int BaseK_To_Base10(int* arr, int length, int k);
long int findFactor(long n);
bool isPrime(long n);
int arrToBinary(int*  arr, int length);

int main(int argc, char const *argv[]) {
	for(long int i = 2; i < max; ++i)
		prime[i] = true;

	for(long int i = 2, m=0; i < max-1; ) {
		//mark all multiples
		for(long int j = 2; (j*i) < max-1; ++j) {
			prime[i*j] = false;
		}
		//find next prime
		for(long int k = i+1; k <= max-1; k++) {
			if(prime[k]){
				i=k;
				primes[pSize++] = i;

				break;
			}
		}
	}
	

	int numTests, currNum;
	cin >> numTests;

	
	for(int i = 1; i <= numTests; ++i){	
		cin >> currSize >> numOfAns;
		ansNum = new int[numOfAns];
	
		count = 0;
		temp = new int[currSize];
		temp[0] = 1;
		temp[currSize-1] = 1;
		int count = 0;
		
		find_N_CoinJam(1);
		

		cout << "Case #" << i << ":\n";
		for(int k = 0; k < numOfAns; ++k){
			//cout << " " << finalNumber[k];
			for (int j = currSize-1; j >= 0; j--){
    			std::cout << ((ansNum[k] >> j) & 1);
    			temp[j] = (ansNum[k] >> j) & 1;
    		}
    		//cout<<endl;
			for(int j = 2; j <= 10; ++j){
				//cout << " " << BaseK_To_Base10(temp, currSize, j) << ":";
				cout << " " << findFactor(BaseK_To_Base10(temp, currSize, j));
			}
			cout << "\n";
		}
	}
	return 0;
}

void find_N_CoinJam(int level){
	if(numOfAns == count)
		return;
	else if(level == currSize-1){
		//cout <<"Reached level "<< level <<endl;
		bool isCoin = true;

		for(int i = 2; i <= 10; ++i){
			isCoin &= !isPrime(BaseK_To_Base10(temp, currSize, i));
		}

		if(isCoin){
			int tempNum =  arrToBinary(temp, currSize);
			ansNum[count++] = tempNum;
		}

	} else{
		//cout << "change bit :" << level <<endl;
		temp[level] = 0;
		find_N_CoinJam(level+1);
		temp[level] = 1;
		find_N_CoinJam(level+1);
	}
}

long int BaseK_To_Base10(int* arr, int length, int k){
	long int sum = 0;
	for(int i = length-1; i>= 0; --i){
		sum = sum*k + arr[i];
	}
	return sum;
}

long findFactor(long n){
	//cout << "finding factors of " << n << endl;
	for(long i = 0; i < max; ++i){
		if(n%primes[i] == 0)
			return primes[i];
	}
	return 1;

}

bool isPrime(long n){
	for(long i = 0; i < n && i < pSize;++i)

		if(n%primes[i] == 0)
			return false;

	return true;
}

int arrToBinary(int*  arr, int length){
	int sum = 0;
	for(int i = length-1; i >= 0; --i){
		sum |= (arr[i]<<(i));
		//cout << arr[i];
	}
	//cout << ":"<< sum << endl;
	return sum;
}
#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <string.h>

#define ARR_SIZE 600000
using namespace std;

vector<long long> prime(1,2);
long long divisor_arr[9] = {0};

long long isPrime(long long num){
	int i = 0;
	long long divisor = 0;
	while(prime[i] * prime[i] <= num){
		if(num % prime[i] == 0){
			divisor = prime[i];
			return divisor;
		}
		i++;
        if(i == 599999)
            break;
	}
    /*
    if(i == 599999){
        long long keep = prime[i];
        while(keep * keep <= num){
            if(num % keep == 0)
                return keep;
            keep++;
        }
    }*/
	return divisor;
}

void gen_prime(){
    int count = 1;
    int num = 3;
    while(count < ARR_SIZE){
        if(isPrime(num) == 0){
            prime.push_back(num);
            count++;
        }
        num++;
    }
}

bool isJamCoin(int* arr, int N){
	long long num, base, tmp;
    for(int i = 0; i < 9; i++){
        divisor_arr[i] = 0;
    }
	for(int i = 2; i <= 10; i++){
		num = 0;
		base = 1;
		for(int j = N - 1; j >= 0; j--){
			if(arr[j] == 1)
				num += base;
			base *= i;
		}
		tmp = isPrime(num);
		if(tmp == 0){
			return false;
		}else{
			divisor_arr[i-2] = tmp;
		}
	}
	return true;
}

void arr_increase(int* arr, int size){
	int carry = 1, tmp;
	for(int i = size - 2; i > 0; i--){
		if(carry == 0)
			break;
		tmp = arr[i] + carry;
		arr[i] = tmp % 2; 
		carry = tmp / 2;
	}
}
int main() {
    gen_prime();
    int T;
    cin >> T;
    for(int T_i = 0; T_i < T; T_i++){
    	int N, J;
    	cin >> N >> J;
    	int count = 0;
    	int jamcoin[N] = {0};
    	jamcoin[0] = jamcoin[N-1] = 1;
    	cout << "Case #" << T_i + 1 << ":" << endl;
    	while(count < J){
    		if(isJamCoin(jamcoin, N)){
    			count++;   			
    			for(int i = 0; i < N; i++)
    				cout << jamcoin[i];
    			for(int i = 0; i < 9; i++)
    				cout << " " << divisor_arr[i];
    			cout << endl;
    		}
    		arr_increase(jamcoin, N);
    	}
    }
    return 0;
}

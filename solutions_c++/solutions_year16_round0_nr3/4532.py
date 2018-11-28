#include <iostream>
#include <stdlib.h>
#include <math.h>

using namespace std;
int numPrimes;

long long *sieveOfEratothenes(int maxval){
	bool *primes = new bool[maxval + 1];
	int i,j;
	for(i = 2 ; i <= maxval ; i++)
		primes[i] = true;
	numPrimes = 0;
	for(int i = 2 ; i < maxval ; i++){
		if(!primes[i])
			continue;
		numPrimes++;
		for(j = 2 * i ; j < maxval ; j = j + i)
			primes[j] = false;
	}
	
	long long *primeNums = new long long[numPrimes];
	int temp = 0;
	for(i = 2 ; i <= maxval ; i++)
		if(primes[i])
			primeNums[temp++] = i;
	delete[] primes;
	return primeNums;		
}	

int checkPrime(long long num, long long *primes){
	int i,j;
	long long limit = sqrt(num);
	//cout<<max(limit, (long long)pow(10, 8))<<"h\t";
	for(i = 0 ; i < numPrimes ; i++){
		if(num % primes[i] == 0)
			return primes[i];
		if(primes[i] > limit)
				break;
	}
	return -1;
}

int main(){
	int i,j,k,l;
	int T, N, J;
	cin>>T;
	long long *primes = sieveOfEratothenes(pow(10, 8));
	for(l = 0 ; l < T ; l++){
		cin>>N>>J;
		cout<<"Case #"<<l + 1<<":\n";
		int count = 0;
		for(i = 0 ; i < pow(2, N - 2) ; i++){
			int *digits = new int[N];
			digits[0] = 1;
			digits[N-1] = 1;
			//cout<<i<<"\t";
			int n = 1;
			for(j = 0 ; j < N - 2 ; j++){
				if(i & n){
					digits[j+1] = 1;
					//cout<<1;
				}
				else{
					digits[j+1] = 0;
					//cout<<0;
				}
				n = n*2;
			}
			//cout<<"\n";
			int *divisors = new int[11];
			for(j = 2 ; j <= 10 ; j++)
			{
				long long num = 0;
				for(k = 0 ; k < N ; k++)
					num = num + (long long)digits[k] * (long long)pow(j, k);
				//cout<<num<<"\t";
				divisors[j] = checkPrime(num, primes);
				if(divisors[j] == -1)
					break;
			}
			//cout<<"\n";
			if(j == 11)
			{
				count++;
				for(k = N - 1 ; k >= 0 ; k--)
					cout<<digits[k];
				for(k = 2 ; k <= 10 ; k++)
					cout<<" "<<divisors[k];
				cout<<"\n";
				delete[] divisors;
				delete[] digits;

				if(count == J)
					break;
			}
			else{	
				delete[] divisors;
				delete[] digits;
			}
		} 
	}
	delete[] primes;
}

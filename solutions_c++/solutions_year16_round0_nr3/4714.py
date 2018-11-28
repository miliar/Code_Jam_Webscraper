
#include <stdio.h>
#include <iostream>
#include <stdlib.h>
#include <math.h>
#include <algorithm>

#define SIZE 16381
using namespace std;

unsigned long long isPrime( unsigned long long x) {
	for(unsigned long long i = 2; i < x ; i++) {
		if(x%i == 0) {
			return i;
		}
	}
	return 1;
}

int ProcessInput();

int main()
{

	int testcases, i;

	cin >> testcases;

	for(i=0; i < testcases; i++) {
		cout<<"Case #"<<i + 1<<": ";
		cout<<endl;
		ProcessInput();
	}

return 0;
}

 
int ProcessInput()
{
int N, J, i, k, m, count;
int *jamcoin;
unsigned long long **NumArray, **FactorArray;
unsigned long *isJamCoin;
int nComb;

cin >> N; 
cin >> J;

jamcoin = new int[N];
nComb = 1 << (N-2);
NumArray = new unsigned long long*[nComb];
FactorArray = new unsigned long long*[nComb];

for(i=0; i<nComb; i++){
	NumArray[i] = new unsigned long long[9];
	FactorArray[i] = new unsigned long long[9];
}
	
isJamCoin = new unsigned long[nComb];

// First and last digits of jamcoin is 1 and N > 2
jamcoin[N-1] = 1;
jamcoin[0] = 1;
// Find all possible combinations
for(i = 0; i < nComb ; i ++) {
	// Assume none of them are jamcoins
	isJamCoin[i] = 0;
	// Start with MSB which is 1
	for(m=2; m <= 10; m++) { 
		NumArray[i][m-2] = 1;
		// Factor array is initialized to all 1 at the end of loop
		FactorArray[i][m-2] = 1;
	}
	// Add remaining bit unit LSB
	for(k= N-2; k > 0 ; k --) {
		jamcoin[k] = (i >>(k-1)) & 0x1;
		for(m=2; m <= 10; m++)
			NumArray[i][m -2] = NumArray[i][m-2]*m + jamcoin[k];
	}
	// Add LSB which is also 1
	for(m=2; m <=10; m++)
		NumArray[i][m-2] = NumArray[i][m-2]*m + 1;
} 

count = 0;
// keep finding factors until we find J jamcoins
unsigned long long prime_num = 2;
int sum_factor_array;
while(1) {
	for(i=0; i < nComb; i++) {
		if(isJamCoin[i] ==1)
			continue;
		for(m=2; m <=10; m++) {
			if(prime_num >= NumArray[i][m-2]) 
				continue;
			if(FactorArray[i][m-2] == 1) { // We haven't found a factor yet 
				if(NumArray[i][m-2]%prime_num == 0)  
					FactorArray[i][m-2] = prime_num;	
			}
		}
		// check if we have found a jamcoin
		sum_factor_array = 0;
		for(m=2; m<=10; m++)
			if(FactorArray[i][m-2] >1)
				sum_factor_array ++;
		if(sum_factor_array == 9) {
			isJamCoin[i] = 1;
			cout<<"1"; // print the MSB
			for(k=N-2; k>0; k--)
				cout<<( (i >> (k-1))&0x1 );
			cout<<"1 "; // print the LSBs
			for(m=2; m<=10 ; m++)
				cout<<FactorArray[i][m-2]<<" ";
			cout<<endl;
	/*
			cout<<"1"; // print the MSB
			for(k=N-2; k>0; k--)
				cout<<( (i >> (k-1))&0x1 );
			cout<<"1 "; // print the LSBs
			for(m=2; m<=10 ; m++)
				cout<<NumArray[i][m-2]<<" ";
			cout<<endl;
	*/	
			count ++;
			if(count == J)
				return 1;
			
		}
	}
	// find the next prime number
	while(1) {
		prime_num ++;
		if(isPrime(prime_num)==1)
			break;
	}
}

return 0; 
}


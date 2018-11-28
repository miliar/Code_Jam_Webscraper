// Coin.cpp : Definiert den Einstiegspunkt für die Konsolenanwendung.
//

#include "stdafx.h"

#include "stdafx.h"


#include "stdafx.h"
#include <iostream>
#include <iomanip>
#include <algorithm>
#include <map>
#include <vector>
#include <set>
#include <string>
#include <sstream>
#include <bitset>

using namespace std;
const unsigned long MaxPrime = 1000000;
unsigned long Sieve[MaxPrime];

int _tmain(int argc, _TCHAR* argv[])
{
	int T;
	cin >> T;
	for(int NumCase=1; NumCase <=T; NumCase++) {
		unsigned  N,J;
		cin >> N >> J;
		cout << "Case #" << NumCase << ": " << endl;
		vector<unsigned long int> primes;
		for(unsigned long i=2;i<MaxPrime;i++) Sieve[i]=i;
		
		for(unsigned long i=2;i<MaxPrime;i++)
			for(unsigned long j=2;j<=sqrt(double(i))&&Sieve[i];j++) 
				if(Sieve[j] && Sieve[i]%j==0) Sieve[i]=0;



		for(unsigned long  i=0;i<(1UL<<(N-2)) && J>0;i++) {
			bitset<32> x((unsigned long long)(i*2UL+1L+(1UL<<(N-1))));
			int isPrime(0);
			unsigned long int divisors[11];
			for(int base=2; base <=10  && !isPrime ; base++) {
				unsigned long long Num1 = strtoul(x.to_string().c_str()  ,0,base);
				unsigned long long Num=0UL,CurMul=1;
				for(unsigned int i=0;i<N;i++) {
					if(x[i]) 
						Num = Num+CurMul;
					CurMul *= base;
				}
				divisors[base]=1;
				for(unsigned long i=2;i<=min(MaxPrime, (unsigned long)sqrt(double(Num))) && divisors[base] == 1;i++) {
					if(Sieve[i] && Num%Sieve[i]==0) {
						divisors[base]=Sieve[i];
					}
				}
				isPrime = divisors[base]==1;
			}
			if(!isPrime) {
				cout << x.to_string().substr(32-N) << ' ';
				for(int base=2; base <=10  && !isPrime ; base++)
					cout << divisors[base] << ' ';
				cout << endl;
				J--;
			}
		}
	}

	return 0;
}


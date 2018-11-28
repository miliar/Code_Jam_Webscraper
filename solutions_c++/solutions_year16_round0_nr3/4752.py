#include<cstdio>
#include<cstdlib>
#include<iostream>
#include<time.h>
#include<math.h>
using namespace std;

long long pot(long long a, long long b)
{
	long long w;
	if(b==0) return 1; 
	if(b==1) return a;
	if(b%2==0) { w=pot(a,b/2);	return w*w; }
	w=pot(a,b-1);
	return w*a;	
}

bool isPrime(long long n) {
	for(long long j =2; j<= sqrt(n)+1; j++) {
		if(n%j == 0) {
			return false;
		}
	}
	return true;
}

long long dev(long long n) {
	for(long long j =2; j<= sqrt(n)+1; j++) {
		if(n%j == 0) {
			return j;
		}
	}
	return -1;
}

long long int convert(int base, long long int n) {
	long long int p = 1, score = 0, x;
	for(int i = 0; i<16	; i++) {
		x=n%10;
		score += x*p;
		n/=10;
		p*=base;
	}
	return score;
}


int main() {
	int tq;
	cin>>tq;
	cin>>tq;
	cin>>tq;
	cout<<"Case #1:\n";
	long long number = 1000000000000001;
	long long int p = 1;
	long long temp;
	long long h;
	bool is;
	int primes = 1;
	while(primes<=50) {
		temp = number;
		for(int j = 0; j<=16; j++) {
			
			if(temp%10 == 2) {
				p = pot(10, j);
				number -= 2*p;
				number += p*10;
				temp = number;
				temp /= pot(10, j+1);
			}
			else temp /= 10;
		}
		is = true;
		for(long long k = 2; k<=10; k++) {
			h = convert(k, number);
			if( isPrime(h) ) {
				is = false;
			}
		}
		if(is) {
			cout<<number<<" ";
			primes++;
			for(long long k = 2; k<=10; k++) {
				h = convert(k, number);
			 	cout<<dev(h)<<" ";
			}
			cout<<endl;
		}
		number+=10;
	}
	
	return 0;
}





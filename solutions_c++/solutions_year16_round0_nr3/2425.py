#include <cstdio>
#include <iostream>
#include <stdlib.h>
#include <string.h>

using namespace std;

int isprime(long long N){
	//cout << "Chequeando si " << N << "es primo " << endl;
	if (N <= 1){
		return 0;
	}
	if (N <= 3){
		return 0;
	}
	if (N % 2 == 0){
		return 2;
	}
	if (N % 3 == 0){
		return 3;
	}
	long long i = 5;
	while (i*i <= N){
		if (N % i == 0){
			return i;
		}
		if (N% (i+2) == 0){
			return i + 2;
		}
		i+=6;
	}
	return 0;
}


long long nextComb(long long a){
	long long test = a;

	int counter = 1;
	int restar = 0;
	long long aux = 1;
	long long aux2 = 1;
	while(test /= 10){
		if (test%10 == 1){
			restar = counter;
		} 
		else if (test%10 == 0){
			while(counter--){
				aux*= 10;
			}
			while(restar--){
				aux2 = aux2*10 + 1;
			}
			return a + aux - (aux2 -1);
		}
		counter ++;
	}

	return 0;

}


void toString(char* a, long long b, int c){
	for (int i = c; i >= 0; i--){
		a[i] = b%10 + '0';
		b= b/10;
	}
}

int main(){

	int cases;

	int J,K;
	long long N = 1;
	bool primo;
	char s[16];
	int counter = 0;
	int divisores[11];

	cin >> cases;


	for (int c = 1; c <= cases; c++){


		cin >> K;
		cin >> J;

		cout << "Case #" << c << ":" << endl;


		for (int i = 1; i < K; i++){
			N = N*10;
		}
		N += 1;


		while ((N = nextComb(N)) != 0){
		//	cout << N << endl;
			memset(divisores,0,sizeof(divisores));
			toString(s,N,K);
			primo = false;
			for (int i = 2; i <= 10; i++){
				if ((divisores[i] = isprime(strtol(s,NULL,i))) == 0){
					primo = true;
					break;
				}
			}

			if (!primo){
				counter++;
				cout << N;
				for (int i = 2; i <= 10; i++){
					cout << " " <<divisores[i];
				}
				cout << endl;
			}

			if (counter == J){
				break;
			}

		}

	}
}
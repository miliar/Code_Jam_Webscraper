#include <iostream>
#include <cstdio>
#include <cmath>
#include <vector>

using namespace std;

vector<int> primes;
void sieve(int N) {
     int M=(N-1)/2;
     int x=(floor(sqrt(N))-1)/2,i,j;
     vector<bool> S(M+1,0);
     for (i=1;i<=x;i++)
         if (!S[i])
            for (j=2*i*(i+1);j<=M;j+=(2*i+1))
                S[j]=1;
 
     primes.push_back(2);
     for (i=1;i<=M;i++)
         if (!S[i])
                primes.push_back(2*i+1);
}

long long pow(int i, int p) {
	long long result = 1;
	for (int j = 1; j <= p; j++) {
		result *= i;
	}
	return result;
}

int primeDivisor(long long p) {
	for (int i = 0; primes[i] * 1LL * primes[i] <= p; i++) {
		if (p % primes[i] == 0) {
			return primes[i];
		}
	}
	return 0;
}

char* binaryString(int k) {
	char* str = new char[17];
	for (int i = 1; i < 15; i++) {
		str[i] = '0';
	}
	str[0] = '1';
	str[15] = '1';
	int j = 2;
	while (k > 0) {
		if(k % 2 == 1) {
			str[16 - j] = '1';
		}
		j++;
		k /= 2;
	}
	str[16] = '\0';
	return str;
}

int main() {
	sieve(100000000);
	int T, N, J;
	T = 1;
	for (int i = 0; i < T; i++) {
		N = 16; J = 50;
		printf("Case #%d:\n", i + 1);
		int count = 0;
		long long numberInBaseN[11];
		long long result[11];
		for (int k = 0; ; k++) {
			for (int i = 2; i < 11; i++) {
				numberInBaseN[i] = 1 + pow(i, N - 1);
			}
			int l = k;
			int p = 1;
			while(l > 0) {
				if(l % 2 == 1) {
					for (int i = 2; i < 11; i++) {
						numberInBaseN[i] += pow(i, p);
					}
				}
				l /= 2;
				p++;
			}
			int i;
			for (i = 2; i < 11; i++) {
				int p = primeDivisor(numberInBaseN[i]);
				if (p == 0) break;
				else result[i] = p;
			}
			if (i == 11) {
				printf("%s", binaryString(k));
				for (i = 2; i < 11; i++) {
					printf(" %lld", result[i]);
				}
				printf("\n");
				count++;
			}
			if(count == J) break;
		}
	}
}

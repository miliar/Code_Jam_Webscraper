#include <cstdio>
#include <iostream>
#include <cstring>
#include <cmath>
#include <vector>

using namespace std;

#define ll long long int

#define MAX 100000000
#define LMT 10000

unsigned flag[MAX/64];
unsigned primes[5761460], total;

#define chkC(n) (flag[n>>6] & (1<<((n>>1)&31)))
#define setC(n) (flag[n>>6] |= (1<<((n>>1)&31)))

void sieve()
{
    unsigned i, j, k;
    flag[0]|=0;
    for(i=3;i<LMT;i+=2)
        if(!chkC(i))    //if i is prime
            for(j=i*i,k=i<<1;j<MAX;j+=k)
                setC(j);

    primes[(j=0)++] = 2;
    
    for(i=3;i<MAX;i+=2)
        if(!chkC(i))    //if ith bit is clear/set to 0
            primes[j++] = i;
    total = j;
}

int isPrime(long long int num){
	int i;
	for(i = 0; i < total && primes[i] < ceil(sqrt(num)); i++) {
		if(num % primes[i] == 0) {
			return primes[i];
		}
	}
	return 0;
}

int isJamCoin(char str[]) {
	// printf("%d\n", primesLength);
	int count = 0,i,j,k;
	int arr[11];
	for(i = 2; i < 11; i++) {
		long long int num = 0;
		for(j = 15; j >= 0; j--) {
			num += 1ll * pow(i, 15-j) * (str[j] - '0');
		}
		int famous = isPrime(num);
		if(famous > 0){
			arr[i] = famous;
			count++;
		} else {
			break;
		}
	}
	if(count == 9) {
		printf("%s ", str);
		for( i = 2; i < 10; i++) {
			printf("%d ", arr[i]);
		}
		printf("%d\n", arr[i]);
		return 1;
	}
	return 0;
}

void generateStrings(int size, char str[size][18]) {
    int i,j,k;
    for(i = 0; i < size; ++i) {
        str[i][0] = '1';
        for(j = size/2, k = 1; j > 0; j /= 2, k++) {
            str[i][k] = (i/j%2) + '0';
        }
        str[i][k] = '1';
        str[i][k+1] = '\0';
    }
}

int main(){
	int t,n,j,test,i;
	scanf("%d",&t);
	for(test = 1; test <= t; test++) {
		printf("Case #%d:\n", test);
		scanf("%d%d", &n, &j);
		int size = pow(2,n-2);
		ll pSize = ceil(sqrt(1111111111111111));
		sieve();
		char str[size][18];
		generateStrings(size,str);
		for(i = 0; i < size && j>0; i++) {
			// printf("%s\n", str[i]);
			if(isJamCoin(str[i])) {
				j--;
			}
		}
	}
}

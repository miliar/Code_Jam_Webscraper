#include <cstdio>
#include <string>
#include <iostream>
#include <algorithm>

#define MAXN 10000000

using namespace std;

long long conv (long long n, int k){
	long long res = 0, aux = 1;
	while (n){
		if (n%2)
			res += aux;
		n /= 2;
		aux *= k;
	}
	return res;
}

long long check (long long n){

	for (long long i = 2; i*i <= n; i++)
		if(n%i == 0)
			return i;

	return 0;

}

int main(){

	long long N = (1<<15) + 1;
	long long t = 0;
	printf("Case #1:\n");
	while(t < 50){

		long long a = check(conv(N, 2));
		long long b = check(conv(N, 3));
		long long c = check(conv(N, 4));
		long long d = check(conv(N, 5));
		long long e = check(conv(N, 6));
		long long f = check(conv(N, 7));
		long long g = check(conv(N, 8));
		long long h = check(conv(N, 9));
		long long k = check(conv(N,10));
		if(a && b && c && d && e && f && g && h && k && (N%2)){
			string str = "";
			long long R = N;
			while(R){
				if(R%2)
					str = "1" + str;
				else
					str = "0" + str;
				R /= 2;

			}
			cout << str;
			printf(" %lld %lld %lld %lld %lld %lld %lld %lld %lld\n", a, b, c, d, e, f, g, h, k);
			t++;
		}

		N += 2;
	}

}

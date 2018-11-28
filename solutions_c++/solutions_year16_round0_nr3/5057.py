#include <bits/stdc++.h>

using namespace std;

#define debug 0

long long power[15][20];

void generatePower() {
	for (int i=2; i<=10; i++) {
		long long temp = 1LL;
		power[i][0] = temp;
		for (int j=1; j<=16; j++) {			
			temp *= i;
			power[i][j] = temp;
		}
	}
}

int isPrime(long long x) {
	for (long long i=2; i*i<=x; i++) {
		if (x%i == 0) {
			if (debug) printf("%lld is not a prime\n", x);
			return i;
		}
	}
	return -1;
}

long long convertFrom10To2(long long n) {
	long long ret = 0;
	string st = "";
	while (n>0) {
		st += ((n % 2) + '0');
		n /= 2;
	}
	long long pengali = 1;
	for (int i=0; i<st.length(); i++) {
		ret += ((st[i]-'0')*pengali);
		pengali*=10;
	}
	return ret;
}

long long baseX(long long n, int x) {
	long long ret = 0;
	long long original = n;
	int cnt = 0;
	while (n>0) {	
		long long temp = n%10;
		ret += temp*power[x][cnt];
		cnt++;
		n/=10;
	}
	if (debug) printf("%lld in base %d is %lld\n", original, x, ret);
	return ret;
}

bool isValid(long long n) {
	for (int i=2; i<=10; i++) {
		if (isPrime(baseX(n,i)) == -1) {
			if (debug) printf("%lld is a prime\n", baseX(n,i));
			return false; 
		}
	}
	return true;
}

void prove(long long n) {
	for (int i=2; i<=10; i++) {
		printf(" %lld",isPrime(baseX(n, i)));
	}
	printf("\n");
}

int main() {
	freopen("C-small.in", "r", stdin);
	freopen("output.out", "w", stdout);

	int t;
	scanf("%d", &t);
	generatePower();
	for (int tc=1; tc<=t; tc++) {
		printf("Case #%d:\n", tc);
		int j;
		int n;
		scanf("%d %d", &n, &j);
		long long start = power[2][n-1]+1;
		long long stop = power[2][n];
		if (debug) printf("n = %d start = %lld, stop = %lld\n", n, start, stop);
		int cnt = 0;
		for (long long xx = start; xx<stop && cnt<j; xx+=2) {
			long long x = convertFrom10To2(xx);
			if (debug) printf("%lld\n", x);
			if (isValid(x)) {
				cnt++;
				printf("%lld", x);
				prove(x);
			}
		}

	}
	return 0;

}
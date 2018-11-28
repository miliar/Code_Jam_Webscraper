#include <cmath>
#include <iostream>
#include <stdio.h>
using namespace std;

typedef long long ll;

int n, j;

int c = 0;
bool C[32];

int D[11]; // Divisors

bool prime(int n, int b) {
	ll num = 0;
	ll m = 1;
	for(int i=n-1; i>=0; i--) {
		if(C[i]) num += m;
		m *= b;
	}
	
	if(num % 2 == 0) {
		D[b] = 2;
		return false;
	}
	for(int i=3; i<sqrt(num); i+=2) {
		if(num % i == 0) {
			D[b] = i;
			return false;
		}
	}
	return true;
}

void dfs(int i) {
	if(c == j) return;
	
	if(i == n-1) {
		bool jamcoin = true;
		for(int b=2; b<=10; b++) {
			if(prime(n, b)) {
				jamcoin = false;
				break;
			}
		}
		if(jamcoin) {
			for(int j=0; j<n; j++) {
				printf("%d", C[j]);
			}
			
			for(int j=2; j<=10; j++) {
				printf(" %d", D[j]);
			}
			printf("\n");
			
			c++;
		}
	}
	else {
		dfs(i + 1);
		C[i] = true;
		dfs(i + 1);
		C[i] = false;
	}
}

int main() {
	freopen("c.in", "r", stdin);
	freopen("c.out", "w", stdout);
	
	int nn;
	scanf("%d\n", &nn);
	
	printf("Case #1:\n");
	scanf("%d %d\n", &n, &j);
	
	C[0] = C[n-1] = true;
	dfs(1);
	
	return 0;
}

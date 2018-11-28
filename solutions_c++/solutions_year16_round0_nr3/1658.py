#include <stdio.h>
#include <string.h>
#include <stdlib.h>
#include <set>
#include <iostream>

using namespace std;

typedef long long LL;

struct num {
	LL x;
	int b;
	num(LL _x, int _b) : x(_x), b(_b) {}
};

int findDivisor(num _n, int J) {
	int tryWith[6] = {3,5,7,11,13,17};
	for (int i = 0; i < 6; ++i) {
		num n = _n;
		LL mod = 0;
		LL p = 1;
		while(n.x > 0) {
			if(n.x&1) mod = ((mod + p)) % tryWith[i];
			p *= n.b;
			p %= tryWith[i];
			n.x >>= 1;
		}
		if (mod == 0) {
			return tryWith[i];
		}
	}
	return -1;
}

void printBinary(LL x) {
	char s[100];
	int k=0;
	while (x>0){
		s[k++] = (x&1); x>>=1;
	}
	for (--k; k >= 0; --k) printf("%d", int(s[k]));
}

void solve(int N, int J) {
	for (LL i = ((1L<<(N-1))+1); i < (1LL<<N) && J > 0; i += 2) {
		int div[11];
		int k=0;
		bool bad = false;
		for (int b = 2; !bad && b <= 10; ++b) {
			int d = findDivisor(num(i, b), J);
			if (d < 0) bad = true;
			else div[k++] = d;
		}
		if (!bad) {
			--J;
			printBinary(i);
			for (int x=0;x<9;++x) printf(" %d", div[x]);
			puts("");
		}
	}
}

int main() {
	int T;scanf("%d",&T);
	for(int t=1;t<=T;++t) {
		int N, J; scanf("%d%d",&N,&J);
		printf("Case #%d:\n", t); solve(N,J);
	}
	return 0;
}

#include <bits/stdc++.h>
#define fr(a,b,c) for(int a = b; a < c; a++)
#define rp(a,b) fr(a,0,b)
using namespace std;
#define maxn 10000100

long long a, b;
int qnt[maxn];

char lol[10000];
bool isPal(long long p) {
	int size = 0;
	while (p > 0) {
		lol[size++] = p%10 + '0';
		p/=10;
	}
	rp(i,size/2) if (lol[i] != lol[size-i-1]) return 0;
	return 1;
}

int main() {
	int cas = 1;
	for (int i = 1; i <= 10000000; i++) {
		qnt[i] = qnt[i-1];
		if (isPal(i) && isPal((long long)i*i)) qnt[i]++;
	}
	int T; scanf("%d", &T);
	while (T--) {
		scanf("%lld%lld", &a, &b);
		int c = (int)ceil(sqrt(a));
		int d = (int)sqrt(b);
		printf("Case #%d: %d\n", cas++, qnt[d]-qnt[c-1]);
	}
	return 0;
}
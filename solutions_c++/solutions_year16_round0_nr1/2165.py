#include <bits/stdc++.h>

using namespace std;

int T;
long long n;

bool met[10];

bool check(long long x) {
	while(x != 0) {
		int a = x % 10;
		x /= 10;
		met[a] = 1;
	}
	for(int i = 0; i < 10; i++) {
		if(!met[i]) return false;
	}
	return true;
}

int main() {
	freopen("A-large.in", "r", stdin);
	freopen("ans1.txt", "w", stdout);

	scanf("%d", &T);
	int cas = 0;
	while(T--) {
		memset(met,0,sizeof(met));
		printf("Case #%d: ", ++cas);
		scanf("%lld", &n);
		if(n == 0) printf("INSOMNIA\n");
		else {
			long long res = n;
			for(int i = 1; i <= 1000000; i++) {
				res = n * i;
				if(check(res)) break;
			}
			printf("%lld\n", res);
		}
	}
}
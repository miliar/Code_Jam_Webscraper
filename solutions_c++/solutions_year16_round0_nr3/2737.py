#include <cstdio>

const int n = 16;
const int j = 50;

int num[n];
int cnt ;
void output() {
	for (int i = 0; i < n; i++) {
		printf("%d", num[i]);
	}
	
	for (int base = 2; base <= 10; base++) {
		long long sum = 0;
		for (int i = 0; i < n; i++) {
			sum = sum * base + num[i];
		}
		// find divosr
		int d = 2;
		while (true) {
			if (sum % d == 0) break;
			d++;
		}
		printf(" %d", d);
	}
	printf("\n");
}

bool prime(long long x) {
	long long t = 2;
	//printf("%lld\n", x);
	while (t * t <= x) {
		if (x % t == 0) {
		//	printf("%lld %lld\n", x, t);
			return false;
		}
		t++;
	}
	return true;
}

bool check() {
	// for (int i = 0; i < n; i++) {
	// 	printf("%d", num[i]);
	// }
	// puts("");
	for (int base = 2; base <= 10; base ++) {
		long long sum = 0;
		for (int i = 0; i < n; i++) {
			sum = sum * base + num[i];
		}
	//	printf("base = %d, sum = %lld\n", base , sum);
		if (prime(sum) == true) return false;
	}
	return true;
}

void dfs(int start) {
//	printf("%d\n",start);
	if (cnt == j) return ;
	if (start == 15) {
		if (check()) {
			cnt ++;
			output();
		}
		return ;
	}
	num[start] = 0;
	dfs(start + 1);
	num[start] = 1;
	dfs(start + 1);
}

int main() {
	num[0] = 1;
	num[15] = 1;
	printf("Case #1:\n");
	dfs(1);
	return 0;
}
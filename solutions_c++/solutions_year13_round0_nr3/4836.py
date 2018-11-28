#include <cstdio>
#include <cmath>
#include <cstdlib>
#include <vector>
#include <algorithm>

using namespace std;

long long a, b;

void input() {
	scanf("%lld%lld", &a, &b);
}

int palindrome(long long num) {
	char buf[20];
	int len = 0;
	while(num) {
		buf[len++] = num%10;
		num /= 10;
	}

	for(int i = 0;i < len/2;i ++) if(buf[i] != buf[len-1-i]) return 0;
	return 1;
}

void solve() {
	int i;
	for(i = 1;((long long)i)*i < a;i ++) ;
	
	int res = 0;
	for(;((long long)i)*i <= b;i ++) if(palindrome(i)&&palindrome(((long long)i)*i)) ++ res;

	printf("%d\n", res);
}

int main() {
	freopen("C-small-attempt0.in", "r", stdin);
	freopen("output.txt", "w", stdout);

	int t;
	scanf("%d", &t);
	for(int cas = 1;cas <= t;cas ++) {
		input();
		printf("Case #%d: ", cas);
		solve();
	}
	return 0;
}
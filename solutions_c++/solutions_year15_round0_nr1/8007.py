#include <stdio.h>

#define MAXN 1005

using namespace std;

int n;
char aud[MAXN];

int num(char a) {
	return a - '0';
}

void Read() {
	scanf("%d",&n);
	scanf("%s",aud);
	int sum = 0;
	int res = 0;
	for (int i=0;i<=n;i++) {
		// printf("Info %d %d\n", sum, i);
		if ( sum < i ) {
			res += i - sum;
			sum = i;
		}
		sum += num(aud[i]);
	}
	printf("%d\n", res);
}

void Solve() {

}

int main () {
	int t;
	scanf("%d",&t);
	freopen("result.out","w",stdout);
	for (int i=1;i<=t;i++) {
		printf("Case #%d: ", i);
		Read();
		Solve();
	}
	return 0;
}
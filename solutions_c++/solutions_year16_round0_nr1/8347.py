#include <stdio.h>
using namespace std;
typedef long long LL;
int T;
LL N;
int chk[10];
void initchk() {
	for (int i = 0; i < 10; i++) 
		chk[i] = 0;
}
bool isok() {
	for (int i = 0; i < 10; i++){
		if (chk[i] == 0) {
			return false;
		}
	}
	return true;
}

void sol() {
	initchk();
	LL cnt = 1;
	if (N == 0) {
		printf("INSOMNIA\n");
		return;
	}

	while (!isok()) {
		LL cur = N*cnt;
		while (cur) {
			chk[cur % 10] = 1;
			cur /= 10;
		}
		if (isok())
			break;
		cnt++;
	}
	printf("%d\n", cnt*N);
}

int main() {
	scanf("%d\n", &T);

	for (int iter = 1; iter <= T; iter++) {
		printf("Case #%d: ", iter);
		scanf("%lld", &N);
		sol();
	}
}
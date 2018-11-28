#include <cstdio>

void sol(int ks) {
	int k, chk = 0, t = 0;
	bool v[15] = {false};
	scanf("%d", &k);
	if(k == 0) {
		printf("Case #%d: INSOMNIA\n", ks);
		return;
	}
	while(chk != 10) {
		chk = 0;
		t += k;
		int x = t;
		while(x) v[x % 10] = true, x /= 10;
		for(int i = 0;i < 10;i++) chk += v[i];
	}
	printf("Case #%d: %d\n", ks, t);
}

int main() {
	int n;
	scanf("%d", &n);
	for(int ks = 1;ks <= n;ks++)
		sol(ks);
}

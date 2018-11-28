#include <stdio.h>

int n, result;
int a[2000];

void init() {
	int i;
	char s[2000];
	scanf("%d",&n);
	scanf("%s",s);
	for (i=0; i<=n; ++i) a[i] = s[i] - '0';
}

void work() {
	int i;
	int tot = 0;
	result = 0;
	for (i=0; i<=n; ++i) {
		if (tot>=i) tot+=a[i];
		else {
			result += i - tot;
			tot += (i - tot) + a[i];
		}
	}
}

void output() {
	printf("%d\n", result);
}

int main() {
	freopen("a.in", "r", stdin);
	// FILE *fout=fopen("a.out","w");
	int T;
	int t;
	scanf("%d", &T);
	for (t=1; t<=T; ++t) {
		printf("Case #%d: ", t);
		init();
		work();
		output();
	}
	return 0;
}
#include <stdio.h>
#include <string.h>

int mark[10];

int count(int v) {
	while(v) {
		mark[v%10] = 1;
		v /= 10;
	}
	int res = 0;
	for (int i = 0; i < 10; ++i) {
		if (mark[i]) res++;
	}
	return res;
}

void f(int v) {
	if (v == 0) {
		printf("INSOMNIA\n");
		return;
	}
	for (int i = 1; ; ++i) {
		int num = count(v*i);
		if (num == 10) {
			printf("%d\n",v*i);
			break;
		}
	}
}

int main() {
	int n;
	freopen("A-large.in","r",stdin);
	freopen("large.txt","w",stdout);
	scanf("%d", &n);
	for (int i = 0; i < n; ++i) {
		int v;
		scanf("%d", &v);
		memset(mark,0,sizeof(mark));
		printf("Case #%d: ",i+1);
		f(v);
	}
	fclose(stdin);
	fclose(stdout);
	return 0;
}

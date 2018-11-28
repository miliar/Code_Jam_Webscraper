#include<stdio.h>
int record[10];

bool ExtractAndCheck(int n) {
	while(n) {
		int d = n%10;
		n /= 10;
		record[d] = 1;
	}
	for(int i = 0; i < 10; i++) {
		if(!record[i]) return 0;
	}
	return 1;
}
int Shepherd(int n) {
	for(int i = 1;; i++) {
		int sheep = i*n;
		if(ExtractAndCheck(sheep)) return sheep;
	}
}

int main() {
	int T, cnt = 0;;
	scanf("%d", &T);
	while(T--) {
		for(int i = 0; i < 10; i++) record[i] = 0;
		printf("Case #%d: ", ++cnt);

		int n;
		scanf("%d", &n);
		if(!n) printf("INSOMNIA\n");
		else {
			int ans = Shepherd(n);
			printf("%d\n", ans);
		}
	}
}

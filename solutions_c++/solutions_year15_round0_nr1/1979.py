#include <cstdio>
#include <cstdlib>

int main(){
	int n, t;
	char c;
	freopen("in.in", "r", stdin);
	freopen("out.out", "w", stdout);
	scanf("%d\n", &t);
	for (int k = 1; k<=t; k++){
		scanf("%d%c", &n, &c);
		int prev = 0, sum = 0;
		for (int i = 0; i<=n; i++){
			scanf("%c", &c);
			if ( prev < i ) {
				sum += ( i - prev );
				prev += ( i - prev );
			}
			prev += c - '0';
		}
		printf("Case #%d: %d\n", k, sum);
	}
	return 0;
}

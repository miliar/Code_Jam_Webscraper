#include <cstdio>

typedef long double ld;

int main() {
	int n;
	scanf("%d", &n);
	for(int i = 0; i < n; i++) {
		ld c, f, x;
		scanf("%Lf %Lf %Lf", &c, &f, &x);
		ld production = 2;
		ld final_result = x/production;
		ld time = 0;
		for(int i = 1; ; i++) {
			time += c/production;
			production += f;
			ld result = time + x/production;
			if(result < final_result)
				final_result = result;
			else
				break;
		}
		printf("Case #%d: %.7Lf\n", i+1, final_result);
	}
	return 0;
}

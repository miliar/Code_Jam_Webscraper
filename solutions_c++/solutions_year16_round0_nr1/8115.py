#include <cstdio>
using namespace std;

int main(){
	freopen("A-large.in", "r", stdin);
	freopen("A-large.out", "w", stdout);

	int t;
	unsigned long long n;
	scanf("%d", &t);
	for(int tcase = 1; tcase <= t; tcase++){
		int digits[10] = {0};
		scanf("%lld", &n);
		if(n == 0){
			printf("Case #%d: INSOMNIA\n", tcase);
			continue;
		}
		int sheep = 0;
		int times = 1;
		unsigned long long last, tmp;
		while(sheep < 10){
			sheep = 0;
			last = n * times;
			tmp = last;
			// printf("%lld,%d,%lld\n", n, times, tmp);
			do {
				digits[tmp % 10]++;
				tmp /= 10;
			} while(tmp);
			for(int i = 0; i < 10; i++){
				if(digits[i]) sheep++;
			}
			times++;
		}
		printf("Case #%d: %lld\n", tcase, last);
	}

	return 0;
}
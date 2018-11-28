#include <cstdio>
using namespace std;

char buf[50];

int main() {
	int n, nt = 1;
	scanf("%d", &n);
	while(n--) {
		int tmp, ans = 0, ch, sum = 0;
		scanf("%d", &tmp);
		getchar();
		for(int i = 0; i <= tmp; i++) {
			ch = getchar() - '0';
			if(sum - i < 0) {
				ans += i - sum;
				sum = i;
			}
			sum += ch;
		}
		printf("Case #%d: %d\n", nt++, ans);
		fgets(buf, 49, stdin);
	}
}
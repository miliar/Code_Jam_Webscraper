#include <cstdio>
#include <cstring>
#include <algorithm>
#define NMAX 6

using namespace std;

int main () {
	int n, t;
	char c;
	int count = 0;
	scanf("%d", &t);
	while (t--) {
		scanf("%d", &n);
		n++;
		int sum = 0, ans = 0;
		for (int i = 0; i < n; i++) {
			scanf(" %c", &c);
			int a = c - '0';
			if (sum >= i)
				sum += a;
			else {
				ans += (i - sum);
				sum += a + (i - sum);
			} 
		}
		printf("Case #%d: %d\n", ++count, ans);
	}
	return 0;
}
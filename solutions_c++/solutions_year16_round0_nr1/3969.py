#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include <unordered_set>

using std::unordered_set;

int main() {
	int T, C;
	long n;
	unordered_set<long> dict;
	scanf("%d", &T);
	//int x = 0;
	for (C=1; C<=T; ++C) {
		scanf("%ld", &n);
		if (!n) {
			printf("Case #%d: INSOMNIA\n", C);
			continue;
		}
		dict.clear();
		for (int i=1; ;++i) {
			long ans = i*n;
			//printf("%ld\n", ans);
			while (ans) {
				dict.insert(ans%10);
				ans/=10;
			}
			if (dict.size()>=10) {
				printf("Case #%d: %ld\n", C, i*n);
				//if (i > x)
				//	x = i;
				break;
			}
		}
	}
	//printf("%d\n", x);
	return 0;
}


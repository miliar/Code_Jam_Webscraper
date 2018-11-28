#include <cstdio>
#define MAX 1024
using namespace std;

int main(int argc, char const *argv[]) {
	int cases;
	int N;
	char str[MAX];

	scanf("%d", &cases);
	for(int i = 1; i <= cases; i++) {
		scanf("%d %s", &N, str);
		int ans = 0;
		int curr = str[0] - '0';

		for(int i = 1; i <= N; i++) {
			if(curr < i) {
				ans += (i - curr);
				curr += (i - curr);
			}
			curr += (str[i] - '0');
		}

		printf("Case #%d: %d\n", i, ans);
	}
	return 0;
}
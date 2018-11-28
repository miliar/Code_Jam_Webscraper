#include <cstdio>
using namespace std;

int main() {
	freopen("r1a\\A-large.in", "r", stdin);
	freopen("r1a\\A-large.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int N=1; N<=T; ++N) {
		char s[1001], t[2001] = {0};
		scanf("%s", s);
		int idx = 1000;
		t[idx] = s[0];
		for (int i=1; s[i]; ++i) {
			if (s[i] >= t[idx])
				t[--idx] = s[i];
			else
				t[idx+i] = s[i];
		}
		printf("Case #%d: ", N);
		puts(t + idx);
	}
}

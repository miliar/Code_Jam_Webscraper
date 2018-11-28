#include <cstdio>
#include <cstring>
using namespace std;

void proc(int caseIdx) {
	int n;
	scanf("%d", &n);

	printf("Case #%d: ", caseIdx);

	bool chk[10];
	memset(chk, 0, sizeof(chk));
	for (int loop = 1; loop <= 100; ++loop) {
		int p = loop * n;
		while (p > 0) {
			chk[p % 10] = true;
			p /= 10;
		}

		bool ok = true;
		for (int k = 0; k < 10; ++k) {
			if (chk[k] == false) {
				ok = false;
				break;
			}
		}
		if (ok) {
			printf("%d\n", loop * n);
			return;
		}
	}
	printf("INSOMNIA\n");
}

int main() {
	freopen("input.txt", "r", stdin);
	freopen("output.txt", "w", stdout);
	int t;
	scanf("%d", &t);
	for (int i = 1; i <= t; ++i) {
		proc(i);
	}
	return 0;
}
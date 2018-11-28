#include <cstdio>
#include <cstring>
#include <algorithm>
using namespace std;

int n;
char inp[200];
int d[200][2];

void proc(int caseIdx) {
	scanf("%s", inp + 1);
	n = strlen(inp + 1);

	memset(d, 0x1f, sizeof(d));
	d[0][0] = d[0][1] = 0;
	for (int i = 1; i <= n; ++i) {
		if (inp[i] == '+') {
			d[i][1] = d[i - 1][1];

			int j = i;
			while (j >= 1 && inp[j] == '+') {
				d[i][1] = min(d[i][1], d[j - 1][0] + 1);
				--j;
			}

			d[i][0] = min(d[i][0], d[i][1] + 1);
		}
		else {
			d[i][0] = d[i - 1][0];

			int j = i;
			while (j >= 1 && inp[j] == '+') {
				d[i][0] = min(d[i][0], d[j - 1][1] + 1);
				--j;
			}

			d[i][1] = min(d[i][1], d[i][0] + 1);
		}
	}
	printf("Case #%d: %d\n", caseIdx, d[n][1]);
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
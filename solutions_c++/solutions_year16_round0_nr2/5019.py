#include <cstdio>
#include <string.h>

FILE * in = fopen("in.txt", "r");
FILE * out = fopen("out.txt", "w");

using namespace std;

char d[10005];

int main() {
	int t;

	fscanf(in, "%d", &t);

	for (int i = 1; i <= t; i++) {
		fscanf(in, "%s", d);

		int len = strlen(d), flag, ans = 0;

		if (d[len - 1] == '-')
			ans++;

		for (int j = len - 2; j >= 0; j--) {
			if (d[j] == '-' && ans % 2 == 0) ans++;
			else if (d[j] == '+' && ans % 2 == 1) ans++;
		}

		for (int j = 0; j <= len; j++) d[j] = 0;

		fprintf(out, "Case #%d: %d\n", i, ans);
	}
}
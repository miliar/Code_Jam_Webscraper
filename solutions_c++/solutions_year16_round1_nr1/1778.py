#include <cstdio>
#include <string>

using namespace std;

int main() {
	int T;
	char buf[1024];

	fgets(buf, 1024, stdin);

	sscanf(buf, "%d", &T);

	int i, j, k;

	for (i = 0; i < T; ++i) {
		string res;

		memset(buf, 0x00, sizeof(buf));
		fgets(buf, 1024, stdin);

		for (j = 0; j < 1024; ++j) {
			if (buf[j] == 0x00 || buf[j] == '\n')
				break;

			string ems = "A";
			ems[0] = buf[j];

			for (k = 0; k < j; ++k) {
				if (buf[j] > res[k]) {
					res = ems + res;
					break;
				} else if (buf[j] < res[k]) {
					res = res + ems;
					break;
				}
			}

			if (k == j)
				res = res + ems;
		}

		printf("Case #%d: %s\n", i + 1, res.c_str());
	}
}
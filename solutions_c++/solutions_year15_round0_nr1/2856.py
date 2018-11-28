#include <cstdio>
#include <cstdlib>
#include <string>
#include <algorithm>

using namespace std;

int main() {
	char buf[2000];
	char aud[2000];
	int audiences[1200];

	memset(buf, 0x00, sizeof(buf));

	while (buf[0] == 0x00 || buf[0] == '\n')
		gets(buf);

	int T;
	int S;
	int i, j;

	sscanf(buf, "%d", &T);

	for (i = 0; i < T; ++i) {
		memset(buf, 0x00, sizeof(buf));
		memset(aud, 0x00, sizeof(aud));

		while (buf[0] == 0x00 || buf[0] == '\n')
			gets(buf);

		sscanf(buf, "%d %s", &S, aud);

		int claps = 0;
		int morefriends = 0;

		for (j = 0; aud[j] != 0x00 && aud[j] != '\n'; ++j) {
			audiences[j] = aud[j] - '0';

			if (audiences[j] > 0 && claps < j) {
				//printf("we need %d more friends when %d\n", j - claps, j);
				morefriends += j - claps;
				claps += j - claps;
			}

			claps += audiences[j];
		}

		printf("Case #%d: %d\n", i + 1, morefriends);
	}
}
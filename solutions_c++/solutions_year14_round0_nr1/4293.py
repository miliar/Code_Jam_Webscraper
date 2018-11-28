#include <cstdio>
#include <cstring>
using namespace std;

int main() {
	FILE * fin = fopen("A.in", "r"), * fout = fopen("A.out", "w");
	int T, t, i, j, l, c, cards[16];
	fscanf(fin, "%d", &T);
	for (t = 1; t <= T; ++t) {
		memset(cards, 0, 64);
		fscanf(fin, "%d", &l);
		for (i = 0; i < 4; ++i) {
			for (j = 0; j < 4; ++j) {
				fscanf(fin, "%d", &c);
				if (i + 1 == l) {
					++cards[c - 1];
				}
			}
		}
		fscanf(fin, "%d", &l);
		for (i = 0; i < 4; ++i) {
			for (j = 0; j < 4; ++j) {
				fscanf(fin, "%d", &c);
				if (i + 1 == l) {
					++cards[c - 1];
				}
			}
		}
		l = 0;
		c = 0;
		for (i = 0; i < 16; ++i) {
			if (cards[i] == 2) {
				++l;
				c = i + 1;
			}
		}
		if (l == 1) {
			fprintf(fout, "Case #%d: %d\n", t, c);
		} else if (!l) {
			fprintf(fout, "Case #%d: Volunteer cheated!\n", t);
		} else {
			fprintf(fout, "Case #%d: Bad magician!\n", t);
		}
	}
	return 0;
}


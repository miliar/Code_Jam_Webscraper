#include <cstdio>
#include <cstring>
int main()
{
	FILE *fp = fopen("B-large.in", "r"), *op = fopen("B-large.txt", "w");
	int t;
	fscanf(fp, "%d", &t);
	for (int tc = 1;tc <= t;++tc) {
		char str[101];
		bool happy[101] = { false };
		fscanf(fp, "%s", str);
		int len = strlen(str), plus = 0, cnt = 0;
		for (int i = 0;i < len;++i) {
			if (str[i] == '+') {
				++plus;
				happy[i] = true;
			}
			else happy[i] = false;
		}
		while (plus != len) {
			++cnt;
			if (happy[0]) {
				for (int i = 0;i < len && happy[i];++i) {
					--plus;
					happy[i] = false;
				}
			}
			else {
				int p;
				for (p = len - 1;p >= 0 && happy[p];--p);
				for (int i = 0;i <= p / 2;++i) {
					bool tmp = happy[i];
					happy[i] = !happy[p - i];
					happy[p - i] = !tmp;

					if (happy[i]) ++plus;
					else --plus;
					if (p - i != p / 2) {
						if (happy[p - i]) ++plus;
						else --plus;
					}
				}
			}
		}
		fprintf(op, "Case #%d: %d\n", tc, cnt);
	}

	return 0;
}
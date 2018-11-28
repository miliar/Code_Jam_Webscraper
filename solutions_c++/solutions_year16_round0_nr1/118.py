#include <cstdio>

int cnt;
bool appeared[10];

void see(int digit) {
	if (!appeared[digit])
		appeared[digit] = true, ++cnt;
}

void countNumbers(int s) {
	if (0 == s)
		see(0);
	else {
		while (s) {
			see(s % 10);
			s /= 10;
		}
	}

}

int sheep(int N) {
	cnt = 0;
	for (int i = 0; i < 10; ++i)
		appeared[i] = false;
	for (int s = N; ; s += N) {
		countNumbers(s);
		if (10 == cnt)
			return s;
	}
}

int main() {
	int T, N;
	FILE *ifp = fopen("A-large.in", "r");
	FILE *ofp = fopen("A.out", "w");
	fscanf(ifp, "%d", &T);
	for (int t = 1; t <= T; ++t) {
		fscanf(ifp, "%d", &N);
		fprintf(ofp, "Case #%d: ", t);
		if (N)
			fprintf(ofp, "%d\n", sheep(N));
		else
			fprintf(ofp, "INSOMNIA\n");
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}

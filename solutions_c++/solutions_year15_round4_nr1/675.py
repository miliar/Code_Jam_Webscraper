#include <bits/stdc++.h>
using namespace std;
const int mn = 200;

char a[mn][mn];
bool seen[4][mn];

int getdir(char c) {
	switch (c) {
	case '^':
		return 0;
	case '>':
		return 1;
	case 'v':
		return 2;
	case '<':
		return 3;
	default:
		return -1;
	}
	return -1;
}
int main() {
	int Tc;
	scanf("%d", &Tc);
	for (int Tn = 1; Tn <= Tc; ++Tn) {
		int R, C;
		scanf("%d%d", &R, &C);
		for (int i = 0; i < R; ++i) {
			scanf("%s", a[i]);
		}
		bool wrong = 0;
		for (int i = 0; i < R && !wrong; ++i)
			for (int j = 0; j < C && !wrong; ++j) {
				int arrowd = getdir(a[i][j]);
				if (arrowd != -1) {
					bool found = 0;
					for (int k = 0; k < R; ++k)
						if (k != i) {
							if (getdir(a[k][j]) != -1) {
								found = 1;
								break;
							}
						}
					for (int k = 0; k < C; ++k)
						if (k != j) {
							if (getdir(a[i][k]) != -1) {
								found = 1;
								break;
							}
						}
					if (!found) {
						wrong = 1;
					}
				}
			}
		int ans = -1;
		if (!wrong) {
			ans = 0;
			memset(seen, 0, sizeof(seen));
			for (int i = 0; i < R; ++i)
				for (int j = 0; j < C; ++j) {
					int arrowd = getdir(a[i][j]);
					if (arrowd == -1) {
						continue;
					} else {
						bool found = 0;
						switch (arrowd) {
						case 0:
							for (int k = 0; k < i; ++k)
								if (getdir(a[k][j]) != -1)
									found = 1;
							break;
						case 1:
							for (int k = j + 1; k < C; ++k)
								if (getdir(a[i][k]) != -1)
									found = 1;
							break;
						case 2:
							for (int k = i + 1; k < R; ++k)
								if (getdir(a[k][j]) != -1)
									found = 1;
							break;
						case 3:
							for (int k = 0; k < j; ++k)
								if (getdir(a[i][k]) != -1)
									found = 1;
							break;
						}
						if (!found)
							ans++;
					}
				}
		} else {
			ans = -1;
		}

		printf("Case #%d: ", Tn);
		if (ans == -1)
			puts("IMPOSSIBLE");
		else
			printf("%d\n", ans);
	}
	return 0;
}

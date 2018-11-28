#include<cstdio>
#include<cstring>

#define SMAX 100

bool constant(char c) {
	return (c!='a') && (c!='e') && (c!='i') && (c!='o') && (c!='u');
}

char name[SMAX+1];

int solve(bool *consonants, int n, int size) {
	int ret = 0, size2 = size-n;
	for (int i = 0; i <= size2; ++i) {
		int nc = 0;
		bool cons = false;
		for (int j = i; j < size; ++j) {
			if (nc < n && consonants[j]) {
				if (cons) ++nc;
				else {
					nc = 1;
					cons = true;
				}
			} else cons = false;
			if (nc >= n) ++ret;
		}
	}
	return ret;
}

int main() {
	int T;
	scanf("%d", &T);
	char name[SMAX+1];
	bool constants[SMAX+1];
	for (int t = 0; t < T; ++t) {
		int n, size;
		scanf("%s%d", name, &n);
		size = strlen(name);
		for (int i = 0; i < size; ++i) constants[i] = constant(name[i]);
		printf("Case #%d: %d\n", t+1, solve(constants, n, size));
	}
	return 0;
}
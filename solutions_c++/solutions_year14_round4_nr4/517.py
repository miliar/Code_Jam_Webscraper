#include <cstdio>
#include <vector>
#include <cstring>
#include <algorithm>

int M, N;
int ans = 0, acnt;

struct Str {
	char c[11];
	bool operator<(const Str &cmp) const {
		int i = 0;
		for ( ; c[i] && cmp.c[i]; ++i)
			if (c[i] != cmp.c[i]) return c[i] < cmp.c[i];
		return c[i] < cmp.c[i];
	}	
} str[10];

int put[10];

std::vector<Str> sets[4];

int calc() {
	int tmp = 0;
	for (int i = 0; i < N; ++i)
		sets[i].clear();
	for (int i = 0; i < M; ++i)
		sets[put[i]].push_back(str[i]);
	for (int i = 0; i < N; ++i) {
		if (sets[i].size() == 0) return -1;
		std::sort(sets[i].begin(), sets[i].end());
		for (int j = 0; j < sets[i].size(); ++j) {
			tmp += strlen(sets[i][j].c);
			if (j > 0) {
				int k = 0;
				while (sets[i][j].c[k] != 0 && 
						sets[i][j].c[k] == sets[i][j - 1].c[k]) ++k;
				tmp -= k;
			}
			//puts(sets[i][j].c);
		}
		//puts("----------");
	}
	//puts("===========");
	//printf("%d\n", tmp);
	return tmp + N;
}

void go(int dep) {
	if (dep == M) {
		int tmp = calc();
		if (tmp > ans) {
			ans = tmp;
			acnt = 1;;
		} else if (tmp == ans) {
			++acnt;
		}
		return;
	}
	for (int i = 0; i < N; ++i) {
		put[dep] = i;
		go(dep + 1);
	}
	return;
}

int main() {
	freopen("D-small-attempt1.in", "r", stdin);
	freopen("D-small.out", "w", stdout);
	int T;
	scanf("%d", &T);
	for (int t = 1; t <= T; ++t) {
		acnt = ans = 0;
		scanf("%d%d", &M, &N);
		for (int i = 0; i < M; ++i)
			scanf("%s", str[i].c);
		go(0);
		printf("Case #%d: %d %d\n", t, ans, acnt);
	}
}
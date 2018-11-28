#include <algorithm>
#include <cstring>
#include <cstdio>

using namespace std;

const int MAXN = 5e3 + 10;

int N, R, P, S;
char s[MAXN], t[MAXN];
bool Cnt;

inline void Check(int a, int b, int l) {
	bool Jud = 0;
	for (int i = 0; i < l; ++i) {
		if (t[a + i] < t[b + i]) { Jud = 1; break;}
		else if (t[a + i] > t[b + i]) break;
	}
	if (!Jud) for (int i = 0; i < l; ++i) swap(t[a + i], t[b + i]);
}

void Calc() {
	int RR = 0, PP = 0, SS = 0;
	for (int i = 1; i <= N; i ++) {
		if (t[i] == 'R') RR ++;
		if (t[i] == 'P') PP ++;
		if (t[i] == 'S') SS ++;
	}
	if (RR != R || PP != P || SS != S) return;
	if (!Cnt) {
		Cnt = 1;
		for (int i = 1; i <= N; ++i) s[i] = t[i];
		return;
	}
	bool Jud = 0;
	for (int i = 1; i <= N; i ++) {
		if (t[i] < s[i]) { Jud = 1; break;}
		else if (t[i] > s[i]) break;
	}
	if (!Jud) for (int i = 1; i <= N; ++i) swap(s[i], t[i]);
}

void Dfs(char C, int l, int r) {
	if (l == r) { t[l] = C; return;}
	int Mid = (l + r) >> 1;
	char A, B;
	A = C;
	if (C == 'R') B = 'S'; if (C == 'S') B = 'P'; if (C == 'P') B = 'R';
	Dfs(A, l, Mid);
	Dfs(B, Mid + 1, r);
	Check(l, Mid + 1, Mid - l + 1);
	if (l == 1 && r == N) Calc();
}

void Work(int Ask) {
	printf("Case #%d: ", Ask);
	scanf("%d%d%d%d", &N, &R, &P, &S);
	N = 1 << N, Cnt = 0;
	Dfs('R', 1, N), Dfs('P', 1, N), Dfs('S', 1, N);
	if (!Cnt) printf("IMPOSSIBLE\n"); else {
		for (int i = 1; i <= N; i ++) printf("%c", s[i]);
		printf("\n");
	}
}

int main() {
	freopen("AA.in", "r", stdin), freopen("AA.out", "w", stdout);
	int Test;
	scanf("%d", &Test);
	for (int i = 1; i <= Test; i ++) Work(i);
	return 0;
}

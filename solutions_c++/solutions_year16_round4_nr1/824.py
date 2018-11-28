#include <cstdio>
#include <string>
#include <iostream>
#include <cstring>
using namespace std;

const int MAXN = 12;
const int R = 0, P = 1, S = 2;
string f[MAXN + 1][3];
int cnt[MAXN + 1][3][3] = {0};

int char2int(char c) {
	if (c == 'R') return R;
	if (c == 'P') return P;
	return S;
}

void preprocess() {
	f[0][R] = "R";
	f[0][P] = "P";
	f[0][S] = "S";
	for (int i = 0; i < 3; ++i)
		for (int j = 0; j < 3; ++j)
			cnt[0][i][j] = 0;
	cnt[0][R][R] = cnt[0][P][P] = cnt[0][S][S] = 1;
	for (int i = 1; i <= MAXN; ++i) {
		f[i][R] = min(f[i - 1][R] + f[i - 1][S], f[i - 1][S] + f[i - 1][R]);
		f[i][P] = min(f[i - 1][P] + f[i - 1][R], f[i - 1][R] + f[i - 1][P]);
		f[i][S] = min(f[i - 1][S] + f[i - 1][P], f[i - 1][P] + f[i - 1][S]);
	}
	cout << "Finish!\n";
	for (int i = 0; i <= MAXN; ++i) {
		for (int j = 0; j < 3; ++j) {
			int len = f[i][j].length();
			for (int k = 0; k < len; ++k)
				++cnt[i][j][char2int(f[i][j][k])];
		}
	}
}

string findAns(int N, int r, int p, int s) {
	if (cnt[N][R][R] == r && cnt[N][R][P] == p && cnt[N][R][S] == s) return f[N][R];
	if (cnt[N][P][R] == r && cnt[N][P][P] == p && cnt[N][P][S] == s) return f[N][P];
	if (cnt[N][S][R] == r && cnt[N][S][P] == p && cnt[N][S][S] == s) return f[N][S];
	return "IMPOSSIBLE";
}

int main() {
	FILE *ifp = fopen("A-large.in", "r");
	FILE *ofp = fopen("A.out", "w");
	int T, N, r, p, s;
	fscanf(ifp, "%d", &T);
	preprocess();
	for (int t = 1; t <= T; ++t) {
		fscanf(ifp, "%d%d%d%d", &N, &r, &p, &s);
		fprintf(ofp, "Case #%d: %s\n", t, findAns(N, r, p, s).c_str());
	}
	fclose(ifp);
	fclose(ofp);
	return 0;
}

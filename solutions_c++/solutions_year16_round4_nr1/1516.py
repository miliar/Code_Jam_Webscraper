#define _CRT_SECURE_NO_WARNINGS
#include <cstdio>
#include <cstdlib>
#include <cctype>
#include <string>
#include <vector>
#include <unordered_map>
#include <unordered_set>
#include <map>
#include <set>
#include <queue>
#include <stack>
#include <list>
using namespace std;

char s[10];
int m, a, b, c;

char wingame(char x, char y) {
	if (x == 'P' && y == 'R' || x == 'R' && y == 'P') return 'P';
	if (x == 'R' && y == 'S' || x == 'S' && y == 'R') return 'R';
	if (x == 'S' && y == 'P' || x == 'P' && y == 'S') return 'S';
	return -1;
}

bool check() {
	vector<char> tmp;
	for (int i = 0; i < m; ++i) tmp.push_back(s[i]);
	while (tmp.size() > 1) {
		vector<char> newtmp;
		for (int i = 0; i < tmp.size(); i += 2) {
			if (tmp[i] == tmp[i + 1]) return false;
			newtmp.push_back(wingame(tmp[i], tmp[i + 1]));
		}
		tmp = move(newtmp);
	}
	return true;
}

bool dfs(int pos, int cura, int curb, int curc) {
	if (pos == m) {
		if (check()) return true;
		return false;
	}
	if (cura < a) {
		s[pos] = 'P';
		if (dfs(pos + 1, cura + 1, curb, curc)) return true;
	}
	if (curb < b) {
		s[pos] = 'R';
		if (dfs(pos + 1, cura, curb + 1, curc)) return true;
	}
	if (curc < c) {
		s[pos] = 'S';
		if (dfs(pos + 1, cura, curb, curc + 1)) return true;
	}
	return false;
}

int main() {
	FILE *fp = fopen("A-small-attempt0.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int T;
	fscanf(fp, "%d", &T);
	for (int iii = 0; iii < T; ++iii) {
		int n;
		fscanf(fp, "%d", &n);
		m = (1 << n);
		fscanf(fp, "%d%d%d", &b, &a, &c);
		fprintf(fout, "Case #%d: ", iii + 1);
		if (dfs(0, 0, 0, 0)) {
			s[m] = '\0';
			fprintf(fout, "%s\n", s);
		}
		else fprintf(fout, "IMPOSSIBLE\n");
	}
	fclose(fp);
	fclose(fout);
	return 0;
}
#include <cstdio>
#include <cstdlib>
#include <cctype>

char map[100][100];
int m, n;

bool walk(int j, int k, int x, int y) {
    j += x;
    k += y;
    while (j >= 0 && j < m && k >=0 && k <n) {
        if (map[j][k] != '.') return true;
        j += x;
        k += y;
    }
    return false;
}

int work() {
    int ans = 0;
    for (int j = 0; j < m; ++j) 
        for (int k = 0; k < n; ++k) {
            if (map[j][k] == '.') continue;
            if (map[j][k] == '>' && walk(j, k, 0, 1)) continue;
            if (map[j][k] == '<' && walk(j, k, 0, -1)) continue;
            if (map[j][k] == '^' && walk(j, k, -1, 0)) continue;
            if (map[j][k] == 'v' && walk(j, k, 1, 0)) continue;
            if (walk(j, k, 0, 1) || walk(j, k, 1, 0) || walk(j, k, -1, 0) || walk(j, k, 0, -1)) ++ans;
            else return -1;
        }
    return ans;
}

int main() {
	FILE *fp = fopen("A-large.in", "r");
	FILE *fout = fopen("out.txt", "w");
	int T;
	fscanf(fp, "%d", &T);
	for (int i = 0; i < T; ++i) {
        fscanf(fp, "%d%d", &m, &n);
        for (int j = 0; j < m; ++j) {
            for (int k = 0; k < n; ++k)
                fscanf(fp, " %c", &map[j][k]);
        }
        int ans = work();
		fprintf(fout, "Case #%d: ", i + 1);
        if (ans >= 0) fprintf(fout, "%d\n", ans);
        else fprintf(fout, "IMPOSSIBLE\n");
	}
	fclose(fp);
	fclose(fout);
	return 0;
}
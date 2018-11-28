#include <cstdio>
#include <cstring>

int Arr[26];
int Ans[10];

int main() {
	//FILE *fi = fopen("sample.in", "r");
	FILE *fi = fopen("A-large.in", "r");
	//FILE *fi = fopen("A-small-attempt0.in", "r");
	FILE *fo = fopen("output.txt", "w");
	int T;

	int len;
	char buffer[2005];

	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%s", buffer);
		memset(Arr, 0, sizeof Arr);
		memset(Ans, 0, sizeof Ans);
		len = strlen(buffer);
		for (int i = 0; i < len; i++) {
			Arr[buffer[i] - 'A']++;
		}

		// find 0
		int tmp;
		if (tmp = Arr['Z' - 'A']) {
			Ans[0] = tmp;
			Arr['Z' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
			Arr['R' - 'A'] -= tmp;
			Arr['O' - 'A'] -= tmp;
		}
		// find 2
		if (tmp = Arr['W' - 'A']) {
			Ans[2] = tmp;
			Arr['T' - 'A'] -= tmp;
			Arr['W' - 'A'] -= tmp;
			Arr['O' - 'A'] -= tmp;
		}
		// find 4
		if (tmp = Arr['U' - 'A']) {
			Ans[4] = tmp;
			Arr['F' - 'A'] -= tmp;
			Arr['O' - 'A'] -= tmp;
			Arr['U' - 'A'] -= tmp;
			Arr['R' - 'A'] -= tmp;
		}
		// find 6
		if (tmp = Arr['X' - 'A']) {
			Ans[6] = tmp;
			Arr['S' - 'A'] -= tmp;
			Arr['I' - 'A'] -= tmp;
			Arr['X' - 'A'] -= tmp;
		}
		// find 8
		if (tmp = Arr['G' - 'A']) {
			Ans[8] = tmp;
			Arr['E' - 'A'] -= tmp;
			Arr['I' - 'A'] -= tmp;
			Arr['G' - 'A'] -= tmp;
			Arr['H' - 'A'] -= tmp;
			Arr['T' - 'A'] -= tmp;
		}
		// find 3
		if (tmp = Arr['H' - 'A']) {
			Ans[3] = tmp;
			Arr['T' - 'A'] -= tmp;
			Arr['H' - 'A'] -= tmp;
			Arr['R' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
		}
		// find 1
		if (tmp = Arr['O' - 'A']) {
			Ans[1] = tmp;
			Arr['O' - 'A'] -= tmp;
			Arr['N' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
		}
		// find 7
		if (tmp = Arr['S' - 'A']) {
			Ans[7] = tmp;
			Arr['S' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
			Arr['V' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
			Arr['N' - 'A'] -= tmp;
		}
		// find 5
		if (tmp = Arr['F' - 'A']) {
			Ans[5] = tmp;
			Arr['F' - 'A'] -= tmp;
			Arr['I' - 'A'] -= tmp;
			Arr['V' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
		}
		// find 9
		if (tmp = Arr['E' - 'A']) {
			Ans[9] = tmp;
			Arr['N' - 'A'] -= tmp;
			Arr['I' - 'A'] -= tmp;
			Arr['N' - 'A'] -= tmp;
			Arr['E' - 'A'] -= tmp;
		}
		fprintf(fo, "Case #%d: ", t);
		for (int i = 0; i < 10; i++) {
			for (int j = 0; j < Ans[i]; j++) {
				fprintf(fo, "%d", i);
			}
		}
		fprintf(fo, "\n");
	}

	fclose(fi);
	fclose(fo);
	return 0;
}

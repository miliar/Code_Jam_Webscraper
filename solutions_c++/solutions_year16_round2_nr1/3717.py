#include <stdio.h>

char S[20];
int count[26];
int result[10];

int backout(int number) {
	switch (number) {
	case 0:
			count['Z' - 'A']++;
			count['E' - 'A']++;
			count['R' - 'A']++;
			count['O' - 'A']++;
		break;
	case 1:
			count['O' - 'A']++;
			count['N' - 'A']++;
			count['E' - 'A']++;
		break;
	case 2:
			count['T' - 'A']++;
			count['W' - 'A']++;
			count['O' - 'A']++;
		break;
	case 3:
			count['T' - 'A']++;
			count['H' - 'A']++;
			count['R' - 'A']++;
			count['E' - 'A']++;
			count['E' - 'A']++;
		break;
	case 4:
			count['F' - 'A']++;
			count['O' - 'A']++;
			count['U' - 'A']++;
			count['R' - 'A']++;
		break;
	case 5:
			count['F' - 'A']++;
			count['I' - 'A']++;
			count['V' - 'A']++;
			count['E' - 'A']++;
		break;
	case 6:
			count['S' - 'A']++;
			count['I' - 'A']++;
			count['X' - 'A']++;
		break;
	case 7:
			count['S' - 'A']++;
			count['E' - 'A']++;
			count['V' - 'A']++;
			count['E' - 'A']++;
			count['N' - 'A']++;
		break;
	case 8:
			count['E' - 'A']++;
			count['I' - 'A']++;
			count['G' - 'A']++;
			count['H' - 'A']++;
			count['T' - 'A']++;
		break;
	case 9:
			count['N' - 'A']++;
			count['I' - 'A']++;
			count['N' - 'A']++;
			count['E' - 'A']++;
		break;
	default:
		return 0;
	}
	return 1;
}
int check(int number) {
	switch (number) {
	case 0:
		if (count['Z' - 'A'] && count['E' - 'A'] && count['R' - 'A'] && count['O' - 'A']) {
			count['Z' - 'A']--;
			count['E' - 'A']--;
			count['R' - 'A']--;
			count['O' - 'A']--;
			return 4;
		}
		break;
	case 1:
		if (count['O' - 'A'] && count['N' - 'A'] && count['E' - 'A']) {
			count['O' - 'A']--;
			count['N' - 'A']--;
			count['E' - 'A']--;
			return 3;
		}
		break;
	case 2:
		if (count['T' - 'A'] && count['W' - 'A'] && count['O' - 'A']) {
			count['T' - 'A']--;
			count['W' - 'A']--;
			count['O' - 'A']--;
			return 3;
		}
		break;
	case 3:
		if (count['T' - 'A'] && count['H' - 'A'] && count['R' - 'A'] && count['E' - 'A'] >= 2) {
			count['T' - 'A']--;
			count['H' - 'A']--;
			count['R' - 'A']--;
			count['E' - 'A']--;
			count['E' - 'A']--;
			return 5;
		}
		break;
	case 4:
		if (count['F' - 'A'] && count['O' - 'A'] && count['U' - 'A'] && count['R' - 'A']) {
			count['F' - 'A']--;
			count['O' - 'A']--;
			count['U' - 'A']--;
			count['R' - 'A']--;
			return 4;
		}
		break;
	case 5:
		if (count['F' - 'A'] && count['I' - 'A'] && count['V' - 'A'] && count['E' - 'A']) {
			count['F' - 'A']--;
			count['I' - 'A']--;
			count['V' - 'A']--;
			count['E' - 'A']--;
			return 4;
		}
		break;
	case 6:
		if (count['S' - 'A'] && count['I' - 'A'] && count['X' - 'A']) {
			count['S' - 'A']--;
			count['I' - 'A']--;
			count['X' - 'A']--;
			return 3;
		}
		break;
	case 7:
		if (count['S' - 'A'] && count['E' - 'A'] >= 2 && count['V' - 'A'] && count['N' - 'A']) {
			count['S' - 'A']--;
			count['E' - 'A']--;
			count['V' - 'A']--;
			count['E' - 'A']--;
			count['N' - 'A']--;
			return 5;
		}
		break;
	case 8:
		if (count['E' - 'A'] && count['I' - 'A'] && count['G' - 'A'] && count['H' - 'A'] && count['T' - 'A']) {
			count['E' - 'A']--;
			count['I' - 'A']--;
			count['G' - 'A']--;
			count['H' - 'A']--;
			count['T' - 'A']--;
			return 5;
		}
		break;
	case 9:
		if (count['N' - 'A'] >= 2 && count['I' - 'A'] && count['E' - 'A']) {
			count['N' - 'A']--;
			count['I' - 'A']--;
			count['N' - 'A']--;
			count['E' - 'A']--;
			return 4;
		}
		break;
	default:
		return 0;
	}
	return 0;
}

int findRet(int size) {
	int res;
	int ret;

	if (!size) return 1;
	for (int i = 0; i < 10; i++) {
		if (res = check(i)) {
			if (findRet(size - res)) {
				result[i]++;
				return 1;
			}
			backout(i);
		}
	}
	return 0;
}

void main() {
	FILE *in, *out;
	in = fopen("A-small-attempt1.in", "r");
	out = fopen("A-small-attempt1.out", "w");

	if (!in || !out);

	int T;
	int testcase;

	fscanf(in, "%d ", &T);
	//fprintf(out, "Test Case : %d\n", T);
	for (testcase = 1; testcase <= T; testcase++) {
		// -------------------------------------------------- //
		// input
		// -------------------------------------------------- //
		fscanf(in, "%s", S);
		for (int i = 0; i < 26; i++) count[i] = 0;
		for (int i = 0; i < 10; i++) result[i] = 0;
		// -------------------------------------------------- //
		// start here
		// -------------------------------------------------- //
		int i = 0;
		for (i = 0; S[i] != '\0'; i++) count[S[i] - 'A']++;
		findRet(i);
		// -------------------------------------------------- //
		// output
		// -------------------------------------------------- //
		fprintf(out, "Case #%d: ", testcase);
		for (i = 0; i < 26; i++) {
			for (int j = 0; j < result[i]; j++) fprintf(out, "%d", i);
		}
		fprintf(out, "\n");
	}

	fclose(in);
	fclose(out);
}
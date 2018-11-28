#include <cstdio>
#include <cstring>

FILE *fi, *fo;
char S[105];
char buff[105];
int Answer;

void flip(int level) { // 0 base
	if (level < 0) {
//		fprintf(fo, "%d\n", level);
		return;
	}
	Answer++;
//	fprintf(fo, "%d [%s]", level, S);
	strncpy(buff, S, level+1);
	for (int i = 0; i <= level; i++) {
		if (buff[level - i] == '-') S[i] = '+';
		else S[i] = '-';
	}
//	fprintf(fo, "/[%s]\n", S);
}

int main() {
	//fi = fopen("sample.in", "r");
	fi = fopen("B-large.in", "r");
	//fi = fopen("B-small-attempt0.in", "r");
	fo = fopen("output.txt", "w");

	int T, N;
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
		fscanf(fi, "%s\n", S);
		N = strlen(S);
		Answer = 0;
		int flip_lv = -1;
		int fix_bot = N; // fix N-th level (0 base)
		while (fix_bot > 0) {
			// Step 1 : set fix_bot
			while (fix_bot > 0 && S[fix_bot - 1] == '+') fix_bot--;
			
			// Step 2 : find level to 1st flip
			flip_lv = -1;
			for (int i = 0; i<fix_bot; i++) {
				if (S[i] == '-') {
					flip_lv = i - 1;
					break;
				}
			}
//			fprintf(fo, "flip ");
			flip(flip_lv);
//			fprintf(fo, "fix  ");
			flip(fix_bot - 1);
		}
		fprintf(fo, "Case #%d: %d\n", t, Answer);

	}
	fclose(fi);
	fclose(fo);
	return 0;
}












/**************************

#include <cstdio>
#include <cstring>


int main() {
	//FILE *fi = fopen("sample.in", "r");
	FILE *fi = fopen("A-large.in", "r");
	//FILE *fi = fopen("A-small-attempt0.in", "r");
	FILE *fo = fopen("output.txt", "w");

	int T;
	fscanf(fi, "%d", &T);
	for (int t = 1; t <= T; t++) {
	}
	fclose(fi);
	fclose(fo);
	return 0;
}
****************************/
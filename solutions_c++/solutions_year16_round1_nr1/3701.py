#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <string>

using namespace std;

int main() {
	int testcase;
	char S[1010];
	string last = "";
	FILE *fi, *fo;
	fi = fopen("A-large.in", "r");
	fo = fopen("A1_out2.txt", "w");
	fscanf(fi, "%d", &testcase);
	for (int t = 1; t <= testcase; t++) {
		fscanf(fi, "%s", &S);
		if (S[0] > S[1]) {
			last = S[0];
			last += S[1];
		}
		else {
			last = S[1];
			last += S[0];
		}
		for (int i = 2; i < strlen(S); i++) {
			if (last[0] <= S[i]) {
				last = S[i] + last;
			}
			else {
				last = last + S[i];
			}
		}
		fprintf(fo, "Case #%d: %s\n", t,(char*)last.c_str());
	}
	fclose(fi);
	fclose(fo);
	return 0;
}
#include<stdio.h>
int chk[101], len = 0, result = 0;
int chks[200][101];
int main() {
	int t, n, i, j, k, l, cnt, temp;
	char inp[101];
	FILE *in, *ou;
	fopen_s(&in, "input.txt", "r");
	fopen_s(&ou, "output.txt", "w");
	fscanf_s(in, "%d\n", &t);
	for (l = 0; l < t; l++) {
		//fscanf_s(in, "%s", inp);
		fgets(inp, 101, in);
		for (i = 0; i < 100; i++) {
			if (inp[i] == 0 || inp[i] == '\n')
				break;
			chk[i] = (inp[i] == '-' ? 0 : 1);
			chks[0][i] = chk[i];
		}
		len = i;
		result = len + 1;
		cnt = 0;
		for (i = 0; i < len-1; i++) {
			if (chk[i] != chk[i + 1]) {
				for (j = 0; j < i+1; j++) {
					chk[j] = 1 - chk[j];
				}
				cnt++;
			}
		}
		if (chk[0] == 0)
			cnt++;


		
		fprintf(ou, "Case #%d: %d\n", l + 1, cnt);

	}

	return 1;
}
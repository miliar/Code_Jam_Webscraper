#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(){

	FILE *fi = fopen("B-large.in.txt", "r");
	FILE *fo = fopen("output.txt", "w");

	int N;

	fscanf(fi,"%d", &N);

	for (int i = 0; i < N; i++){
		char s[101] = { 0, };

		fscanf(fi,"%s", s);
		int len = strlen(s);
		int cnt = 0;
		for (int j = 1; j < len; j++){
			if (s[j] != s[j - 1])
				cnt++;
		}
		if (s[len-1] == '-')
			cnt++;
		fprintf(fo,"Case #%d: %d\n", i+1,cnt);
	}

	return 0;
}
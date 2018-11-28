#include <stdio.h>
#include <string.h>

FILE *in=fopen("B-large.in", "r");
FILE *out=fopen("output.txt", "w");

int main()
{
	int t;
	fscanf(in, "%d", &t);
	for (int tt=1; tt<=t; tt++){
		char A[999];
		int cnt=0;
		fscanf(in, "%s", A);
		fprintf(out, "Case #%d: ", tt);
		for (int i=1; i<strlen(A); i++){
			if (A[i-1]!=A[i]) cnt++;
		}
		if (A[strlen(A)-1]=='-') cnt++;
		fprintf(out, "%d\n", cnt);
	}
	return 0;
}

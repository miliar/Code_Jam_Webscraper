#include <stdio.h>
#include <string.h>

FILE *in=fopen("D-small-attempt1.in", "r");
FILE *out=fopen("output.txt", "w");

int main()
{
	int t;
	fscanf(in, "%d", &t);
	for (int tt=1; tt<=t; tt++){
		int a, b, c;
		fscanf(in, "%d %d %d", &a, &b, &c);
		fprintf(out, "Case #%d: ", tt);
		for (int i=1; i<=a; i++) fprintf(out, "%d ", i);
		fprintf(out, "\n");
	}
	return 0;
}

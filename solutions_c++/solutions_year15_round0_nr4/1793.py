#include <iostream>
#include <cstdio>

using namespace std;

int test;
int cnt = 1;
int x, r, c;
int main(){
	FILE *fi = fopen("D-small-attempt0.in", "r");
	FILE *fo = fopen("output.out", "w");

	fscanf(fi, "%d", &test);

	while (test--)
	{
		fscanf(fi, "%d%d%d", &x, &r, &c);
		if (x == 1)
		{
			fprintf(fo, "Case #%d: GABRIEL\n", cnt++);
			continue;
		}
		if (x == 2)
		{
			if ((r*c) & 1) fprintf(fo, "Case #%d: RICHARD\n", cnt++);
			else fprintf(fo, "Case #%d: GABRIEL\n", cnt++);
			continue;
		}
		if (x == 3)
		{
			if ((r*c) % 3 == 0 && r != 1 && c != 1) fprintf(fo, "Case #%d: GABRIEL\n", cnt++);
			else fprintf(fo, "Case #%d: RICHARD\n", cnt++);
			continue;
		}
		if (x == 4)
		{
			if (r*c == 12 || r*c == 16) fprintf(fo, "Case #%d: GABRIEL\n", cnt++);
			else fprintf(fo, "Case #%d: RICHARD\n", cnt++);
		}
	}
}
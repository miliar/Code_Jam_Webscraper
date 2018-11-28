#include <stdio.h>

char s[1002];
int max, n;

void init(FILE* ifp)
{
	n = 0;
	fscanf(ifp, "%d %s", &max, s);
	for (int i = 0; i <= max; ++i)
	{
		s[i] -= '0';
	}
}

void solve(void)
{
	int count = 0;
	for (int i = 0; i <= max; ++i)
	{
		if (s[i] > 0 && i > count)
		{
			n += i - count;
			count = i;
		}
		count += s[i];
	}
}

void printAns(int caseNum, FILE* ofp)
{
	fprintf(ofp, "Case #%d: %d\n", caseNum, n);
}

char * inName = "a.in";
char * outName = "a.out";

void test(int caseNum, FILE* ifp, FILE* ofp)
{
	init(ifp);
	solve();
	printAns(caseNum, ofp);
}

int testCaseN;
int main(void)
{
	FILE* ifp = fopen(inName, "rt");
	FILE* ofp = fopen(outName, "wt");
	fscanf(ifp, "%d", &testCaseN);
	for (int i = 1; i <= testCaseN; ++i)
	{
		test(i, ifp, ofp);
	}
	fclose(ifp);
	fclose(ofp);
}
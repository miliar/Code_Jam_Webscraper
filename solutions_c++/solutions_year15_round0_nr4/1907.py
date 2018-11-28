#include <stdio.h>


int ans[4][4][4] = {
	{
		{ 1, 1, 1, 1 },
		{ 1, 1, 1, 1 },
		{ 1, 1, 1, 1 },
		{ 1, 1, 1, 1 }
	},
	{
		{ 0, 1, 0, 1 },
		{ 1, 1, 1, 1 },
		{ 0, 1, 0, 1 },
		{ 1, 1, 1, 1 }
	},
	{
		{ 0, 0, 0, 0 },
		{ 0, 0, 1, 0 },
		{ 0, 1, 1, 1 },
		{ 0, 0, 1, 0 }
	},
	{
		{ 0, 0, 0, 0 },
		{ 0, 0, 0, 0 },
		{ 0, 0, 0, 1 },
		{ 0, 0, 1, 1 }
	},
};

char * inName = "d.in";
char * outName = "d.out";
FILE *ifp, *ofp;
int possible, x, r, c;
void init(void)
{
	fscanf(ifp, "%d %d %d", &x,&r,&c);
}

void solve(void)
{
	possible = ans[x - 1][r - 1][c - 1];
}

void printAns(int caseNum)
{
	fprintf(ofp, "Case #%d: ", caseNum);
	if (possible)
		fprintf(ofp, "GABRIEL\n");
	else
		fprintf(ofp, "RICHARD\n");
}

void test(int caseNum)
{
	init();
	solve();
	printAns(caseNum);
}

int testCaseN;
int main(void)
{
	ifp = fopen(inName, "rt");
	ofp = fopen(outName, "wt");
	fscanf(ifp, "%d", &testCaseN);
	for (int i = 1; i <= testCaseN; ++i)
	{
		test(i);
	}
	fclose(ifp);
	fclose(ofp);
}
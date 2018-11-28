#include <stdio.h>
int charTable[4][4] = { { 0, 1, 2, 3 },
{ 1, 0, 3, 2 },
{ 2, 3, 0, 1 },
{ 3, 2, 1, 0 }, };
int signTable[4][4] = { { 1, 1, 1, 1 },
{ 1, -1, 1, -1 },
{ 1, -1, -1, 1 },
{ 1, 1, -1, -1 }, };

char L[10003];
int ln, x;

char * inName = "c.in";
char * outName = "c.out";
FILE *ifp, *ofp;

int val, sign, index;
int possible;

void init(void)
{
	int tmp;
	index = 0;
	fscanf(ifp, "%d %d", &ln, &x);
	fscanf(ifp, "%s", L);
	for (int i = 0; i < ln; ++i)
	{
		L[i] -= 'h';
	}
	possible = 0;
}

int getNext(void)
{
	if (index >= ln*x)
		return -1;
	int ret = L[index%ln];
	++index;
	return ret;
}

void calc(int nextChar)
{
	sign *= signTable[val][nextChar];
	val = charTable[val][nextChar];
}

void solve(void)
{
	int nextChar;
	val = 0;
	sign = 1;
	while (val != 1 || sign != 1)
	{
		nextChar = getNext();
		calc(nextChar);
		if (nextChar < 0)
			return;
	}


	val = 0;
	sign = 1;
	while (val != 2 || sign != 1)
	{
		nextChar = getNext();
		calc(nextChar);
		if (nextChar < 0)
			return;
	}


	val = 0;
	sign = 1;
	while ((nextChar = getNext()) >= 0)
	{
		calc(nextChar);
	}
	if (val == 3 && sign == 1)
		possible = 1;
}

void printAns(int caseNum)
{
	fprintf(ofp, "Case #%d: ", caseNum);
	if (possible)
		fprintf(ofp, "YES\n");
	else
		fprintf(ofp, "NO\n");
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
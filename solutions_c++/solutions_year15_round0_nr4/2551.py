#include <iostream>
#include <cstdio>
#include <cstring>
#include <algorithm>

using namespace std;

#define MAXN 1002

char * win(int x, int r, int c)
{
	int rc = r * c;
	if (rc % x != 0) return "RICHARD";
	if (x == 1 || x == 2) return "GABRIEL";
	if (x == 3)
	{
		switch (rc)
		{
		case 3:
			return "RICHARD";
			break;
		case 6:
			if (r == 2 || r == 3) return "GABRIEL";
			else return "RICHARD";
			break;
		case 9:
			if (r == 3) return "GABRIEL";
			else return "RICHARD";
			break;
		case 12:
			if (r == 1 || r == 12) return "RICHARD";
			else return "GABRIEL";
			break;
		case 15:
			if (r == 1 || r == 15) return "RICHARD";
			else return "GABRIEL";
		default:
			break;
		}
	}
	if (x == 4)
	{
		switch (rc)
		{
		case 4:
		case 8:
			return "RICHARD";
			break;
		case 12:
			if (r == 3 || r == 4) return "GABRIEL";
			else return "RICHARD";
			break;
		case 16:
			if (r == 4) return "GABRIEL";
			else return "RICHARD";
		default:
			break;
		}
	}
}

int main()
{
	int n, cases;
	FILE *fin, *fout;

	fin = fopen("D-small-attempt3.in", "r");
	fout = fopen("out.txt", "w");

	fscanf(fin, "%d", &n);
	cases = 1;

	///////////// Code begins here /////////////////////
	int x, r, c;

	while (n--)
	{
		fscanf(fin, "%d %d %d", &x, &r, &c);
		fprintf(fout, "Case #%d: %s\n", cases++, win(x, r, c));
	}

	///////////// Code ends here /////////////////////

	fclose(fin);
	fclose(fout);

	return 0;
}

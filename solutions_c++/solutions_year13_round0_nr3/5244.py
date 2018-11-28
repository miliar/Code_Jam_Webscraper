
	#include <stdio.h>
	#include <string.h>
	#include <stdlib.h>
	#include <math.h>

	using namespace std;

	char buffer[64];

    char *getline (FILE *fp)
    {
        char *p;

		if (!fgets (buffer, sizeof(buffer), fp)) return NULL;

		p = strchr (buffer, '\n');
		if (p) *p = '\0';

		return buffer;
    }

	long double modulus (long double x, long double y)
	{
		long double r = x - (floorl(x / y) * y);
		if (r == y) r = 0;

		return r;
	}

	int isPalindrome (long double x)
	{
		int i = 0, j, y, z;

		while (1)
		{
			if (floorl(x / powl(10, i)) != 0)
				i++;
			else
				break;
		}

		while (i > 0)
		{
			if (modulus (x, 10) != floorl(x / powl(10, i-1)))
				return 0;

			x = floorl (modulus (x, powl(10, i-1)) / 10);
			i -= 2;
		}

		return 1;
	}

	long double fairSquares (long double A, long double B)
	{
		long double mink = ceill(sqrt(A));
		long double maxk = floorl(sqrt(B));

		long double m = 0;

		for (long double k = mink; k <= maxk; k++)
		{
			if (isPalindrome(k*k) && isPalindrome(k))
				m++;
		}

		return m;
	}

	void eatWhiteSpace (FILE *fp)
	{
		int ch;
		
		while (1) {
			ch = getc(fp);
			if (ch == EOF || ch > 32) break;
		}

		if (ch != EOF) ungetc(ch, fp);
	}

	int main (int argc, char *argv[])
	{
		int testCase, testCases;
		FILE *fp; char *line;
		int i, j, k;
		long double A, B;

		if (argc < 2)
		{
			printf ("Use: main <input-file>\n");
			return -1;
		}

		fp = fopen (argv[1], "rt");
		if (!fp) return -2;

		sscanf(getline(fp), "%u", &testCases);

		for (testCase = 1; testCase <= testCases; testCase++)
		{
			sscanf(getline(fp), "%Lf %Lf", &A, &B);
			printf ("Case #%u: %Lg\n", testCase, fairSquares(A, B));
		}

		fclose(fp);
		return 0;
	}

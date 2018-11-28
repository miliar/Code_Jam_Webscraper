#ifdef WIN32
#pragma warning(disable:4996)
#pragma warning(disable:4100)
#endif /* WIN32 */

#include <string.h>
#include <stdio.h>
#include <stdlib.h>

//#define TESTING

int main(int argc, char *argv[])
{
	int t = 0;
	int smax = 0;
	char ch;
	int k;
	int y;
	int total_so_far;
	int to_be_added;
#ifdef TESTING
	FILE *fp;
#endif

#ifdef TESTING
	fp = fopen(argv[1], "r");
#else
	fp = stdin;
#endif

	fscanf(fp, "%d", &t);

	for (int x = 0; x < t; x++)
	{
		fprintf(stdout, "Case #%d: ", x + 1);
		fscanf(fp, "%d", &smax);

		ch = fgetc(fp);
		if (ch == ' ')
		{
			y = 0;
			total_so_far = 0;

			for (k = 0; k <= smax; k++)
			{
				ch = fgetc(fp);
				if (total_so_far < k)
				{
					to_be_added = k - total_so_far;
					y += to_be_added;
					total_so_far += to_be_added;
				}

				total_so_far += ch - '0';
			}

			fprintf(stdout, "%d\n", y);
		}
		else
		{
			//Input format error
			break;
		}
	}

#ifdef TESTING
	fclose(fp);
#endif

	return 0;
}
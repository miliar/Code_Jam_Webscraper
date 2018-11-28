#ifdef WIN32
#pragma warning(disable:4996)
#endif

#include <stdio.h>
#include <string.h>

bool all_found(bool *pfound)
{
	bool all_found = true;

	for (int i = 0; i < 10; i++)
	{
		if (!pfound[i])
		{
			all_found = false;
			break;
		}
	}

	return all_found;
}

void find_digits(unsigned long long int n, bool *pfound)
{
	int mod;

	while (n > 0)
	{
		mod = n % 10;
		pfound[mod] = true;
		n /= 10;
	}
}

int main(int argc, char *argv[])
{
	bool found[10];
	FILE *fp;
	int t = 0;
	unsigned long long int n;
	unsigned long long int ni;
	int i;

#ifdef TESTING
	fp = fopen(argv[1], "r");
#else
	fp = stdin;
#endif

	fscanf(fp, "%d", &t);

	for (int ti = 0; ti < t; ti++)
	{
		fprintf(stdout, "Case #%d: ", ti + 1);
		fscanf(fp, "%llu", &n);
		if (n == 0)
		{
			fprintf(stdout, "INSOMNIA\n");
		}
		else
		{
			memset(found, 0, sizeof(found));
			i = 1;
			ni = n;
			find_digits(ni, found);
			while (!all_found(found))
			{
				i++;
				ni = n * i;
				find_digits(ni, found);
			}

			fprintf(stdout, "%llu\n", ni);
		}
	}

#ifdef TESTING
	fclose(fp);
#endif
}

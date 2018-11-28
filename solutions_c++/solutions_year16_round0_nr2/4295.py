#ifdef WIN32
#pragma warning(disable:4996)
#endif

#include <stdio.h>
#include <string.h>

int find_last_minus(const char *s, int len)
{
	int index = -1;

	for (int i = len - 1; i >= 0; i--)
	{
		if (s[i] == '-')
		{
			index = i;
			break;
		}
	}

	return index;
}

int get_leading_plus_count(const char *s, int end_index)
{
	int count = 0;

	for (; count <= end_index; count++)
	{
		if (s[count] == '-')
		{
			break;
		}
	}

	return count;
}

inline char flip_char(char ch)
{
	if (ch == '-')
	{
		return '+';
	}
	else
	{
		return '-';
	}
}

void flip(char *s, int last_index)
{
	char src, dest;

	for (int i = 0; i <= last_index / 2; i++)
	{
		src = flip_char(s[i]);
		dest = flip_char(s[last_index - i]);
		s[i] = dest;
		s[last_index - i] = src;
	}
}

int main(int argc, char *argv[])
{
	FILE *fp;
	int t = 0;
	char s[101];
	int len;
	int last_minus_index;
	int leading_plus_count;
	int maneuvres;

#ifdef TESTING
	fp = fopen(argv[1], "r");
#else
	fp = stdin;
#endif

	fscanf(fp, "%d", &t);

	for (int ti = 0; ti < t; ti++)
	{
		fprintf(stdout, "Case #%d: ", ti + 1);
		fscanf(fp, "%s", s);

		maneuvres = 0;
		len = strlen(s);
		last_minus_index = find_last_minus(s, len);
		while (last_minus_index > -1)
		{
			leading_plus_count = get_leading_plus_count(s, last_minus_index);
			if (leading_plus_count > 0)
			{
				memset(s, '-', leading_plus_count);
				maneuvres++;
			}

			flip(s, last_minus_index);
			maneuvres++;

			last_minus_index = find_last_minus(s, last_minus_index);
		}

		fprintf(stdout, "%d\n", maneuvres);
	}

#ifdef TESTING
	fclose(fp);
#endif
}

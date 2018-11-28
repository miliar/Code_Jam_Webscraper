#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>
#include <string.h>

int
	T,
   fscount = 0;

__int64
   fs[1000];

__int64 pow(__int64 b, __int64 e)
{
   __int64
      result = 1;

   for (__int64 i = 0; i < e; i++)
      result *= b;

   return result;
}

int is_palindrome(const char s[101])
{
   for (int i = 0, size = strlen(s), max = (size + 1 / 2); i < max; i++)
      if (s[i] != s[size - 1 - i])
         return (0);

   return (1);
}

void form_palindrome(const char in[101], char out[101], int skiplast)
{
   int
      size = strlen(in),
      max  = size * 2 - skiplast;

   for (int i = 0; i < size; i++)
      {
      out[i] = in[i];
      out[max - 1 - i] = in[i];
      }

   out[max] = 0;
}

void add_fs_nums(int digits, int skiplast)
{
   __int64
      min = pow(10, digits - 1),
      max = pow(10, digits),
      pal,
      sq;

   char
      si[101],
      spal[101],
      ssq[101];

   for (__int64 i = min; i < max; i++)
      {
      sprintf(si, "%llu", i);
      form_palindrome(si, spal, skiplast);
      sscanf(spal, "%llu", &pal);
      sq = pal * pal;
      sprintf(ssq, "%llu", sq);
      if (is_palindrome(ssq))
         fs[fscount++] = sq;
      }
}

int main(int argc, char *argv[])
{
   for (int i = 1; i < 3; i++)
      {
      add_fs_nums(i, 1);
      add_fs_nums(i, 0);
      }
   add_fs_nums(4, 1);

   FILE
	   *fpi = fopen("C-small.in", "r"),
	   *fpo = fopen("C-small.out", "w");

	fscanf(fpi, "%d", &T);
	for (int i = 0; i < T; i++)
		{
		__int64
         A,
         B,
         result = 0;

		fscanf(fpi, "%llu", &A);
		fscanf(fpi, "%llu", &B);

		for (int j = 0; j < fscount; j++)
         {
         if (fs[j] < A)
            continue;

         if (fs[j] > B)
            break;

         result++;
         }

      fprintf(fpo, "Case #%d: %llu\n", i + 1, result);
		}

	fclose(fpi);
	fclose(fpo);
	return 0;
}

#include <stdio.h>
#include <malloc.h>

FILE *fpIn;
FILE *fpOut;
int ans1;
int ans2;
int **grid1;
int **grid2;

void process()
{
   int *checkList = (int *)calloc(16, sizeof(int *));
   
   for (int i = 0; i < 4; ++i)
   {
      checkList[grid1[ans1 - 1][i] - 1] += 1;
   }

   for (int i = 0; i < 4; ++i)
   {
      checkList[grid2[ans2 - 1][i] - 1] += 1;
   }

   int numberOf1 = 0;
   int numberOf2 = 0;
   int ans = -1;

   for (int i = 0; i < 16; ++i)
   {
      if (checkList[i] == 1)
      {
         ++numberOf1;
      }
      else if (checkList[i] == 2)
      {
         ++numberOf2;
         ans = i + 1;
      }
   }

   if (numberOf2 == 0)
   {
      fprintf(fpOut, "Volunteer cheated!");
   }
   else if (numberOf2 == 1)
   {
      fprintf(fpOut, "%d", ans);
   }
   else if (numberOf2 > 1)
   {
      fprintf(fpOut, "Bad magician!");
   }
}

int main()
{
   int T;
   int tmp;

   grid1 = (int **)malloc(4 * sizeof(int **));
   for (int i = 0; i < 4; ++i)
      grid1[i] = (int *)malloc(4 * sizeof(int));

   grid2 = (int **)malloc(4 * sizeof(int **));
   for (int i = 0; i < 4; ++i)
      grid2[i] = (int *)malloc(4 * sizeof(int *));

   fpIn = fopen("c:\\gcj\\in_c", "r");
   fpOut = fopen("c:\\gcj\\out_c", "w");
   
   fscanf(fpIn, "%d\n", &T);

   for (int i = 0; i < T; ++i)
   {
      fscanf(fpIn, "%d\n", &ans1);

      for (int j = 0; j < 4; ++j)
      {
         for (int k = 0; k < 4; ++k)
         {
            fscanf(fpIn, "%d\n", &(grid1[j][k]));
         }
      }

      fscanf(fpIn, "%d\n", &ans2);

      for (int j = 0; j < 4; ++j)
      {
         for (int k = 0; k < 4; ++k)
         {
            fscanf(fpIn, "%d\n", &(grid2[j][k]));
         }
      }

      fprintf(fpOut, "Case #%d: ", i + 1);

      process();

      fprintf(fpOut, "\n");
   }

   return 0;
}
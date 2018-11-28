#include <stdio.h>
#include <stdlib.h>


int main()
{
   int k;
   int n_case;
   int n_sMax;
   FILE* file, *output;

   file = fopen("A-large.in", "r");
   output = fopen("output.txt", "w");

   fscanf(file, "%d", &n_case);

   for( k = 1; k <= n_case; k++)
   {
      int i;

      //read the test data input
      fscanf(file, "\n%d ", &n_sMax);
      int* pS = new int [n_sMax+1];

      for(i = 0; i <= n_sMax; i++)
      {
         char ch;
         fscanf(file, "%c",  &ch);
         pS[i] = atoi(&ch);
      }

      //now loop & calculate the extra people
      int cnt = 0;
      int extra = 0;
      int prev = 0;
      for(i = 1; i <= n_sMax;i++)
      {
         prev += pS[i-1];
         if(pS[i]==0)
            continue;
         cnt = prev+extra;
         if(cnt >= i)
            continue;
         extra += i-cnt;
      }

      delete []pS;
      fprintf(output, "Case #%d: %d\n", k, extra);
   }
   fclose(output);
   fclose(file);
}
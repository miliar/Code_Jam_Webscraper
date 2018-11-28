#include<stdio.h>
int main(void)
{
	double A, B, C, min, now, temp;
   int T, next;
   
   FILE *p;
   FILE *p2;
   p = fopen("B-large.in", "rt");
   p2 = fopen("output.txt", "wt");
   fscanf(p, "%d", &T);
   for (int i = 0; i < T; i++)
   {
      fscanf(p, "%lf %lf %lf", &A, &B, &C);
      next = 1;
      min = C / 2;
      now = 1.0 / 2;
      temp = (C / (2 + next*B)) + (A * now);
      while (temp < min)
      {
         min = temp;
         now = now + (1 / (2 + next*B));
         next++;
         temp = (C / (2 + next*B)) + (A * now);
      }
      fprintf(p2, "Case #%d: %.7lf\n", i + 1, min);
   }
   fclose(p);
   fclose(p2);
 
   return 0;
}
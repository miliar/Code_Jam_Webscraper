#include <stdio.h>
#include <iostream>

void tictactoetomek(FILE*);

void main(int argv, char** argc)
{
   int n;
   FILE* file = fopen(argc[1], "r");
   fscanf(file, "%d\n", &n);
   for(int i = 0; i < n; i++)
   {
      printf("Case #%d: ", i+1);
      tictactoetomek(file);
      printf("\n");
   }
   fclose(file);
}
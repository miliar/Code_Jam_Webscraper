#include <stdio.h>
char table[100][100] = {0};

void process_lawn_mover
(
   FILE *fp,
   unsigned short n,
   unsigned short m,
   int tcase)
{
  unsigned short i = 0;
  unsigned short j = 0;
  
  unsigned short x = 0;
  unsigned char check_col = 0;
  
  for (i = 0 ; i < n; i++)
  {
      for (j = 0; j < m; j++)
      {
          
         // row wise
         for (x = 0; x < m; x++)
         {
             if (x == j)
             continue;
             
             if (table[i][x] > table[i][j])
             {
               check_col = 1;             
             }                 
         } 

         if (check_col == 0)
         continue;  
         // column wise
         for (x = 0; x < n; x++)
         {
             if (x == j)
             continue;
             
             if (table[x][j] > table[i][j])
             {
                 // not correct pattern.. print
                 fprintf(fp, "Case #%d: NO\n", tcase);       
                 return;             
             }                 
         } 
                       
         check_col = 0;                       
      }     
      
   }
      
   // correct pattern print yes  
                 fprintf(fp, "Case #%d: YES\n", tcase);            
  return;   
}

int main()
{
  unsigned short num_test_case = 0;  
  unsigned short i = 0;
  unsigned short j = 0;
  unsigned short k = 0;
  unsigned short m = 0;
  unsigned short n = 0; 
  FILE *fp1;
  FILE *fp2;
  fp1=fopen("c:\\input.txt", "r");
  fp2=fopen("c:\\output.txt", "w");
  
  fscanf(fp1,"%hd", &num_test_case);
  
  for (i = 0; i < num_test_case; i++)
  {
      fscanf(fp1,"%hd %hd", &n, &m);

      for (j = 0; j < n; j++)
      {
         for (k = 0; k < m; k++)           
         {
          fscanf(fp1, "%hd", &table[j][k]);  
            
          printf("%hd",table[j][k]);
         }
         printf("\n");

      }   
      
      process_lawn_mover(fp2, n, m, i+1);
      printf("\n");

  }
  system("PAUSE");
  return 0; 
}

#include <stdio.h>

#define MAX_TEST_CASE   1000

char tic_toe_table[4][4] = {0};


enum result
{
     
     no_result = 0,
     x_win = 1,
     o_win = 2,
     draw = 3
};

void process_tic_tac(char (*input)[4],  FILE *fp, int tcase)
{
   short i = 0;
  short j = 0;
  short k = 0;
  unsigned char res = draw;
  unsigned char check_flag = 3;
  // check rows
  for(i = 0; i <4;i++)
  {
        check_flag = 3;  
        for (j = 0; j < 4; j++)
        {
           if (input[i][j] == '.')
           {
             res =  no_result;
             check_flag = 0;
             break;                
           } 
           
           if (input[i][j] == 'X')
           {
              check_flag &= 1;
           }  
           else if (input[i][j] == 'O')
           {
                
                 check_flag &= 2;  
                
           }
           else // T
           {     
               check_flag &= 3;      
           }
        }
        if (check_flag != 0)
        {
           if (check_flag == 1)
           {
              // print 1 
              fprintf(fp, "Case #%d: X won\n", tcase);              
           }          
           else
           {
              // print 2    
              fprintf(fp, "Case #%d: O won\n", tcase);               
              
           }
           return;
                   
        }
  }  
  
  // check columns
  // check rows
  for(j = 0; j <4;j++)
  {
        check_flag = 3;  
        for (i = 0; i < 4; i++)
        {
           if (input[i][j] == '.')
           {
             res =  no_result;
             check_flag = 0;
             break;                
           } 
           
           if (input[i][j] == 'X')
           {
              check_flag &= 1;
           }  
           else if (input[i][j] == 'O')
           {
                
                 check_flag &= 2;  
                
           }
           else // T
           {     
               check_flag &= 3;      
           }
        }
        if (check_flag != 0)
        {
           if (check_flag == 1)
           {
              // print 1     
              fprintf(fp, "Case #%d: X won\n", tcase);                         
           }          
           else
           {
              // print 2    
              fprintf(fp, "Case #%d: O won\n", tcase);               
           }
           return;
                   
        }
  }  
  check_flag = 3;
   for (i = 0; i < 4; i++)
   {
           if (input[i][i] == '.')
           {
             res =  no_result;
             check_flag = 0;
             break;                
           } 
           
           if (input[i][i] == 'X')
           {
              check_flag &= 1;
           }  
           else if (input[i][i] == 'O')
           {
                
                 check_flag &= 2;  
                
           }
           else // T
           {     
               check_flag &= 3;      
           }

 
   }

       if (check_flag != 0)
        {
           if (check_flag == 1)
           {
              // print 1          
              fprintf(fp, "Case #%d: X won\n", tcase);      
           }          
           else
           {
              // print 2    
              fprintf(fp, "Case #%d: O won\n", tcase);               
           }
           return;
                   
        }
  check_flag = 3;
   for (i = 0; i < 4; i++)
   {
           if (input[i][3-i] == '.')
           {
             res =  no_result;
             check_flag = 0;
             break;                
           } 
           
           if (input[i][3-i] == 'X')
           {
              check_flag &= 1;
           }  
           else if (input[i][3-i] == 'O')
           {
                
                 check_flag &= 2;  
                
           }
           else // T
           {     
               check_flag &= 3;      
           }


   }

        if (check_flag != 0)
        {
           if (check_flag == 1)
           {
              // print 1               
              fprintf(fp, "Case #%d: X won\n", tcase);               
           }          
           else
           {
              // print 2    
              fprintf(fp, "Case #%d: O won\n", tcase);               
           }
           return;
                   
        }
   if (res == draw)
   {
              fprintf(fp, "Case #%d: Draw\n", tcase);            
   }
   else
   {
              fprintf(fp, "Case #%d: Game has not completed\n",tcase);                   
       
   }

     
  return;     
}

int main()
{
  unsigned short num_test_case = 0;  
  unsigned short i = 0;
  unsigned short j = 0;
  unsigned short k = 0;
  char temp[5] = {0};
  FILE *fp1;
  FILE *fp2;
  fp1=fopen("c:\\input.txt", "r");
  fp2=fopen("c:\\output.txt", "w");
  
  fscanf(fp1,"%hd", &num_test_case);
  
  for (i = 0; i < num_test_case; i++)
  {
      for (j = 0; j < 4; j++)
      {
         fscanf(fp1, "%s", temp); 

         for (k = 0; k < 4; k++)           
         {
          tic_toe_table[j][k] = temp[k];   
          printf("%c",tic_toe_table[j][k]);
         }
         temp[k] = '\0';
         printf("\n");

      }   
      printf("\n");
      process_tic_tac(tic_toe_table,fp2, i + 1);
//      fscanf(fp1, "%s", temp); 
  }
/*
  for (i = 0; i < num_test_case; i++)
  {
     process_tic_tac(tic_toe_table[i],fp2, i + 1);
  }
*/  
  fclose(fp1);
  fclose(fp2);
//  system("PAUSE");
  return 0;
}

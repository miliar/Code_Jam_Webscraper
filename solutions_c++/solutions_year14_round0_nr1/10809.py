#include<stdio.h>

int main()
{
     //Variable declaration and instantiation
     FILE *fp1 = fopen("C:\\Users\\Jagadeesh\\Downloads\\A-small-attempt0.txt", "r");
     FILE *fp2 = fopen("C:\\Users\\Jagadeesh\\Desktop\\Code Jam\\Output.txt", "w");
     
     int test_cases, first_ans, second_ans, count, card_num, case_num;
     int first_arr[4][4], second_arr[4][4];
     int i = 0, j = 0;
     
     //Read input file
     fscanf(fp1, "%d", &test_cases);
     
     for(case_num = 0; case_num < test_cases; case_num++)
     {
     		count = 0;
             fscanf(fp1, "%d", &first_ans);
             
             for(i = 0; i < 4; i++)
             {
             	for(j = 0; j < 4; j++)
             	{
                     fscanf(fp1, "%d", &first_arr[i][j]);
                }
             }
             
             fscanf(fp1, "%d", &second_ans);
             
             for(i = 0; i < 4; i++)
             {
             	for(j = 0; j < 4; j++)
             	{
                     fscanf(fp1, "%d", &second_arr[i][j]);
                }
             }
             
             //Search for appropriate card
             for(i = 0; i < 4; i++)
             {
                   for(j = 0; j < 4; j++)
                   {
                         if(first_arr[first_ans - 1][i] == second_arr[second_ans - 1][j])
                         {
                                         count ++;
                                         card_num = first_arr[first_ans - 1][i];
                         }
                   }      
             }
             
             //Print the output
             fprintf(fp2, "Case #%d: ", case_num + 1);
             if(count == 0)
                      fprintf(fp2, "Volunteer cheated!\n");
             else if(count == 1)
                           fprintf(fp2, "%d\n", card_num);
             else
                           fprintf(fp2, "Bad magician!\n");
     }
     return 0;
}

/* 
 * File:   main.cpp
 * Author: Dayanand
 *
 * Created on 13 April 2013, 08:04
 */

#include <cstdlib>
#include<stdio.h>
using namespace std;
char a[4][4];
/*
 * 
 */

bool FindwhoWon(char c)
{
    int i = 0;
    int j =0;
    for(j = 0;j<4;j++)
    {
      if((a[i][j] == c || a[i][j] == 'T') &&
        (a[i+1][j] == c || a[i+1][j] == 'T') &&
        (a[i+2][j] == c || a[i+2][j] == 'T') &&
        (a[i+3][j] == c || a[i+3][j] == 'T'))
      {
           return true;
       }
     }
    i = 0;
    j =0;
    for(j = 0;j <4 ; j++)
    {
      if((a[j][i] == c || a[j][i] == 'T') &&
        (a[j][i+1] == c || a[j][i+1] == 'T') &&
        (a[j][i+2] == c || a[j][i+2] == 'T') &&
        (a[j][i+3] == c || a[j][i+3] == 'T'))
         {
            return true;
         }
     }
    i=0,j=0;
    if((a[j][i] == c || a[j][i] == 'T') &&
        (a[j+1][i+1] == c || a[j+1][i+1] == 'T') &&
        (a[j+2][i+2] == c || a[j+2][i+2] == 'T') &&
        (a[j+3][i+3] == c || a[j+3][i+3] == 'T'))
     {
            return true;
      }
    i = 0;j = 3;
     if((a[i][j] == c || a[i][j] == 'T') &&
        (a[i+1][j-1] == c || a[i+1][j-1] == 'T') &&
        (a[i+2][j-2] == c || a[i+2][j-2] == 'T') &&
        (a[i+3][j-3] == c || a[i+3][j-3] == 'T'))
      {
           return true;
       }
     
    return false;
}

int FindtheResult()
{
    int result = 0;
   if(FindwhoWon('X'))
      return 1;
   
       
    if(FindwhoWon('O'))
        return 2;
    
    for(int i = 0; i< 4;i++)
      for(int j = 0;j<4;j++)
      {
          if(a[i][j] == '.')
          { 
              return 3;
          }
       }
    return 0;
}
int main(int argc, char** argv) {
    int no_of_test_cases;
    freopen("tictactoe.txt" ,"r+",stdin);
    freopen("tictactoe_out.txt" ,"w+",stdout);
    scanf("%d\n",&no_of_test_cases);
    for(int i=0;i<no_of_test_cases;i++)
    {
        
        for(int j = 0;j<4;j++)
        {
            for(int k = 0;k<4;k++)
            {
                scanf("%c",&a[j][k]);
            }
            scanf("\n");
        }
        int result = FindtheResult();
        if(result == 0)
            printf("Case #%d: Draw",i+1);
        else if(result == 1)
            printf("Case #%d: X won",i+1);    
        else  if(result == 2)
            printf("Case #%d: O won",i+1);
        else 
            printf("Case #%d: Game has not completed",i+1);
        
        printf("\n");
        
    }
    return 0;
}


// CodeJam_A.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <stdio.h>
#include <iostream>
#include <math.h>

int FindSol(int P1[], int P2[])
{
    int match=0;
    int i;
    int check1=0, check2=0, test=1, check;
    
    
    for (i=0; i < 4; i++)
    {
        test = test << P1[i];
        check1 = check1 | test ;
        test = 1;    
    }    
    
    for (i=0; i<4; i++)
    {
        test = test << P2[i];
        check2 = check2 | test;
        test = 1;    
    }
    
    check = check1 & check2;
    
    while (check != 0)
    {
          match = match + check%2;
          check = check/2;      
    }
    
    if (match == 0)
       return 0; // V.C
       
    if (match == 1)
    {
       check = check1 & check2;
       match = 0;
       while (check != 0)
       {
             check = check/2;
             match++;      
       }
       return match-1;
    }
    
    if (match > 1)
    {
       return -1;  // B.M         
    }
}

void PrintBoard(int board[][4])
{
	int i,j;
	for (i=0;i<4;i++)
	{
		for (j=0;j<4;j++)
		{
			printf("%d ", board[i][j]);
		}
		printf("\n");
	}
	printf("\n");
}


int main ()
{
    int t, row1, row2, match=0, T;
    int A[4][4], B[4][4];
    int i,j;
    int P1[4], P2[4];
    
	errno_t err;

    FILE *ip ;
	err = fopen_s(&ip,"A-small-attempt0.txt", "r");

	errno_t errOp;
	FILE *op;
	errOp = fopen_s(&op,"outputSmall.txt","w+");

    fscanf_s(ip,"%d", &T);
    
    for (t=1; t<=T; t++)
    {
           fscanf_s(ip, "%d", &row1);
           row1--;

           for (i=0; i<4; i++)
           {
               for(j=0;j<4;j++)
               {
                   fscanf_s(ip,"%d", &A[i][j]);                
               }    
           }
           

           for (i=0; i<4;i++)
           {
               P1[i] = A[row1][i];    
           }
           
           fscanf_s(ip, "%d", &row2);
           row2--;

           for (i=0; i<4; i++)
           {
               for(j=0;j<4;j++)
               {
                   fscanf_s(ip,"%d", &B[i][j]);                
               }    
           }
           
		  // PrintBoard(A); PrintBoard(B);

           for (i=0; i<4;i++)
           {
               P2[i] = B[row2][i];    
           }           
           
           match = FindSol(P1,P2);
           
           if(match == 0)
           {
            fprintf_s(op,"Case #%d: Volunteer cheated!\n", t);
           }
           
           else if (match == -1)
           {
            fprintf_s(op,"Case #%d: Bad magician!\n", t);     
           }
           
           else
           {
            fprintf_s(op,"Case #%d: %d\n", t,match);    
           }
    }
    
    system("PAUSE");
    return 0;
}

#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    long long X;
    long long R;
    long long C;
    int step = 0;
    int size;
    char str[10000];
    char map[5][5];
/*---------*/  

/*
int sep(int low, int high)
{
    int i;
    int minutes = 0;
    
    for(i = low; i <= high; i ++)
    {
        if((i & 1) != 0)
        {
            pieNum[i/2 + 1] += pieNum[i];
            pieNum[i/2] += pieNum[i];
            minutes += pieNum[i];
            pieNum[i] = 0;
        }
        else
        {
            pieNum[i/2] += pieNum[i]*2;
            minutes += pieNum[i];            
            pieNum[i] = 0;
        }
    }
    printf("minutes %d\n", minutes);
    
    return minutes;
} 


int count()
{
    int i, j;
    int sum;
    int result = 0;
        
    for(i = maxPie; i >= 0; i --)
    {
        if(pieNum[i] == 0)
            continue;
            
        sum = 0;
        printf("i %d ceil+1 %f\n", i, ceil(((double)i)/2.0)+1);
        for(j = ceil(((double)i)/2.0)+1; j <= i; j++)
        {
            sum += pieNum[j];
        }
        
        if((int)(i/2) > sum)
        {
            result += sep(ceil(((double)i)/2.0)+1, i);
        }
        else
            return result + i;
    }
    
    return result;
}
*/



int main(int argc, char *argv[])
{

    char *inFileName = "D.in";
    char *outFileName = "D.out";
    long long i, j, k;
    int group;
    int result;
/*---------*/    
    FILE * pInFile, *pOutFile;
    

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");


    

    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {
        memset(str, 0, sizeof(str));
        fscanf(pInFile, "%I64d %I64d %I64d\n", &X, &R, &C);
        printf("X: %I64d, R: %I64d, R: %I64d\n", X, R, C);
        result = 0;

        switch(X)
        {
            case 1:
                result = 0;
                break;
            case 2:
                if((R*C) %2 == 0)
                    result = 0;
                else
                    result = 1;
                break;
            case 3:
                if((R*C) %3 == 0 && (R >= 2) && (C >= 2))
                    result = 0;
                else
                    result = 1;
                break;
            case 4:
                if((R*C) %4 == 0 && (R >= 3) && (C >= 3))
                    result = 0;
                else
                    result = 1;
                break;
            default:
                break;
        }

        if(result == 0)
            fprintf(pOutFile, "Case #%d: GABRIEL\n", i+1);
        else
            fprintf(pOutFile, "Case #%d: RICHARD\n", i+1);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




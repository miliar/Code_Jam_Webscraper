#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int L, X;
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

    char *inFileName = "C.in";
    char *outFileName = "C.out";
    int i, j, k;
    int group;
    int ans1, ans2;
/* Local Variables*/    
    //int A, N;
    int result;
    int preChar, nowChar;
    int sign = 1;
/*---------*/    
    FILE * pInFile, *pOutFile;
    

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");

    map[1][1] = 1;
    map[1][2] = 2;
    map[1][3] = 3;
    map[1][4] = 4;
    map[2][1] = 2;
    map[2][2] = -1;
    map[2][3] = 4;
    map[2][4] = -3;
    map[3][1] = 3;
    map[3][2] = -4;
    map[3][3] = -1;
    map[3][4] = 2;
    map[4][1] = 4;
    map[4][2] = 3;
    map[4][3] = -2;
    map[4][4] = -1;
    

    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {
        memset(str, 0, sizeof(str));
        fscanf(pInFile, "%d %d\n", &L, &X);
        printf("L: %d, X: %d\n", L, X);
        fscanf(pInFile, "%s\n", str);
        //printf("%s\n", str);
        preChar = 1;
        step = 0;
        sign = 1;
        for(j =0; j < X; j ++)
        {
            for(k = 0; k < L; k ++)
            {
                nowChar = str[k] - 'i' + 2;
                preChar = map[preChar][nowChar];
                if(preChar < 0)
                {
                    sign *= -1;
                    preChar *= -1;
                }
                //printf("(%d)->%d", nowChar, preChar*sign);
                switch(step)
                {
                    case 0:
                        if(preChar==2)
                        {
                            step ++;
                        }
                        break;
                    case 1:
                        if(preChar==4)
                            step ++;
                        break;
                    default:
                        break;
                }
            }
        }
        if(preChar == 1 && sign == -1)
            step ++;
        printf("\nstep %d\n", step);
        if(step == 3)
            fprintf(pOutFile, "Case #%d: %s\n", i+1, "YES");
        else
            fprintf(pOutFile, "Case #%d: %s\n", i+1, "NO");
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




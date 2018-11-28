#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int ans1, ans2;
    int num;
    int pie;
    int pieNum[10];
    int maxPie, secondPie;
    int result;
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

int count()
{
    int i, j;
    int time = 0;
    int minTime = 1000;
    int localPieNum[10];
    
    memcpy(localPieNum, pieNum, sizeof(pieNum));
        
    for(i = 9; i > 0; i--)
    {
        if(pieNum[i] == 0)
            continue;

        if(minTime > time + i)
            minTime = time +i;

        if(i&1 == 1)
        {
            for(j = 0; j <=i-1; j++)
            {
                pieNum[j] = pieNum[j+1];
            }
            time+=1;
        }
        else
        {
            pieNum[i/2] += pieNum[i];
            pieNum[i/2] += pieNum[i];
            time += pieNum[i];
        }
        
    }
    
    if(localPieNum[9] != 0)
    {
        time = 0;
        localPieNum[3] += 3*localPieNum[9];
        time+=2*localPieNum[9];
        for(i = 8; i > 0; i--)
        {
            if(localPieNum[i] == 0)
                continue;

            if(minTime > time + i)
                minTime = time +i;

            if(i&1 == 1)
            {
                for(j = 0; j <=i-1; j++)
                {
                    localPieNum[j] = localPieNum[j+1];
                }
                time+=1;
            }
            else
            {
                localPieNum[i/2] += localPieNum[i];
                localPieNum[i/2] += localPieNum[i];
                time += localPieNum[i];
            }
        }
    }
    
    return minTime;
}


int main(int argc, char *argv[])
{

    char *inFileName = "B.in";
    char *outFileName = "B.out";
    int i, j, k;
    int group;
    int ans1, ans2;
/* Local Variables*/    
    //int A, N;
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
        memset(pieNum, 0, sizeof(pieNum));
        maxPie = secondPie = 0;
        fscanf(pInFile, "%d\n", &num);
        printf("D: %d\n", num);
        for(j =0; j < num; j ++)
        {
            fscanf(pInFile, "%d", &pie);
            printf("%d", pie);
            pieNum[pie]++;
            if(pie > maxPie)
            {
                maxPie = pie;
            }
        }
        printf("\n");
        result = count();
          
        fprintf(pOutFile, "Case #%d: %d\n", i+1, result);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




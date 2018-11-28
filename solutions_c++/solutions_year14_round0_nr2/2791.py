#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    double cost, gain, target;
/*---------*/  


double genResult(void)
{
    double currentGain = 2.0;
    double minTime, newMinTime, usedTime;
    
    usedTime = 0;
    while(1)
    {
        minTime = target / currentGain;
        newMinTime = cost/currentGain + target/(currentGain+gain);
        if(minTime <= newMinTime)
            return usedTime+minTime;
        else
        {
            usedTime+=cost/currentGain;
            currentGain+= gain;
        }
    }
}


int main(int argc, char *argv[])
{

    char *inFileName = "B-large.in";
    char *outFileName = "B-large.out";
    int i, j, k;
    int group;
    int num1, num2;
/* Local Variables*/    
    //int A, N;
    double result;
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
         
          fscanf(pInFile, "%lf %lf %lf", &cost, &gain, &target);
          //printf("str %s val %d\n", str, minLen);
          printf("%lf %lf %lf\n", cost, gain, target);

          result = genResult();
          
          fprintf(pOutFile, "Case #%d: %.7lf\n", i+1, result);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int ans1, ans2;
    int num;
    char person[1500];
    
/*---------*/  




int count()
{
    int i = 0, currP = 0, result = 0;
    
    currP = person[0]-'0';
    
    for(i = 1; i <= num; i ++)
    {
        if(currP < i)
        {
            result += (i - currP);
            currP +=  (i - currP);
        }
        currP += person[i]-'0';
    }
    
    return result;
}


int main(int argc, char *argv[])
{

    char *inFileName = "A-large.in";
    char *outFileName = "A-large.out";
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
          fscanf(pInFile, "%d %s\n", &num, person);
          printf("%d %s\n", num, person);
          result = count();
          
          fprintf(pOutFile, "Case #%d: %d\n", i+1, result);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




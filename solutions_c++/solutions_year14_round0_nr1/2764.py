#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int ans1, ans2;
    int card1[4], card2[4], tmp[4];
    
/*---------*/  




int compare(int *ans)
{
    int i = 0, j, match = 0;
    
    for(i = 0; i < 4; i ++)
    {
        for(j = 0; j < 4; j ++)
        {
            if(card1[i] == card2[j])
            {
                match ++;
                *ans = card1[i];
            }
        }
    }
    
    return match;
}


int main(int argc, char *argv[])
{

    char *inFileName = "A-small-attempt0.in";
    char *outFileName = "A-small-attempt0.out";
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
         
          fscanf(pInFile, "%d", &ans1);
          //printf("str %s val %d\n", str, minLen);
          for(j =0; j <4; j ++)
          {
                if(j+1 == ans1)
                    fscanf(pInFile, "%d %d %d %d", &card1[0], &card1[1], &card1[2], &card1[3]);
                else
                    fscanf(pInFile, "%d %d %d %d", &tmp[0], &tmp[1], &tmp[2], &tmp[3]);
          }
          
          fscanf(pInFile, "%d", &ans2);
          //printf("str %s val %d\n", str, minLen);
          for(j =0; j <4; j ++)
          {
                if(j+1 == ans2)
                    fscanf(pInFile, "%d %d %d %d", &card2[0], &card2[1], &card2[2], &card2[3]);
                else
                    fscanf(pInFile, "%d %d %d %d", &tmp[0], &tmp[1], &tmp[2], &tmp[3]);
          }

          result = compare(&k);
          
          if(result == 0)
            fprintf(pOutFile, "Case #%d: Volunteer cheated!\n", i+1);
          else if(result == 1)
            fprintf(pOutFile, "Case #%d: %d\n", i+1, k);
          else
            fprintf(pOutFile, "Case #%d: Bad magician!\n", i+1);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




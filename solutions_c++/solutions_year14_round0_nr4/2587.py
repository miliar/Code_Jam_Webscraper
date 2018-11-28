#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;

int numWood;
double NWood[1000], KWood[1000];


void sort()
{
	int i, j;
    double smallVal, tmp;
    int smallIdx;
	
	for(i=0; i< numWood; i ++)
	{
        smallVal = NWood[i];
        smallIdx = i;
        for(j=i+1; j<numWood; j++)
        {
            if(smallVal > NWood[j])
            {
                smallVal=NWood[j];
                smallIdx=j;
            }
        }
        tmp = NWood[i];
        NWood[i] = NWood[smallIdx];
        NWood[smallIdx] = tmp;
    }
        
    for(i=0; i< numWood; i ++)
	{
        smallVal = KWood[i];
        smallIdx = i;
        for(j=i+1; j<numWood; j++)
        {
            if(smallVal > KWood[j])
            {
                smallVal=KWood[j];
                smallIdx=j;
            }
        }
        tmp = KWood[i];
        KWood[i] = KWood[smallIdx];
        KWood[smallIdx] = tmp;
    }
        
}

int WAR()
{
	int i, j, win;
    double samllVal, smallIdx, tmp;
	
	win = 0;
	j = numWood-1;
	for(i=numWood-1; i >= 0; i --)
	{
        if(NWood[i] > KWood[j])
        {
            win ++;
        }
        else
        {
            j--;
        }
    }
    return win;
        
}

int DWAR()
{
	int i, j, win;
    double samllVal, smallIdx, tmp;
	
	win = 0;
	j = 0;
	for(i=0; i< numWood; i ++)
	{
        if(NWood[i] > KWood[j])
        {
            win ++;
            j ++;
        }

    }
    return win;
        
}

int main(int argc, char *argv[])
{

    char *inFileName = "D-large.in";
    char *outFileName = "D-large.out";
    //char *inFileName = "B-small-practice.in";
    //char *outFileName = "B-small-practice.out";
    int group, result;
    int i, j, k;
    FILE * pInFile, *pOutFile;
    

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");

    //genDataBase();
    //displayDataBase(pOutFile);

    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    
    int tmp;
    for(i =0; i< group; i++)
    {
          fscanf(pInFile, "%d", &numWood);
          printf("numWood %d\n", numWood);
                     
          for(j = 0; j < numWood; j ++)
          {
                fscanf(pInFile, "%lf", &NWood[j]);
                printf("%lf ", NWood[j]);
          }
          printf("\n", NWood[j]);

          for(j = 0; j < numWood; j ++)
          {
                fscanf(pInFile, "%lf", &KWood[j]);
                printf("%lf ", KWood[j]);
          }
          printf("\n", KWood[j]);
    
          sort();
          
          fprintf(pOutFile, "Case #%d: %d %d\n", i + 1, DWAR(), WAR());
          
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




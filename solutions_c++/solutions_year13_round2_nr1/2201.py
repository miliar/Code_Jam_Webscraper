#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>

using namespace std;



/* Global Variables*/    
    int A;
    int N;
    int obj[1000];
/*---------*/  


int genResult(int nowSize, int index, int move)
{
    int i;
    int movAdd, movDel;
    for(i = index; i < N; i++)
    {
        if(nowSize > obj[i])
            nowSize += obj[i];
        else
            break;
    }
    
    if(i == N)
        return move;
    else
    {
        if(nowSize > 1)
        {
            movAdd = genResult(nowSize + nowSize -1, i, move+1);
            movDel = genResult(nowSize, i+1, move+1);
        
            if(movAdd <= movDel)
                return movAdd;
            else
                return movDel;
        }
        else
            return genResult(nowSize, i+1, move+1);
    }
    
}


int powCal(int x, int n)
{
    int i = 0, result = 1;
    for(i = 0; i < n; i ++)
    {
        result *= x;
    }
    
    return result;
}

void sort()
{
    int i, j, min = obj[0], minIdx = 0, tmp;
    
    for(i = 0; i < N; i++)
    {
        min = obj[i];
        minIdx = i;
        for(j = i; j < N; j ++)
        {
            if(obj[j] < min)
            {
                min = obj[j];
                minIdx = j;
            }
        }
        tmp = obj[i];
        obj[i] = obj[minIdx];
        obj[minIdx] = tmp;
    }
}

int main(int argc, char *argv[])
{

    char *inFileName = "A-large.in";
    char *outFileName = "A-large.out";
    int i, j, k;
    int group;
    int num1, num2;
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
          memset(obj, 0, sizeof(obj));
          
          fscanf(pInFile, "%d", &A);
          printf("A %d\n", A);
          
          fscanf(pInFile, "%d", &N);
          printf("N %d\n", N);

          for(j = 0; j < N; j ++)
          {
                fscanf(pInFile, "%d", &obj[j]);
                printf("obj[%d] %d \n", j, obj[j]);
          }
          
          sort();
          
          for(j = 0; j < N; j ++)
          {
                printf("obj[%d] %d \n", j, obj[j]);
          }
          
          result = genResult(A, 0, 0);
          
          fprintf(pOutFile, "Case #%d: %d\n", i+1, result);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    char line[100];
/*---------*/  




int count()
{
    int i = 0, result = 0, pre = 0, curr=0, len=strlen(line);
    
    
    for(i = 0; i < len; i ++)
    {
        if(line[i] == '-')
        	curr = 1;
        else
        	curr = 2;
        
		switch(pre)
		{
			case 0:
				if(curr == 1)
					result ++;
				break;
			case 1:
				break;
			case 2:
				if(curr == 1)
					result +=2;
				break;
			default:
				break;
		}
		
		pre = curr;
    }
    
    return result;
}


int main(int argc, char *argv[])
{

    char *inFileName = "B-large.in";
    char *outFileName = "B-large.out";
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
          fscanf(pInFile, "%s\n", &line);
          printf("%s\n", line);
          result = count();
          
          fprintf(pOutFile, "Case #%d: %d\n", i+1, result);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




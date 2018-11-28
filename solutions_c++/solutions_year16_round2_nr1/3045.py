#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    unsigned __int64 par[9];
	unsigned __int64 curr[9];
    int len, num;
    char iStr[2000];
    int count[26], result[26];
    
	FILE * pInFile, *pOutFile;
/*---------*/  





int main(int argc, char *argv[])
{

    char *inFileName =  "A-large.in";
    char *outFileName = "A-large.out";
    int i, j, k;
    int group, len;
    int ans1, ans2;
/* Local Variables*/    
    //int A, N;
/*---------*/    

    

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");


    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {
    	unsigned __int64 gen;
    	
    	memset(count, 0, sizeof(count));
    	memset(result, 0, sizeof(result));
    	
    	fscanf(pInFile, "%s", iStr);
    	printf("%s\n", iStr);
    
    //printf("%d %I64u %d %I64u %I64u\n", wP1, rP1, wP2, rP2, gened);
    	len = strlen(iStr);
    	    	
    	
    	for(j = 0; j<len; j++)
    	{
    		count[iStr[j] - 'A'] ++; 
		}
		 
		result[0] += count['Z'-'A'];
		count['E'-'A'] -= result[0];
		count['R'-'A'] -= result[0];
		count['O'-'A'] -= result[0];
		
		result[2] += count['W'-'A'];
		count['T'-'A'] -= result[2];
		count['O'-'A'] -= result[2];
		
		result[6] += count['X'-'A'];
		count['S'-'A'] -= result[6];
		count['I'-'A'] -= result[6];
		
		result[8] += count['G'-'A'];
		count['E'-'A'] -= result[8];
		count['I'-'A'] -= result[8];
		count['H'-'A'] -= result[8];
		count['T'-'A'] -= result[8];
		
		result[3] += count['H'-'A'];
		count['T'-'A'] -= result[3];
		count['R'-'A'] -= result[3];
		count['E'-'A'] -= result[3];
		count['E'-'A'] -= result[3];
		
		result[7] += count['S'-'A'];
		count['E'-'A'] -= result[7];
		count['V'-'A'] -= result[7];
		count['E'-'A'] -= result[7];
		count['N'-'A'] -= result[7];
		
		result[5] += count['V'-'A'];
		count['F'-'A'] -= result[5];
		count['I'-'A'] -= result[5];
		count['E'-'A'] -= result[5];
		
		result[4] += count['F'-'A'];
		count['O'-'A'] -= result[4];
		count['U'-'A'] -= result[4];
		count['R'-'A'] -= result[4];
			
		result[1] += count['O'-'A'];
		count['N'-'A'] -= result[1];
		count['E'-'A'] -= result[1];
		
		result[9] += count['E'-'A'];
		
		fprintf(pOutFile, "Case #%d: ", i+1);
		
		for(j = 0; j < 10; j++)
        {
        	while(result[j]!=0)
        	{
        		printf("%d", j);
        		fprintf(pOutFile, "%d", j);
        		result[j] --;
			}
			
		}
		
		fprintf(pOutFile, "\n");
        printf("\n");
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




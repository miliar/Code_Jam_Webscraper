#include <cstdlib>
#include <iostream>
#include <stdio.h>
#include <math.h>
#include <string.h>

using namespace std;



/* Global Variables*/    
    int base[1000];
    int total;
/*---------*/  



int powCal(int x, int n)
{
    int i = 0, result = 1;
    for(i = 0; i < n; i ++)
    {
        result *= x;
    }
    
    return result;
}


int checkPal(int input)
{
	int forward, backward;
	
	forward = input;
	backward = 0;
	while(forward > 0)
	{
		backward = backward * 10 + (forward % 10);
		forward /= 10;
		
	}
	
	forward = input;
	if(backward == forward)
		return true;
	else
		return false;
	
}

int main(int argc, char *argv[])
{

    char *inFileName = "C-small-attempt0.in";
    char *outFileName = "C-small-attempt0.out";
    int i, j, k;
    int group;
    int num1, num2;
/* Local Variables*/    
    int maxVal, endVal, result;
/*---------*/    
    FILE * pInFile, *pOutFile;
    
    maxVal= 1000;
    
    endVal = (int)(sqrt(maxVal))+1;
    
    memset(base, 0, sizeof(base));
    
    total = 0;
    for(i= 0; i < endVal; i++)
    {
    	if(checkPal(i) == true)
		if(checkPal(i * i)==true)
    	{
    		base[total] = i * i;
			printf("base[%d]=%d\n", total, base[total]);
			total ++;		
    	}
    }

    if((pInFile = fopen(inFileName, "r")) == NULL)
          printf("error open file\n");

    if((pOutFile = fopen(outFileName, "w")) == NULL)
          printf("error open file\n");


    fscanf(pInFile, "%d", &group);
    printf("group %d\n", group);
    for(i =0; i< group; i++)
    {
          num1 = num2 = 0;
          
          fscanf(pInFile, "%d", &num1);
          fscanf(pInFile, "%d", &num2);

		  result = 0;
	        for(k = 0; k < total; k ++)
	        {
	            if(base[k] < num1)
	            	continue;
	            else if(base[k] > num2)
	            	break;
	            else
	            	result ++ ;
					 
	        }

            fprintf(pOutFile, "Case #%d: %d\n", i+1, result);
    }
        
    fclose(pInFile);
    fclose(pOutFile);
    
    system("PAUSE");
    return EXIT_SUCCESS;
}




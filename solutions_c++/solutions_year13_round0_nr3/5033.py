#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <iostream>
using namespace std;

void saveFile (int result, int caseNumber)
{
	FILE *fp;
	fp = fopen ("output.txt", "a");
	
	if (fp!=NULL)
	{
			fprintf(fp, "Case #%d: %d\n", caseNumber+1, result);
	}
	else
		printf ("Error opening/creating file");
	fclose(fp);
}

int loadFile (int A[], int B[])
{
	int numberOfCases;
	int i;
	FILE *fp;
	fp = fopen("input.in","r");
	
	if (fp != NULL)
	{
		fscanf(fp,"%d",&numberOfCases);
		
		for (i=0; i<numberOfCases; i++)
		{
			fscanf(fp,"%d %d", &A[i],&B[i]);
		}
	}
	else
	    printf("File not found\n");
	return numberOfCases;
}


int digitCount (int num)
{
      int digitCounter=0, end=0;
      do
      {
            num /= 10;
            digitCounter++;
      }while(num!=0);
      return digitCounter;
}

void createString(int num, char *p, int size)
{
    int s = size; 
    do
    {
         p[size-1] =  '0' + num%10;
         num /= 10;
         size--;
    }while(size>=0);
    p[s] = '\0'; 
}

int ispalindrome(char *p, int size)
{
    int i;
    for(i=0;i<size/2;i++)
    {
          if(p[i] != p[size-1-i])
              return 0;
    }
    return 1;
}

int fairNsquare(int a, int b)
{
      int c1, i, count, countOfFairAndSquare=0;
      float c2;
      char *p,*p2;
      for(i=a;i<=b;i++)
      {
            c2 =  sqrt(i);
            c1 = c2;
            if ( ( (c1/1.0) == c2 ) )
            {
                count = digitCount(c1);
                p = (char *) malloc((count+1)*sizeof(char)); 
                createString(c1, p, count);
                if(ispalindrome(p, count))
                {
                      count = digitCount(i);
                      p2 = (char *) malloc((count+1)*sizeof(char)); 
                      createString(i, p2, count); 
                      if(ispalindrome(p2, count))
                      {
                            printf("%d\n",i);             
                            countOfFairAndSquare++;             
                      }   
                      free(p2);       
                }
                free(p);
            }
      }
      return countOfFairAndSquare;
}

main()
{
      int cases, a[100], b[100], res[100], i;
      cases = loadFile(a,b);
      for(i=0;i<cases;i++)
      {
            res[i] = fairNsquare(a[i] ,b[i]);
            
            saveFile(res[i],i);
      }
      
      
      system("pause");
}


      

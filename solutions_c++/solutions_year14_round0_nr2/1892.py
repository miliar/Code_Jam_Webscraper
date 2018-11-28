#include<stdio.h>
#include <string.h>
#include <stdlib.h>
#include <math.h>


int main() 
{ 

#ifdef FILEIO
	freopen("in.txt","r",stdin); 
	freopen("out.txt","w",stdout); 
#endif

	int T;

	double C,F,X;

	int i,j,k;//for loop

	double result;
	double resultTemp;

	int numberOfFarms;

	scanf("%d",&T);


	for(i=0;i<T;i++)
	{
		scanf("%lf",&C);
		scanf("%lf",&F);
		scanf("%lf",&X);
		result=0;
		resultTemp=0;
		numberOfFarms = 0;
		/*
		4
		30.0 1.0 2.0
		30.0 2.0 100.0
		30.50000 3.14159 1999.19990
		500.0 4.0 2000.0

		Case #1: 1.0000000
		Case #2: 39.1666667
		Case #3: 63.9680013
		Case #4: 526.1904762
		*/

		while(1)
		{
			resultTemp = 0;
			if(numberOfFarms == 0)
			{
				resultTemp = X/(double)2;
				result = resultTemp;
			}
			else if (numberOfFarms >= 1)
			{
				for(j=0;j<numberOfFarms;j++)
				{
					resultTemp += C/((double)2+j*F);
				}
				resultTemp += X/(double)(2+numberOfFarms*F);
			}

			numberOfFarms++;

			if(resultTemp < result)
			{
				result = resultTemp;
				continue;
			}

			if(resultTemp > result)
				break;
		}


		printf("Case #%d: %.7f\n",(i+1),result);
	}
	

#ifdef FILEIO
	fclose(stdin);
	fclose(stdout);
#endif  

	return 0; 
}

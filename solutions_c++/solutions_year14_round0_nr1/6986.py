#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define FAILED -1
#define SUCCESS 0
#define OUTPUT_IN_FILE	0

int gNInputs = 0;
int gInputArray[4][4];
int gOutputArray[4];
int gNAnswer1;
int gNAnswer2;

//Get input from file
int getMagicNumber()
{
	FILE *fp = NULL;

	fp = fopen("D://A-small-attempt2.in","r");

	if(fp == NULL)
	{
		printf("Failed to open the file\n");
		return FAILED;
	}
	
	//get first read number of inputs
	fscanf(fp,"%d",&gNInputs);

	//for each input
	int nCnt = 0, nTemp, nMagicNumber=0;

	for(nCnt = 0;nCnt < gNInputs;nCnt++)
	{
		//reset array
		for(int n=0;n<4;n++)
		{
			gOutputArray[n] = 0;
		}
		//read ans
		fscanf(fp,"%d",&gNAnswer1);

		//read input set 1
		int i =0,j =0;
		while(1)
		{
			if(j == 4)
			{
				j= 0;
				i++;
			}

			if(i == 4)
				break;
			fscanf( fp,"%d",&gInputArray[i][j]);
			j++;
		}

		//check all the element for that row
		//every element of row must be distributed to each row next time
		//then only magician can be identify the so just check if it is so other wise
		//check which row has more then one element mark those rows and if user select
		//any of those rows then "Bad magician!" if user select any row which does not 
		//have any of the element of previous row then "Volunteer cheated" otherwise
		//print that element

		fscanf(fp,"%d",&gNAnswer2);
		i = 0,j=0;

		while(1)
		{
			if(j == 4)
			{
				j= 0;
				i++;
			}

			if(i == 4)
				break;

			fscanf( fp,"%d",&nTemp);
			j++;

			//check if this number is one of the gNAnswer1
			//then update the count in gOutputArray
			for(int n=0;n<4;n++)
			{
				if(nTemp == gInputArray[gNAnswer1-1][n])
				{
					gOutputArray[i] = gOutputArray[i]++;

					if(i==(gNAnswer2-1))
					{
						nMagicNumber = nTemp; 
					}

					break;
				}
			}
		}

		//match user's answer 
		if(gOutputArray[gNAnswer2-1] == 0)
		{
			printf("Case #%d: Volunteer cheated!\n",nCnt+1);
		}

		if(gOutputArray[gNAnswer2-1] == 1)
		{
			printf("Case #%d: %d\n",nCnt+1,nMagicNumber);
		}

		if(gOutputArray[gNAnswer2-1] > 1)
		{
			printf("Case #%d: Bad magician!\n",nCnt+1);
		}

	}


	fclose(fp);

	return SUCCESS;
}

int main(int argc,char *argv[])
{

	getMagicNumber();
	return 0;
}
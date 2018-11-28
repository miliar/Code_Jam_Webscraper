#include <stdio.h>
#include <fcntl.h>
#include <stdlib.h>
#include <string.h>
#include <math.h>

#define FAILED -1
#define SUCCESS 0
#define OUTPUT_IN_FILE	0

int gNInputs = 0;

const int gCMax = 500;
const int gFMin = 1;
const int gXMax = 2000;

//Get input from file
int letUsPlayTheGame()
{
	FILE *fp = NULL;

	fp = fopen("D://B-large (12).in","r");

	if(fp == NULL)
	{
		printf("Failed to open the file\n");
		return FAILED;
	}
	
	//get first read number of inputs
	fscanf(fp,"%d",&gNInputs);

	//for each input
	int nCnt = 0, nTemp;
	double dCValue = 0.0, dFValue = 0.0, dXValue = 0.0;
	double dCookies = 0.0, dElapsedTime = 0.0, dExpectedTime = 0.0, dTimeToC = 0.0, dTimeWithFarm = 0.0 ;
	double dTmp = 0.0;

	for(nCnt = 0;nCnt < gNInputs;nCnt++)
	{
		//scan the input
		dCookies = 2.0, dElapsedTime = 0.0, dExpectedTime = 0.0, dTimeToC = 0.0, dTimeWithFarm = 0.0 ;
		fscanf(fp,"%lf %lf %lf",&dCValue,&dFValue,&dXValue);

		do
		{
			dExpectedTime = dElapsedTime + dXValue/dCookies;
			dTimeToC = dCValue/dCookies;
			dCookies += dFValue;
			dTimeWithFarm = dElapsedTime + dTimeToC + dXValue/dCookies;
			dElapsedTime += dTimeToC;
		}while(dExpectedTime > dTimeWithFarm);

		printf("Case #%d: %lf\n",nCnt+1,dExpectedTime);
	}


	fclose(fp);

	return SUCCESS;
}

int main(int argc,char *argv[])
{

	letUsPlayTheGame();
	return 0;
}
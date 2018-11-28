// cookieClicker.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"


int _tmain(int argc, _TCHAR* argv[])
{  
  FILE *inputFile, *outputFile;
  int numCase, i, j, numFarm;
  double C, F, X, time, speed, numCookie;
  numCase = 0;
  if((inputFile = fopen("B-large.in","r"))==NULL)
  {
    printf("error in reading file!\n");
    return 0;
  }
  if((outputFile = fopen("result.out","w"))==NULL)
  {
    printf("error in reading file!\n");
    return 0;
  }
  fscanf(inputFile,"%d",&numCase);
  fgetc(inputFile);
  for(i = 0; i < numCase; i ++)
  {
    fprintf(outputFile, "Case #%d: ",i+1);
    fscanf(inputFile,"%lf", &C);
    fgetc(inputFile);
    fscanf(inputFile,"%lf", &F);
    fgetc(inputFile);
    fscanf(inputFile,"%lf", &X);
    fgetc(inputFile);

    speed = 2;
    double shortestTimeNotBuyFarm = X/speed;
    double timeWithBuyFarm, timeWithoutBuyFarm;
    timeWithBuyFarm = timeWithoutBuyFarm = 0;
    while(1)
    {

      timeWithoutBuyFarm = timeWithBuyFarm + (X ) / speed;
      if(timeWithoutBuyFarm < shortestTimeNotBuyFarm)  ///shortest time not buy farm found
        shortestTimeNotBuyFarm = timeWithoutBuyFarm;

      timeWithBuyFarm += (C ) / speed;
      if(timeWithBuyFarm >= shortestTimeNotBuyFarm)
        break;
      else
        speed += F;  ///keep on buying farm
    }
    fprintf(outputFile, "%.7lf\n",shortestTimeNotBuyFarm);
    
  }
  return 0;
}


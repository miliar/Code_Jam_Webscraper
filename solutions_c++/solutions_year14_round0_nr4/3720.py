// deceitfulWar.cpp : Defines the entry point for the console application.
//

#include "stdafx.h"
#include <malloc.h>
#include <algorithm> 
#include <vector> 
#include <assert.h>
using namespace std;
typedef enum
{
  INCREASE = 0,
  DECREASE,
}sortOrder;

bool increase (double i,double j) { return (i<j); }
bool decrease (double i,double j) { return (i>j); }
void sortArray(std::vector<double> *myvector, long long numItem, sortOrder order )
{
  if(order == INCREASE)
    std::sort (myvector->begin(), myvector->end(), increase);
  else if(order == DECREASE)
    std::sort (myvector->begin(), myvector->end(), decrease);
  else
    assert(0);

}


////play deceitful war
int playDeceitfulWar(std::vector<double> vectorX, std::vector<double> vectorY, int numItem)
{
  int result = 0;
  int i,j;
  bool *flag = new bool[numItem]; /// flag to indicate mass burnt
  memset(flag, 0, numItem * sizeof(bool)); 
  sortArray(&vectorX, numItem,INCREASE);  ///increase order
  sortArray(&vectorY, numItem,INCREASE);  ///decrease order
  for(i = 0; i < numItem; i ++)
  {
    for( j = 0; j < numItem ; j ++)
    {
      if(flag[j] == true)
        continue;
      if(vectorX[j] > vectorY[i])
      {
        result ++;
        flag[j] = true;
        break;
      }
    }
    if(j == numItem) ///if no one larger, burn the smallest one
    {
      for( j = 0; j < numItem ; j ++)
      {
        if(flag[j] == false)
        {
          flag[j] = true;
          break;
        }
      }
    }
  }
  return result;
}

///play optimal war
int playOptimalWar(std::vector<double> vectorX, std::vector<double> vectorY, int numItem)
{
  int result = numItem;
  bool *flag = new bool[numItem]; /// flag to indicate mass burnt
  memset(flag, 0, numItem * sizeof(bool)); 
  sortArray(&vectorX, numItem,INCREASE);  ////both in increase order
  sortArray(&vectorY, numItem,INCREASE);
  for(int i = 0; i < numItem; i ++)
  {
    for( int j = 0; j < numItem ; j ++)
    {
      if(flag[j] == true)
        continue;
      if(vectorX[i] < vectorY[j])  ///find the optimal one
      {
        result --;
        flag[j] = true;  //burnt
        break;
      }
    }
  }
  delete [] flag;
  return result;
}

int _tmain(int argc, _TCHAR* argv[])
{
  FILE *inputFile, *outputFile;
  int numCase, i, j, credit, numItem;
  double readValue;
  int result;
  numCase = 0;
  if((inputFile = fopen("D-large.in","r"))==NULL)
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
    fscanf(inputFile,"%d", &numItem);
    fgetc(inputFile);
    std::vector<double> vectorX(numItem, 0);
    std::vector<double> vectorY(numItem, 0);
    for(j = 0; j < numItem; j ++)
    {
      fscanf(inputFile,"%lf", &readValue);
      vectorX[j] = readValue;
    }
    for(j = 0; j < numItem; j ++)
    {
      fscanf(inputFile,"%lf", &readValue);
      vectorY[j] = readValue;
    }
    result = playDeceitfulWar(vectorX, vectorY, numItem);   //decieful war
    fprintf(outputFile, "%d  ",result);

    result = playOptimalWar(vectorX, vectorY, numItem);   ///optimal war
    fprintf(outputFile, "%d\n",result);

  }
	return 0;
}


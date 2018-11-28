#include <iostream>
#include <cstdlib>
#include <fstream>

using namespace std;

int compare(const void * a, const void * b)
{
  if(*(double*)a==*(double*)b)
    return 0;
  else if (*(double*)a < *(double*)b)
    return -1;
  else
    return 1;
}

int main(){
  int numCases, numBlocks;
  int i, j, k;
  double *naomi, *ken;
  int warScore, dwarScore;
  ifstream infile;
  ofstream outfile;

  infile.open("D-large.in");
  outfile.open("output.txt");
  infile >> numCases;
  for(i = 0; i < numCases; i++){
    infile >> numBlocks;
    naomi = new double[numBlocks];
    ken = new double[numBlocks];
    warScore = numBlocks;
    dwarScore = 0;
    for(j=0; j<numBlocks; j++)
      infile >> naomi[j];
    for(j=0; j<numBlocks; j++)
      infile >> ken[j];
    qsort(naomi, numBlocks, sizeof(double), compare);
    qsort(ken, numBlocks, sizeof(double), compare);
    for(j=numBlocks - 1, k = numBlocks - 1; j >= 0, k >= 0; j--, k--){
      while(naomi[j] < ken[k] && k > 0)
        k--;
      if (naomi[j] > ken[k])
	dwarScore++;
    }
    for(j=numBlocks - 1, k = numBlocks - 1; j >= 0, k >= 0; j--, k--){
      while(ken[j] < naomi[k] && k > 0)
        k--;
      if (ken[j] > naomi[k])
        warScore--;
    }

    outfile << "case #" << i+1 << ":  " << dwarScore << " " << warScore << endl;

    delete [] naomi;
    delete [] ken;
  }
  infile.close();
  outfile.close();
  return 0;
}

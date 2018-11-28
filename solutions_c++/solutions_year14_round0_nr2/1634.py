#include <iostream>
#include <cmath>
#include <fstream>
#include <iomanip>

using namespace std;

const double COOKIE_RATE = 2.0;  /* cookies per second */

int main(){
  int numCases;
  double C;	/* Cost of farm */
  double F;	/* Farm cookie rate */
  double X;	/* Cookie Goal */
  int i, j, k;
  int maxFarms;
  int numFarms;
  double minTime, sumTime;
  ifstream infile;
  ofstream outfile;
  
  infile.open("B-large.in");
  outfile.open("output.txt");
  outfile << fixed << setprecision(7);
  infile >> numCases;
  for(i = 0; i < numCases; i++){
    infile >> C >> F >> X;
    maxFarms = ceil(X / C);
    minTime = X / COOKIE_RATE;
    for (j = 1; j <= maxFarms; j++){
      sumTime = 0;
      numFarms = 0;
      for(k = 1; k <= j; k++){
        sumTime += (C / (COOKIE_RATE + numFarms * F));
        numFarms++;
      }
      sumTime += (X / (COOKIE_RATE + numFarms * F));
      if (minTime > sumTime)
	minTime = sumTime;
    }
    outfile << "Case #" << i+1 << ":  " << minTime << endl;
  }
 
  infile.close();
  outfile.close();
  return 0;
}

#include<stdio.h>
#include<stdlib.h>
#include<iostream>
#include<fstream>

using namespace std;

int buyMoreFarm(double farmPrice, double farmReward, double cutoff, double numFarms, double* period){
  // time without buying more farms
  double time1 = cutoff / (farmReward*numFarms + 2);
  
  // time with buy one more farm
  double time2 = farmPrice / (farmReward*numFarms + 2) + cutoff / (farmReward*(numFarms + 1) + 2);
  if(time1 < time2){
    *period = *period + time1;
    return 0;
  }
  else{
    *period = *period + farmPrice / (farmReward*numFarms + 2);
    return 1;
  } 
}

int main(){
  ifstream case1;
  string line;
  double farmPrice = 0, farmReward = 0, cutoff = 0, numFarms = 0, period = 0;
  int numCases = 0;

  case1.open("B-large.in");
  case1 >> numCases;
  for(int i = 0; i < numCases; ++i){
    case1 >> farmPrice >> farmReward >> cutoff;
    while(buyMoreFarm(farmPrice, farmReward, cutoff, numFarms, &period)){
      numFarms++;
    }
    cout << "Case #" << i +1<< ": ";
    printf("%.8f\n", period);
    period = 0;
    numFarms = 0;
  }
  case1.close();
  return 0;
}


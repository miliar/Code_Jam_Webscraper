#include <iostream>
#include <iomanip>

using namespace std;

void solve(){
  long double farmCost, farmEarn, goal;
  cin >> farmCost >> farmEarn >> goal;
  
  long double time = 0;
  long double cps = 2.;
  
  
  farmCost *= 1000000;
  farmEarn *= 1000000;
  goal *= 1000000;
  cps *= 1000000;
  
  while(true){
    //calc time to goal
    long double ttg = goal/cps;
    
    //calc time to farm
    long double ttf = farmCost/cps;
    //calc time to goal with increased prod
    long double ttg2 = goal/(cps+farmEarn);
    
    if(ttg < ttf+ttg2){
      //no more farms, we can quit
      time += ttg;
      break;
    }
    else{
      //farm is more efficient, we need to buy one
      time += ttf;
      cps += farmEarn;
    }
  }
  
  //time /= 1000000;
  cout.precision(7);
  cout << fixed << time << endl;
}

int main(){
  int ncase;
  cin >> ncase;
  for(int i=0;i<ncase;++i){
    std::cout << "Case #" << i+1 << ": ";
    
    solve();
  }
}
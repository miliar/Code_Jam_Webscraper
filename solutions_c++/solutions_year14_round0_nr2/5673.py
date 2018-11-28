#include "iostream"
#include <fstream>
#include <iomanip>
#include "cmath"
using namespace std;
int main(int argc, char const *argv[]){
  ofstream myfile;
  myfile.open ("output.txt");
  int cases;
  cin >> cases;
  for(int c=0; c<cases; ++c){
    int numberoffarms=0;
    double income=2, price, farms, goal, seconds=0.0, fastforward, future, winning;
    cin >> price >> farms >> goal;
    do{
      winning = goal/income;
      fastforward = price/income-(0.3e-11*numberoffarms);
      future = fastforward + ((goal-(income*fastforward-price))/(income+farms));
      if((future-winning) < 1e-6){
        seconds += fastforward;
        numberoffarms++;
        income = 2+(numberoffarms*farms);
      }
    }while((future-winning) < 1e-6);
    seconds += winning;
    myfile << "Case #" << c+1 << ": " << fixed << setprecision(7) << seconds << endl;
  }
  return 0;
}
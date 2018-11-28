#include<iostream>
#include<iomanip>
using namespace std;

int main(void){

  int Case;
  double FarmUpgrade;
  double FarmVelocity;
  double ClearCookie;
  cin >> Case;
  for(int I=1;I<=Case;I++){
    cin >> FarmUpgrade;
    cin >> FarmVelocity;
    cin >> ClearCookie;

    double Cookie = 0.0;
    double resultTime = 0.0;
    double Velocity = 2.0;

    if(ClearCookie > FarmUpgrade){
      while(true){
	resultTime += (FarmUpgrade - Cookie) / Velocity;
	Cookie = FarmUpgrade;
	if((ClearCookie - Cookie)/Velocity > (ClearCookie-(Cookie - FarmUpgrade))/(Velocity+FarmVelocity)){
	  Cookie -= FarmUpgrade;
	  Velocity += FarmVelocity;
	  continue;
	}
	else break;
      }
    }
    resultTime += (ClearCookie - Cookie) / Velocity;

    cout << "Case #" << I << ": ";
    cout << fixed << setprecision(7) << resultTime << endl;
  }
  return 0;
}

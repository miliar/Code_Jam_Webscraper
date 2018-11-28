
#include <iostream>

using namespace std;


double requiredSeconds(const double houseCost, const double cookiePerSec, const double cookieTarget)
{
  double elapsedTime = 0;
  double curCookiePerSec = 2;  // we start with 2 cookie per second

  while(((houseCost / curCookiePerSec) + (cookieTarget / (curCookiePerSec + cookiePerSec)))
	< (cookieTarget / curCookiePerSec)) {
    
    elapsedTime += houseCost / curCookiePerSec;
    curCookiePerSec += cookiePerSec;
  }
  
  return elapsedTime + cookieTarget / curCookiePerSec;
}


int main(int argc, char **argv)
{
  int testCount = 0;
  cin >> testCount;

  for(int testCounter=0; testCounter<testCount; testCounter++) {
    double houseCost = 0;
    double cookiePerSec = 0;
    double cookieTarget = 0;

    cin >> houseCost
	>> cookiePerSec
	>> cookieTarget;

    cout << "Case #" << (testCounter+1) << ": ";
    cout.precision(7);
    cout.setf( ios::fixed, ios::floatfield ); 
    cout << requiredSeconds(houseCost, cookiePerSec, cookieTarget)
	 << endl;
  }
}


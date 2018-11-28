//
//  By Satoshi Sakamori
//

#include <fstream>
#include <iostream>
#include <iomanip>

using namespace std;

int main(){

  ifstream ifile("input.txt");
  int T;
  double C,F,X;

  ifile >> T;
  
  for(int i=0; i < T; i++){

    double spentTime = 0.0;
    double numCookies = 0.0;
    double addedCookies = 2.0;
    ifile >> C >> F >> X;

    while( numCookies < X) {

       if ( numCookies >= C ) {
           double nextTime = (X-numCookies)/addedCookies;
           if ( (X -numCookies+C) / (addedCookies + F) <  nextTime ) {
               addedCookies += F;
               numCookies -= C;
           } else {
               spentTime += nextTime;
               numCookies += nextTime*addedCookies;
           }
       } else {

           double nextTime = C/addedCookies;
           if ( (X-numCookies) /addedCookies <= nextTime ){
              spentTime +=  (X-numCookies)/addedCookies;
              numCookies =X ;
           } else { 
              spentTime += nextTime;
              numCookies +=  C;
           }
       }


    }
    cout << "Case #"<< i+1 << ": " <<fixed << setprecision(7) << spentTime << endl;
    
  }

  return 0;
}


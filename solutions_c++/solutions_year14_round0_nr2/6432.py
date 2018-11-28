#include <cstdlib>
#include <fstream>
#include <cstdio>
#include <iostream>
#include <cmath>
#include <vector>
#include <iomanip>

using namespace std;

int main () {


  ifstream ifile("input.in");
  ofstream ofile("output.txt");

  int cases;
  ifile>>cases;

  for(int i=0; i<cases; i++) {
    double c,f,x;
    double rate = 2.0;
    double tick=0.0;
    ifile>>c>>f>>x;
    while(x / rate > c/rate + (x/(rate+f))) {
      //if time to get cookies by current rate is greater than farm over current rate time + time of cookies by rate + f
      //then increase rate by f, and add time to get to c with current rate
      tick+= c/rate;
      rate += f;
    }
    tick+=x/rate;

    cout<<"Case #"<<i+1<<": "<<std::setprecision(15)<<tick<<endl;
    //optimize to get to
    //if cookies to go / currentrate > cookies to farm /curr rate + (cookies to go/ curr rate +4 then buy farm

  }

}
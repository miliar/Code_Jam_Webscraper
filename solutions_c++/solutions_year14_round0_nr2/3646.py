#include <iostream>
#include <string>
#include <set>
#include <iomanip>

using namespace std;

int main(int argc, char** argv) {
  int ntc;
  cin>>ntc;
  for(int tc=1;tc<=ntc;++tc) {
    double c, f, x, r;
    r = 2.;

    cin>>c>>f>>x;

    double besttime = x/r;
    double time = 0;

    //cerr<<" E: "<<besttime<<" R: "<<r<<endl;
    while(time < besttime) {
      double farmtime = c/r;
      double endtime = x/r;
      if(time+endtime < besttime) {
        besttime = time+endtime;
      }
      time += farmtime;
      r += f;
      //cerr<<"T="<<time<<" F: "<<farmtime<<" E: "<<endtime<<" B: "<<besttime<<" R: "<<r<<endl;
    }

    cout<<"Case #"<<tc<<": "<<setprecision(15)<<besttime<<endl;
  }
}

#include <iostream>
#include <fstream>
#include <iomanip>
#include <algorithm>

using namespace std;

int main(){
  int t,i,j;
  double c,f,x;
  ifstream ifs("test.txt");
  ofstream ofs("out1.txt");
  ifs >> t;
  for(i=1;i<=t;i++){
    double ans = 0.0;
    ifs  >> c >> f >> x;
    double y = (x-c) * f / c;
    if(2.0*c > f*(x-c)){ofs  << "Case #" << i << ": " << fixed << setprecision(7) <<  x / 2.0 << endl;}
    else {
      int t = (y-2.0) / f;
      for(j=0;j<=t;j++) ans += c/(2.0 + f*j);
      ans += x /(2.0 + f*(t+1));
      ofs  << "Case #" << i << ": " <<  fixed << setprecision( 7 ) << ans << endl;
    }
  }

  return 0;
} 

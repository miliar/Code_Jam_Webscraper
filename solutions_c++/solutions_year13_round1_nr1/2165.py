#include <iostream>
#include <cmath>

using namespace std;

int main() {
  
  int cases;
  cin >> cases;
 
for(int n=1;n<=cases;n++){
  size_t rad, ml;
  cin >> rad >> ml;
  //double m=;
  
  size_t ans=size_t(-(2.0*rad+3.0)/4.+sqrt((2.0*rad+3.0)*(2.0*rad+3.0)+8.0*(ml-2.0*rad-1.0))/4.0+1);
  cout<< "Case #" << n <<": " << ans << endl;
 // " "<< floor(-(2.0*rad+3.0)/4.+sqrt((2.0*rad+3.0)*(2.0*rad+3.0)+8.0*(ml-2.0*rad-1.0))/4.0) << endl;
}
  return 0;
}
 

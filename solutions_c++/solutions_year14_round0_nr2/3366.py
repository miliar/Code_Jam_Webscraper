#include<iostream>
#include <iomanip>
using namespace std;

int main(){
  int z,t;
  double c,x,f,ct,cr;
  cin >> t;
  for(z=1;z<=t;z++){
    cin >> c >> f >> x;
    ct=0;cr=2;
    while(x/cr > (c/cr)+(x/(cr+f))){
      ct+=c/cr;
      cr+=f;
    }
    cout << setprecision(sizeof(long double)) << "Case #" << z << ": " << ct+(x/cr) << endl;
  }
  return 0;
}
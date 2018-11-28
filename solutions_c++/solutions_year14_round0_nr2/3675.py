#include <iostream>
#include <iomanip>
using namespace std;

int main() {
  int n;
  cin>>n;
  for(int i = 0; i < n; i++) {
    cout.precision(7);
    cout<<fixed;
    long double C, F, X;
    cin>>C>>F>>X;
    long double wynik = 0.0000000;
    long double Z = 2.0000000;
    long double akt = 0;
    while(1) {
      if(X/Z > (C/Z) + X/(Z+F)) {
	wynik += C/Z;
	Z+=F;
      } else {
	wynik += X/Z;
	break;
      }
    }
    cout.precision(7);
    cout<<"Case #"<<i+1<<": "<<wynik<<endl;
  }
  
  
}
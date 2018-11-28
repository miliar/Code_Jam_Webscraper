#include <iostream>
using namespace std;

int main(int argc, char **argv) {
  int T, cn=0;  
  double C, F, X, Cratio, tiempo;
  cout.precision(10);
  cout.setf( ios::fixed, ios::floatfield );
  
  cin>>T;
  while(cn != T) {
    cin>>C>>F>>X;
    Cratio=2;
    tiempo=0;
    
    while( X/Cratio > C/Cratio + X/(Cratio+F) ) {
      tiempo += C/Cratio;
      Cratio += F;
    }
    tiempo += X/Cratio;
    
    cout<<"Case #"<<++cn<<": "<<tiempo<<endl;
  }
  return 0;
}

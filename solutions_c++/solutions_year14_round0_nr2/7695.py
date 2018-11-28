#include <iostream>
#include <iomanip>
#include <cmath>


using namespace std;

int upgrade_num(double C, double F, double X){
  return int(max(0.0, (X*F - 2.0*C)/(F*C)));
}

int main(){
  int repeat;
  double C,F,X;
  int num,n;

  cin >> repeat;
  for(int i=0;i<repeat;i++){
    cin >> C >> F >> X;

    double Totaltime = 0;
    num = upgrade_num(C,F,X);
    
    for(n=0;n<num;n++){
      Totaltime += C/(2.0+n*F);
    }
    Totaltime += X/(2.0+num*F);
     
    cout << "Case #"<< i+1 << ": ";
    cout << fixed << setprecision(7) << Totaltime;
    cout << endl; 
  }  
}

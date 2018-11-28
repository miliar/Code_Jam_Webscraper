#include <iomanip>
#include <iostream>
#include <fstream>

using namespace std;

const double COOKIE = 2;

double timing(double COOKIE, double C, double F, double X){
  if(X/(COOKIE) < C/COOKIE+X/(COOKIE+F))
    return X/COOKIE;    
  else

    return C/COOKIE + timing(COOKIE+F,C,F,X);
}

int main(){
  ifstream file("B-large.in");
  int N;
  file >> N;

  ofstream result("result.txt");
  
  for (int i = 0; i < N; i++){
    double C, F, X;
    file >> C >> F >> X;
    result << fixed << setprecision(7);
    result << "Case #"<< i+1 << ": " << timing(COOKIE, C,F,X) << endl;
  }
  file.close();
}

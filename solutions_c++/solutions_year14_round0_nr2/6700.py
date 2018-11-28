#include <iostream>
#include <fstream>
#include <iomanip>

using namespace std;

double c, f, x;
int t;
double mycur, mynext, curf;


int main(){
  
  ifstream fin("B-large.in");
  ofstream fout("myout.out");
  
  fin >> t;
  
  
  for (int i = 0; i < t; ++i){
    fin >> c >> f >> x;
    fout.precision(7);
    if (c >= x){
      fout << "Case #" << i + 1 << ": " <<fixed << x/2 << endl;
      continue;
    }
    mycur = c/2;
    mynext = c/2 + c/(2 + f);
    curf = 2;
    while (mycur + (x - c)/curf > mynext + (x - c)/(curf + f)){
//      cout << mycur << " " << mynext << " " << curf << endl;
      mycur = mynext + c/(2*f + curf);
      swap(mycur, mynext);
      curf += f;
    }
    fout << "Case #" << i + 1 << ": " << fixed << mycur + (x - c)/curf << endl;
  }
  
  
  
  return 0;

}
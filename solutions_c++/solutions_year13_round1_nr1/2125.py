#include<iostream>
#include<fstream>
#include <cmath>
#include <algorithm>
using namespace std;
ifstream fin("in");
ofstream fout("out");

int main(){
  int cases;
  fin >> cases;
  for (int iii=1; iii<=cases; iii++){
    int r,t;
    fin>>r>>t;
    double calres;
    calres=(1-2*r+sqrt((2*r-1)*(2*r-1)+8*t))/4;
    int count=(int)floor(calres);
    fout <<"Case #"<<iii<<": "<<count<<endl;
  }
  return 0;
}
    

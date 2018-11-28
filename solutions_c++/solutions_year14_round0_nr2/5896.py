#include<fstream>
#include<iostream>
#include<iomanip>
using namespace std;

double solve(double f, double c, double x) {
  double time = 0;
  double rate = 2;
  bool condition  = true;
  while(condition) {
    if( ((x - c)/rate) < (x/(rate + f))) {
      time += x/rate;
      condition = false;
    }
    else {
      time += c/rate;
      rate += f;
    }
  }

  return time;
}


int main(int argc, char** argv) {
  ifstream infile(argv[1]);
  ofstream outfile("o.out");
  outfile << std::fixed;
  int n; infile >> n;
  double F, C, X;

  for(int i = 1; i <= n; i++) {
    infile >> C; infile >> F; infile >> X;
    outfile << "Case #" << i <<": " << setprecision(7) << solve(F,C,X) << '\n';
  }
  
  infile.close();
  outfile.close();
  return 0;
}

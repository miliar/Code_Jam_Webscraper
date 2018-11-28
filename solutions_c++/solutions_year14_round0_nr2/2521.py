#include <iostream>
#include <fstream>
using namespace std;

double bestTime(double C, double F, double X) {
  
  double rate = 2, t_best = X / rate;
  double t = (C / rate);

  while ( t + X / (rate + F) < t_best) {
    rate += F;
    t_best = t + X / rate;
    t += (C / rate);
  }

  return t_best;
}

int main(int argc, char* argv[]) {
 
  if (argc < 3) {
    cout << "Usage: ./cookie input output" << endl;
    return -1;
  }

  ifstream fin(argv[1]);
  ofstream fout(argv[2]);
  fout.setf( std::ios::fixed, std::ios::floatfield );
  fout.precision(7);

  int N;
  fin >> N;

  for (int i=0; i<N; ++i) {
    double C, F, X;
    fin >> C >> F >> X;
    fout << "Case #" << i+1 << ": " << bestTime(C, F, X) << endl;
  }

  fout.close();
  fin.close();

  return 0;
}

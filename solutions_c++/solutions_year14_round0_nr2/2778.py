#include <iostream>
#include <fstream>
#include <string>
#include <cstdio>

const double F0 = 2.0;

double min_time(double C, double F, double X)
{
  double spent = 0.0;
  int farms = 0;
  
  double next_farm = C / F0;
  double win = X / F0;

  while (win > next_farm + X/(F0 + (farms+1)*F)){
    ++farms;
    spent += next_farm;
    next_farm = C / (F0 + farms * F);
    win = X / (F0 + farms * F);
  }

  return spent + win;
}

int main (int argc, char** argv)
{
  std::ifstream ifs(argv[1]);
  if (!ifs) {
    std::cout << "Cannot open" << argv[1] << std::endl;
    return -1;
  }

  int T;
  ifs >> T;

  for (int round = 1; round <= T && !ifs.eof(); ++round) {
    double C, F, X;
    ifs >> C >> F >> X;

    printf("Case #%d: %.7f\n", round, min_time(C,F,X));
  }

  ifs.close();
  return 0;
}

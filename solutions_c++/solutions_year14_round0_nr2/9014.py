#include <iomanip>
#include <iostream>
#include <set>
#include <vector>
#include <iostream>
#include <sstream>


double cookie(double C, double F, double X) {
  double sec = 0.0;
  double rate = 2.0;
  while (true) {
    double wo_farm = X / rate;
    double w_farm = C / rate + X / (rate + F);
    if (wo_farm < w_farm) {
      return sec += X / rate;
    }
    sec += C / rate;
    rate += F;
  }
}

int main(int argc, char** argv) {
  int cases = 0;

  std::string line;
  std::getline(std::cin, line);
  std::istringstream iss(line);
  iss >> cases;

  for (int case_id = 1; case_id < cases + 1; case_id++) {
    double C = 0.0;
    double F = 0.0;
    double X = 0.0;

    std::getline(std::cin, line);
    std::istringstream iss(line);
    iss >> C;
    iss >> F;
    iss >> X;
    std::cout << std::fixed << std::setprecision(7);
    //std::cout << C << " " << F << " " << X << std::endl;
    std::cout << "Case #" << case_id << ": " << cookie(C, F, X) << std::endl;
  }
}

#include <iostream>
#include <fstream>
int main(int argc, char* argv[]) {
  std::ifstream input(argv[1]);
  std::ofstream g(argv[2]);
  g.precision(8);
  g.setf(std::ios::fixed);
  g.setf(std::ios::showpoint);
  int t;
  input >> t;
  for (int k = 0; k <t ; k++) {
    double c, f, x;
    input >> c >> f >> x;
    double remcookies = x;
    double spenttime = 0;
    double prod = 2;
    while (true) {
      if (remcookies / prod <= c/prod + remcookies/(prod + f)) {
        spenttime += remcookies/prod;
        break;
      }
      else {
        spenttime += c/prod;
        prod += f;

      }
    }

    g << "Case #" << (k + 1) <<": " << spenttime << std::endl;
  }
  
  g.close();
}

#include <iostream>
#include <string>
#include <sstream>

double solve(double c, double f, double x) {
  double time = 0.0;
  double rate = 2.0;

  while(true) {
    double timeStop = x / rate;
    double timeContinue = c / rate + x / (rate + f);

    if(timeStop < timeContinue) {
      return time + timeStop;
    }

    time += c / rate;
    rate += f;
  }
  
  return 0.0;
}

int main() {
	std::string line;

	int numTestCases = 0;
	std::getline(std::cin, line);
	sscanf(line.c_str(), "%d", &numTestCases);

	for(int testCase = 0; testCase < numTestCases; testCase++) {
    double c, f, x;

    std::getline(std::cin, line);
    sscanf(line.c_str(), "%lf %lf %lf %lf", &c, &f, &x);

    char buf[32];
    sprintf(buf, "%.7f", solve(c, f, x));
    std::cout << "Case #" << (testCase + 1) << ": " << buf << std::endl;
  }

  return 0;
}

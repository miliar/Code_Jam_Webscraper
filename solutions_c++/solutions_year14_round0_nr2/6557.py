#include <iostream>
#include <algorithm>
#include <iterator>
#include <limits>
#include <iomanip>

struct input {
  double c;
  double f;
  double x;

  double solve() const {
    double rate = 2;
    double time = 0;
    while(x / (rate + f) + c / rate < x / rate) {
      time += c / rate;
      rate += f;
    }
    time += x / rate;
    return time;
  };
};

std::istream& operator>>(std::istream& in, input& input) {
  return in >> input.c >> input.f >> input.x;
}

void print_case(std::ostream& out, double result) {
  out << std::setprecision(std::numeric_limits<double>::digits10) << result;  
};

int main() {
  int num_cases;
  std::cin >> num_cases;
  std::vector<input> cases;
  std::copy_n(std::istream_iterator<input>(std::cin), num_cases, std::back_inserter(cases));
  std::for_each(cases.begin(), cases.end(), [](input const& c) {
      static int case_nr = 1;
      std::cout << "Case #" << case_nr << ": ";
      print_case(std::cout, c.solve());
      std::cout << "\n";
      case_nr++;
    });
}

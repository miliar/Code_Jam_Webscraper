#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <vector>
#include <utility>
#include <iomanip> 

double find_time(double price_cookie_farm,
                 double extra_rate,
                 double winning_number)
{
  bool not_done = true;
  double current_rate = 2;
  double time_spent = 0;
  while (not_done) {
    double time_at_curr_rate = winning_number/current_rate;

    double time_to_new_farm = price_cookie_farm/current_rate;
    double new_rate = current_rate+extra_rate;
    double time_at_new_rate = time_to_new_farm + winning_number/new_rate;

    if(time_at_new_rate < time_at_curr_rate) {
      current_rate = new_rate;
      time_spent += time_to_new_farm;
    } else {
      not_done = false;
      time_spent += time_at_curr_rate;
    }
  }
  return time_spent;
}

int main()
{
  std::string filename = "testFile_large.in";
  std::ifstream file(filename.c_str());
  int numCases;

  file >> numCases;

  for(int i = 0; i < numCases; ++i) {
    double c, f, x;
    file >> c >> f >> x;

    //    std::cout << c << " " <<f << " " << x << std::endl;


    double result;
    result = find_time(c, f, x);


    // for(std::vector<int>::iterator it = result.begin();
    //     it != result.end();
    //     ++it) {
    //   std::cout << *it << " ";
    // }
    // std::cout << std::endl;


    std::cout << "Case #" << i+1 << ": " << std::setprecision(13) << result << std::endl;;
    // if (result.size() == 1) {
    //   std::cout << result.at(0)  << std::endl;
    // } else if (result.size() == 0 ) {
    //   std::cout << "Volunteer cheated!" << std::endl;
    // } else {
    //   std::cout << "Bad magician!" << std::endl;
    // }
  }
}

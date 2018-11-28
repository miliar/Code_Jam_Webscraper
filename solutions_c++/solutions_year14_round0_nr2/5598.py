#include <fstream>
#include <iostream>
#include <iomanip>
using namespace std;


double recurse(double elapsed_time, double cookie_balance, double current_rate, double farm_cost, double farm_rate, double target){

  if(target - cookie_balance < farm_cost) // Finally reached the end
    return elapsed_time + (target - cookie_balance) / current_rate;

  double new_time = elapsed_time + (farm_cost - cookie_balance) / current_rate;

  double skip_factory = elapsed_time + (target - cookie_balance) / current_rate;

  double buy_factory = 0;
  if(current_rate < target * 100.0)
    buy_factory = recurse(new_time, 0, current_rate + farm_rate, farm_cost, farm_rate, target);

  if(buy_factory == 0) return skip_factory;
  if(skip_factory < buy_factory)
    return skip_factory;
  return buy_factory;
}


int main(){
  //std::ofstream << std::fixed;
  //std::ofstream << std::setprecision(7);

  fstream file;
  ofstream out;

  int num_cases;
  double farm_cost; // C
  double farm_rate; // F
  double target; // X

  file.open("input.dat");
  out.open("output.txt");

  out << std::fixed;
  out << std::setprecision(7);

  file >> num_cases;

  for(int i = 0 ; i < num_cases ; i ++){

    file >> farm_cost;
    file >> farm_rate;
    file >> target;

    out << "Case #" << i + 1 << ": " << recurse(0, 0, 2, farm_cost, farm_rate, target) << endl;

  }

  out.close();

  return 0;
}


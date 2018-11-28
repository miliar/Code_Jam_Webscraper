#include <iostream>
#include <fstream>
#include <iomanip>

int main(int argc, char *argv[])
{
  if (argc < 2) {
    std::cout << "Usage: cookie_clicker [input_file]" << std::endl;
    return 0;
  }

  const char * filename = argv[1];  

  std::ifstream in(filename);
  if(!in.is_open()){
    std::cout << "error opening file " << filename << std::endl;
    return -1;
  }

  std::ofstream out("out.txt");
  if(!out.is_open()){
    std::cout << "error creating output file" << std::endl;
    return -2;
  }

  int test_count = 0;
  float start_speed = 2.0;
  in >> test_count;

  for (int i = 0; i < test_count; ++i) {
    double farm_cost = 0.0;
    double farm_speed = 0.0;
    double total_cookies = 0.0;
    double total_time = 0.0;
    in >> farm_cost;
    in >> farm_speed;
    in >> total_cookies;

    double t_without_farm = 0.0;
    double t_with_farm = 0.0;
    double current_speed = start_speed;
    
    t_without_farm = total_cookies / current_speed;
    t_with_farm = farm_cost / current_speed + 
      total_cookies / (current_speed + farm_speed);
    while (t_with_farm < t_without_farm) {
      total_time += farm_cost / current_speed;
      current_speed += farm_speed;
      t_without_farm = total_cookies / current_speed;
      t_with_farm = farm_cost / current_speed + 
        total_cookies / (current_speed + farm_speed);
    }

    total_time += total_cookies / current_speed;
    
    out << "Case #" << i+1 << ": " 
	<< std::setprecision(7) 
        << std::fixed
        << total_time
        << std::endl;
  }

  in.close();
  out.close();

  return 0;
}

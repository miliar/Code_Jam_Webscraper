/* Cookie Clicker Alpha*/

/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com

 */

#include <string>
#include <iostream>
#include <fstream>
#include <iomanip>


int main()
{
	std::ifstream input_file;
	std::ofstream output_file; 

    input_file.open("input.txt");
    output_file.open("output.txt");
  
	double C, F, X;
	double cookie_per_sec;
	double last_timer;
	double new_timer;

	size_t buy_farm;
	size_t total_cases;
	input_file >> total_cases;
	
	for (size_t case_num = 1; case_num <= total_cases; ++case_num) {	
		input_file >> C;
		input_file >> F;
		input_file >> X;
		
		cookie_per_sec = 2;
		last_timer = (X/cookie_per_sec) + 1;  // so that it is bigger than first new_time
		buy_farm = 0;
		size_t count = 1;

		while (true) {	
			new_timer = 0;
			cookie_per_sec = 2;
			for (size_t b = 1; b <= buy_farm; ++b) {
				new_timer += (C/cookie_per_sec);
				cookie_per_sec += F;
			}	
			new_timer += (X/cookie_per_sec);
			
			if (new_timer >= last_timer) {
				output_file << std::setprecision(7) << std::fixed;
				output_file << "Case #" << case_num << ": " << last_timer << std::endl;
				break;
			}
			last_timer = new_timer;
			++buy_farm;
		}
	} 

    input_file.close();
    output_file.close();
	return 0;
}
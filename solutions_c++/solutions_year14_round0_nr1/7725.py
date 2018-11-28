/* Magic Trick*/

/*
 Auther: MM BARI
 progrmming language: c++
 email: talashbari@gmail.com

 */

#include <string>
#include <iostream>
#include <fstream>
#include <set>
#include <algorithm>


int main()
{
	std::ifstream input_file;
	std::ofstream output_file; 

    input_file.open("input.txt");
    output_file.open("output.txt");
  
	size_t total_cases;
	size_t first_answer;
	size_t second_answer;
	
	input_file >> total_cases;
	
	std::set<size_t> first_row;
	std::set<size_t> second_row;
	std::set<size_t> common_set;
	size_t each_card;

	for (size_t case_num = 1; case_num <= total_cases; ++case_num) {
		input_file >> first_answer;

		for (int row = 1; row <= 4; ++row) {
			for (int col = 1; col <= 4; ++col) {
				input_file >> each_card;
				if (first_answer == row) {
					first_row.insert(each_card);
				}
			}
		}
		
		input_file >> second_answer;

		for (int row = 1; row <= 4; ++row) {
			for (int col = 1; col <= 4; ++col) {
				input_file >> each_card;
				if (second_answer == row) {
					second_row.insert(each_card);
				}
			}
		}

		std::set_intersection(first_row.begin(), first_row.end(), second_row.begin(), second_row.end(),
			std::inserter(common_set, common_set.begin()));

		if (common_set.empty()) {
			output_file << "Case #" << case_num << ": Volunteer cheated!" << std::endl;
		} else if (common_set.size() > 1) {
			output_file << "Case #" << case_num << ": Bad magician!" << std::endl;
		} else {
			output_file << "Case #" << case_num << ": " << *(common_set.begin()) << std::endl;
		}
		
		first_row.clear();
		second_row.clear();
		common_set.clear();
	}

    input_file.close();
    output_file.close();
	return 0;
}
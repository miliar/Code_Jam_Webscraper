#include<iostream>
#include<fstream>
#include<string>
#include<Windows.h>
#include<sstream>

#define COUNTER_RESET counter = 0

int main(int argc, char* argv[]){
	if (argc < 2){
		std::cout << "ENTER MORE ARGUMENTS!";
		return 0;
	}
	char* in_filename = argv[1], *out_filename = "C:\\out.out";
	std::ifstream in_file(in_filename);
	std::ofstream out_file(out_filename);
	char test = ',';
	bool found_answer = false;
	std::string input = "", output = "", holder = "", answer = "";
	int test_cases = 0, test_case_on = 0, counter = 0, int_answer = 0, row_choice = 0, row_choice_2 = 0, index = 0, inner_index = 0, list1[4][4] = { 0 }, list2[4][4] = { 0 };
	std::getline(in_file, input);
	test_cases = std::stoi(input);
	while (test_case_on != test_cases){
		answer = "";
		found_answer = false;
		std::getline(in_file, input);
		row_choice = std::stoi(input);
		std::getline(in_file, input);
		index = 0;
		input += ' ';
		COUNTER_RESET;
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list1[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;
		std::getline(in_file, input);
		input += ' ';
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list1[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;
		std::getline(in_file, input);
		input += ' ';
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list1[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;
		std::getline(in_file, input);
		input += ' ';
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list1[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;

		//assigning second list//
		std::getline(in_file, input);
		row_choice_2 = std::stoi(input);
		std::getline(in_file, input);
		index = 0;
		
		input += ' ';
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list2[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;
		std::getline(in_file, input);
		input += ' ';
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list2[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;
		std::getline(in_file, input);
		input += ' ';
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list2[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;
		std::getline(in_file, input);
		input += ' ';
		while (counter != input.length()){
			holder = "";
			test = ',';
			while (test != ' '){
				test = input.at(counter);
				if (test == ' '){
					counter++;
					break;
				}
				holder += test;
				counter++;
			}
			list2[index][inner_index] = std::stoi(holder);
			inner_index++;
		}
		index++;
		inner_index = 0;
		COUNTER_RESET;
		for (int x = 0; x < 4; x++){
			for (int y = 0; y < 4; y++){
				if (list1[row_choice - 1][x] == list2[row_choice_2 - 1][y] && found_answer){
					answer = "Bad magician!";
					break;
				}
				if (list1[row_choice - 1][x] == list2[row_choice_2 - 1][y] && !found_answer){
					int_answer = list1[row_choice - 1][x];
					found_answer = true;
				}
				
			}
			if (answer == "Bad magician!"){
				break;
			}
		}
		if (answer == "" && found_answer == false){
				answer = "Volunteer cheated!";
			}
		if (answer == ""){
			answer = std::to_string(int_answer);
		}
		output += "Case #" + std::to_string(test_case_on + 1) + ": " + answer + '\n';
		test_case_on++;
	}
	in_file.close();
	out_file << output;
	out_file.close();
	return 0;
}